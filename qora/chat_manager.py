"""
====================================================
QORA AI
Chat Manager

Features:
- User login
- User profile
- Chat saving
- Chat history
- Rename chat
- Delete chat
- Search chats
- Continue old conversation
====================================================
"""

import os
import json
import uuid
from datetime import datetime


CHAT_FOLDER = "qora/chats"



class ChatManager:


    def __init__(self):

        os.makedirs(
            CHAT_FOLDER,
            exist_ok=True
        )


    # =========================
    # USER PROFILE
    # =========================

    def create_user(self, username):

        profile = {
            "username": username,
            "created": str(datetime.now()),
            "chats":[]
        }


        file = f"{CHAT_FOLDER}/{username}_profile.json"


        if not os.path.exists(file):

            with open(file,"w") as f:

                json.dump(
                    profile,
                    f,
                    indent=4
                )


        return profile



    def get_profile(self,username):


        file=f"{CHAT_FOLDER}/{username}_profile.json"


        if os.path.exists(file):

            with open(file,"r") as f:

                return json.load(f)


        return self.create_user(username)



    # =========================
    # CREATE NEW CHAT
    # =========================


    def create_chat(
            self,
            username,
            title="New Chat"
    ):


        chat_id=str(uuid.uuid4())


        chat={

            "id":chat_id,

            "title":title,

            "created":
            str(datetime.now()),

            "messages":[]

        }


        file=f"{CHAT_FOLDER}/{chat_id}.json"


        with open(file,"w") as f:

            json.dump(
                chat,
                f,
                indent=4
            )



        profile=self.get_profile(username)


        profile["chats"].append(chat_id)


        self.save_profile(
            username,
            profile
        )


        return chat_id




    # =========================
    # SAVE MESSAGE
    # =========================


    def add_message(
        self,
        chat_id,
        role,
        content
    ):


        chat=self.load_chat(chat_id)


        chat["messages"].append({

            "role":role,

            "content":content,

            "time":
            str(datetime.now())

        })


        self.save_chat(
            chat
        )

    # =========================
    # CLEAR CHAT MESSAGES
    # =========================

    def clear_messages(self, chat_id):


        chat = self.load_chat(chat_id)


        if chat:


            chat["messages"] = []


            self.save_chat(chat)


            return True


        return False


    # =========================
    # LOAD CHAT
    # =========================


    def load_chat(self,chat_id):


        file=f"{CHAT_FOLDER}/{chat_id}.json"


        if os.path.exists(file):

            with open(file,"r") as f:

                return json.load(f)


        return None



    # =========================
    # SAVE CHAT
    # =========================


    def save_chat(self,chat):


        file=f"{CHAT_FOLDER}/{chat['id']}.json"


        with open(file,"w") as f:

            json.dump(
                chat,
                f,
                indent=4
            )



    # =========================
    # CHAT HISTORY
    # =========================


    def history(self,username):


        profile=self.get_profile(username)


        chats=[]


        for cid in profile["chats"]:


            chat=self.load_chat(cid)


            if chat:

                chats.append(chat)



        return chats




    # =========================
    # RENAME CHAT
    # =========================


    def rename_chat(
        self,
        chat_id,
        new_name
    ):


        chat=self.load_chat(chat_id)


        if chat:

            chat["title"]=new_name

            self.save_chat(chat)

            return True


        return False




    # =========================
    # DELETE CHAT
    # =========================


    def delete_chat(
        self,
        username,
        chat_id
    ):


        file=f"{CHAT_FOLDER}/{chat_id}.json"


        if os.path.exists(file):

            os.remove(file)



        profile=self.get_profile(username)


        if chat_id in profile["chats"]:

            profile["chats"].remove(chat_id)


        self.save_profile(
            username,
            profile
        )



        return True




    # =========================
    # SEARCH CHAT
    # =========================


    def search(
        self,
        username,
        keyword
    ):


        result=[]


        for chat in self.history(username):


            if keyword.lower() in chat["title"].lower():

                result.append(chat)



        return result




    # =========================
    # SAVE PROFILE
    # =========================


    def save_profile(
        self,
        username,
        profile
    ):


        file=f"{CHAT_FOLDER}/{username}_profile.json"


        with open(file,"w") as f:

            json.dump(
                profile,
                f,
                indent=4
            )