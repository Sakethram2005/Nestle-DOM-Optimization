"""
=========================================================
QORA AI
qora.py

Main AI Engine

Integrates all Qora modules into a
single intelligent assistant.

=========================================================
"""

from qora.knowledge import knowledge as KNOWLEDGE_BASE
from qora.analytics import DashboardAnalytics
from qora.recommendation import RecommendationEngine
from qora.reports import ReportGenerator
from qora.memory import ConversationMemory
from qora.realtime import RealtimeEngine
from qora.quantum_knowledge import QuantumKnowledge

class QoraAI:

    def __init__(self, dataframe=None, username="guest"):

        self.dataframe = dataframe

        if dataframe is not None:
            self.analytics = DashboardAnalytics(dataframe)
            self.recommendations = RecommendationEngine(self.analytics)
            self.reports = ReportGenerator(self.analytics)
            self.realtime = RealtimeEngine(self.analytics)
        else:
            self.analytics = None
            self.recommendations = None
            self.reports = None
            self.realtime = RealtimeEngine()

        # Quantum results are cached separately from the main
        # dataframe (see quantum_optimizer.py) — this works even
        # if no dataframe was passed in at all.
        self.quantum = QuantumKnowledge()

        self.username = username

        self.memory = ConversationMemory()

        self.memory.load_user_memory(username)

    # =====================================================
    # MEMORY
    # =====================================================

    def remember_user(self, message):

        self.memory.add_user(message)

    def remember_ai(self, message):

        self.memory.add_ai(message)

    # =====================================================
    # KNOWLEDGE SEARCH
    # =====================================================

    def search_knowledge(self, question):

        question = question.lower()

        for topic in KNOWLEDGE_BASE.values():

            for keyword in topic["keywords"]:

                if keyword.lower() in question:
                    return topic["answer"]

        return None

    # =====================================================
    # ANALYTICS SUMMARY
    # =====================================================

    def dashboard_summary(self):

        if self.analytics is None:
            return "Dashboard data not available."

        return self.analytics.planner_summary()

    # =====================================================
    # AI RECOMMENDATIONS
    # =====================================================

    def recommendations_summary(self):

        if self.recommendations is None:
            return "Recommendation engine unavailable."

        return self.recommendations.recommendation_report()
    
        # =====================================================
    # REPORTS
    # =====================================================

    def generate_report(self):

        if self.reports is None:
            return "Report generator unavailable."

        return self.reports.planner_report()

    # =====================================================
    # REALTIME STATUS
    # =====================================================

    def realtime_status(self):

        return self.realtime.status()

    # =====================================================
    # MAIN QUESTION ANSWERING
    # =====================================================

    def ask(self, question):

        self.remember_user(question)

        q = question.lower()

        # -------------------------------
        # Quantum optimization results (objective value, feasibility,
        # optimality gap, runtime, why only N orders selected, etc.)
        # Checked FIRST — these are specific questions about the
        # cached QAOA/exact/greedy run, not the general dashboard data.
        # -------------------------------

        quantum_answer = self.quantum.answer(q)

        if quantum_answer is not None:
            self.remember_ai(str(quantum_answer))
            self.memory.save_user_memory(self.username)
            return quantum_answer

        # -------------------------------
        # Live dashboard data (utilization, shipping cost, revenue,
        # best/worst plant, top products, penalties, carbon, etc. —
        # ~49 intents in DashboardAnalytics.answer()) — always tried
        # before the static FAQ, so any question the live data can
        # answer takes priority over a generic canned response.
        # -------------------------------

        if self.analytics is not None:

            data_answer = self.analytics.answer(q)

            if data_answer is not None and data_answer not in (
                "Sorry, I couldn't understand that analytics question.",
            ):
                self.remember_ai(str(data_answer))
                self.memory.save_user_memory(self.username)
                return data_answer

        # -------------------------------
        # Knowledge Base
        # -------------------------------

        answer = self.search_knowledge(q)

        if answer is not None:

            self.remember_ai(answer)

            self.memory.save_user_memory(
            self.username
            )

            return answer

                        


        # -------------------------------
        # Dashboard Summary
        # -------------------------------

        if "summary" in q:

            answer = self.dashboard_summary()

            self.remember_ai(answer)

            return answer

        # -------------------------------
        # Recommendations
        # -------------------------------

        if "recommendation" in q or "suggestion" in q:

            answer = self.recommendations_summary()

            self.remember_ai(answer)

            return answer

        # -------------------------------
        # Planner Report
        # -------------------------------

        if "report" in q:

            answer = self.generate_report()

            self.remember_ai(answer)

            return answer

        # -------------------------------
        # Realtime
        # -------------------------------

        if "status" in q:

            answer = str(self.realtime_status())

            self.remember_ai(answer)

            return answer

        # -------------------------------
        # Memory
        # -------------------------------

        if "history" in q:

            answer = self.memory.recent_context()

            self.remember_ai(answer)

            return answer

        # -------------------------------
        # Default
        # -------------------------------

        answer = (
            "Sorry, I couldn't understand your question. "
            "Try asking about reports, analytics, recommendations, "
            "dashboard summary or warehouse optimization."
        )

        self.remember_ai(answer)

        return answer
    
        # =====================================================
    # VOICE SUPPORT
    # =====================================================

    def speak(self, text):

        return self.voice.speak(text)

    def listen(self):

        return self.voice.listen()

    def voice_chat(self):

        question = self.listen()

        if not isinstance(question, str):
            return question

        answer = self.ask(question)

        self.speak(answer)

        return answer

    # =====================================================
    # SESSION MANAGEMENT
    # =====================================================

    def reset_session(self):

        self.memory.clear()

        if self.realtime:
            self.realtime.reset()

        return "Qora AI session has been reset."

    # =====================================================
    # SYSTEM STATUS
    # =====================================================

    def system_status(self):

        return {

            "Analytics": self.analytics is not None,

            "Recommendations": self.recommendations is not None,

            "Reports": self.reports is not None,

            "Memory": True,

            "Realtime": True,


        }

    # =====================================================
    # EXPORT SYSTEM INFORMATION
    # =====================================================

    def export(self):

        return {

            "status": self.system_status(),

            "memory": self.memory.export(),

            "realtime": self.realtime.export(),


        }

    # =====================================================
    # DIAGNOSTICS
    # =====================================================

    def diagnostics(self):

        return {

            "System": self.system_status(),

            "Realtime": self.realtime.status(),

            "Memory": self.memory.summary(),


        }

    # =====================================================
    # HELP
    # =====================================================

    def help(self):

        return """
Available Commands

• Dashboard Summary
• Planner Report
• Recommendations
• Warehouse Analytics
• Inventory Analytics
• Revenue Analysis
• Shipping Cost
• Carbon Emissions
• Fill Rate
• Voice Chat
• Conversation History
• System Status
• Diagnostics
"""
    # =====================================================
    # CHAT CLEAR
    # =====================================================

    def clear_chat(self):

        self.memory.clear()

        self.memory.save_user_memory(
            self.username
        )

        return "Chat cleared."
    
    
# =====================================================
# END OF FILE
# =====================================================