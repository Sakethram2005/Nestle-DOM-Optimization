"""
=========================================================
QORA AI
memory.py

Advanced Conversation Memory Engine

Features:
- Temporary session memory
- Permanent user memory
- Save / Load conversations
- Search history
- Conversation analytics
- User based chat storage

=========================================================
"""


from datetime import datetime
import json
import os



class ConversationMemory:


    def __init__(self, max_history=100):

        self.max_history = max_history
        self.history = []



    # =====================================================
    # ADD MESSAGE
    # =====================================================

    def add(self, role, message):

        self.history.append({

            "time":
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "role": role,

            "message": message

        })


        if len(self.history) > self.max_history:

            self.history.pop(0)



    # =====================================================
    # USER MESSAGE
    # =====================================================

    def add_user(self,message):

        self.add(
            "User",
            message
        )



    # =====================================================
    # AI MESSAGE
    # =====================================================

    def add_ai(self,message):

        self.add(
            "Qora AI",
            message
        )



    # =====================================================
    # GET HISTORY
    # =====================================================

    def get_history(self):

        return self.history.copy()



    # =====================================================
    # LAST MESSAGE
    # =====================================================

    def last_message(self):

        if not self.history:

            return None


        return self.history[-1]



    # =====================================================
    # LAST USER MESSAGE
    # =====================================================

    def last_user_message(self):

        for item in reversed(self.history):

            if item["role"]=="User":

                return item


        return None



    # =====================================================
    # LAST AI MESSAGE
    # =====================================================

    def last_ai_message(self):

        for item in reversed(self.history):

            if item["role"]=="Qora AI":

                return item


        return None



    # =====================================================
    # TOTAL MESSAGES
    # =====================================================

    def total_messages(self):

        return len(self.history)



    # =====================================================
    # CLEAR MEMORY
    # =====================================================

    def clear(self):

        self.history=[]



    # =====================================================
    # SEARCH MEMORY
    # =====================================================

    def search(self,keyword):

        keyword=keyword.lower()

        result=[]


        for item in self.history:

            if keyword in item["message"].lower():

                result.append(item)



        return result



    # =====================================================
    # LAST N MESSAGES
    # =====================================================

    def last(self,n=5):

        return self.history[-n:]



    # =====================================================
    # USER QUESTIONS
    # =====================================================

    def user_questions(self):

        return [

            item["message"]

            for item in self.history

            if item["role"]=="User"

        ]



    # =====================================================
    # AI ANSWERS
    # =====================================================

    def ai_answers(self):

        return [

            item["message"]

            for item in self.history

            if item["role"]=="Qora AI"

        ]



    # =====================================================
    # SUMMARY
    # =====================================================

    def summary(self):

        return {


            "Total Messages":
            self.total_messages(),


            "User Messages":
            len(self.user_questions()),


            "AI Messages":
            len(self.ai_answers()),


            "First Message":
            self.history[0]["message"]
            if self.history else None,


            "Last Message":
            self.history[-1]["message"]
            if self.history else None

        }




    # =====================================================
    # RECENT CONTEXT
    # =====================================================

    def recent_context(self,n=5):

        context=""


        for item in self.last(n):

            context += (

                f"{item['role']}: "
                f"{item['message']}\n"

            )


        return context



    # =====================================================
    # EXPORT MEMORY
    # =====================================================

    def export(self):

        return {


            "messages":
            self.history,


            "summary":
            self.summary()

        }




    # =====================================================
    # SAVE NORMAL MEMORY
    # =====================================================

    def save(self,filename="memory.json"):


        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(

                self.history,

                file,

                indent=4,

                ensure_ascii=False

            )


        return filename





    # =====================================================
    # LOAD NORMAL MEMORY
    # =====================================================

    def load(self,filename="memory.json"):


        if not os.path.exists(filename):

            return False



        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:


            self.history=json.load(file)



        return True




    # =====================================================
    # USER BASED MEMORY STORAGE
    # ChatGPT style history
    # =====================================================

    def save_user_memory(self,username):


        folder="qora/chats"


        os.makedirs(
            folder,
            exist_ok=True
        )


        filename=f"{folder}/{username}.json"



        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(

                self.history,

                file,

                indent=4,

                ensure_ascii=False

            )


        return filename





    # =====================================================
    # LOAD USER MEMORY
    # =====================================================

    def load_user_memory(self,username):


        filename=f"qora/chats/{username}.json"



        if not os.path.exists(filename):

            return False



        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:


            self.history=json.load(file)



        return True




    # =====================================================
    # DELETE USER MEMORY
    # =====================================================

    def delete_user_memory(self,username):


        filename=f"qora/chats/{username}.json"



        if os.path.exists(filename):

            os.remove(filename)

            return True



        return False




    # =====================================================
    # REPLAY CONVERSATION
    # =====================================================

    def replay(self):


        lines=[]


        for item in self.history:


            lines.append(

                f"{item['role']}: "
                f"{item['message']}"

            )



        return "\n".join(lines)





    # =====================================================
    # STATISTICS
    # =====================================================

    def statistics(self):


        return {


            "Total Messages":
            self.total_messages(),


            "User Messages":
            len(self.user_questions()),


            "AI Messages":
            len(self.ai_answers()),


            "Memory Limit":
            self.max_history,


            "Usage (%)":
            round(

                len(self.history)
                /
                self.max_history
                *
                100,

                2

            )

        }





    # =====================================================
    # RESET SESSION
    # =====================================================

    def reset_session(self):

        self.clear()

        return "Conversation cleared successfully."





    # =====================================================
    # FULL REPORT
    # =====================================================

    def report(self):


        return {


            "Summary":
            self.summary(),


            "Statistics":
            self.statistics(),


            "Context":
            self.recent_context(),


            "History":
            self.history

        }



# =====================================================
# END OF FILE
# =====================================================