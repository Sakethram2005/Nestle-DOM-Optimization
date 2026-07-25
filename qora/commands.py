"""
=========================================================
QORA AI
commands.py

Natural Language Dashboard Commands

=========================================================
"""

import re


class DashboardCommands:
    """
    Understands user commands and converts them
    into dashboard actions.
    """

    def __init__(self):
        pass

    # =====================================================
    # Normalize Text
    # =====================================================

    def normalize(self, text):

        text = text.lower().strip()

        text = re.sub(r"\s+", " ", text)

        return text

    # =====================================================
    # Main Command Parser
    # =====================================================

    def parse(self, user_input):

        query = self.normalize(user_input)

        # ----------------------------------------
        # Dashboard
        # ----------------------------------------

        if any(word in query for word in [
            "dashboard",
            "home",
            "main page",
            "open dashboard",
            "show dashboard"
        ]):

            return {
                "action": "dashboard",
                "message": "Opening Dashboard..."
            }

        # ----------------------------------------
        # Analytics
        # ----------------------------------------

        if any(word in query for word in [
            "analytics",
            "analysis",
            "charts",
            "graphs",
            "statistics",
            "show analytics"
        ]):

            return {
                "action": "analytics",
                "message": "Opening Analytics..."
            }

        # ----------------------------------------
        # Orders
        # ----------------------------------------

        if any(word in query for word in [
            "orders",
            "order table",
            "show orders",
            "customer orders"
        ]):

            return {
                "action": "orders",
                "message": "Opening Orders..."
            }

        # ----------------------------------------
        # About Project
        # ----------------------------------------

        if any(word in query for word in [
            "about",
            "project",
            "about project",
            "project details"
        ]):

            return {
                "action": "about",
                "message": "Opening About Project..."
            }

        # ----------------------------------------
        # Revenue
        # ----------------------------------------

        if any(word in query for word in [
            "revenue",
            "show revenue",
            "sales"
        ]):

            return {
                "action": "show_revenue",
                "message": "Showing Revenue..."
            }

        # ----------------------------------------
        # Fill Rate
        # ----------------------------------------

        if any(word in query for word in [
            "fill rate",
            "fillrate",
            "service level"
        ]):

            return {
                "action": "show_fillrate",
                "message": "Showing Fill Rate..."
            }

        # ----------------------------------------
        # Shipping Cost
        # ----------------------------------------

        if any(word in query for word in [
            "shipping",
            "shipping cost",
            "transport cost"
        ]):

            return {
                "action": "shipping",
                "message": "Showing Shipping Cost..."
            }

        # ----------------------------------------
        # Carbon
        # ----------------------------------------

        if any(word in query for word in [
            "carbon",
            "carbon emissions",
            "co2",
            "environment"
        ]):

            return {
                "action": "carbon",
                "message": "Showing Carbon Emissions..."
            }

        # ----------------------------------------
        # Benchmark
        # ----------------------------------------

        if any(word in query for word in [
            "benchmark",
            "comparison",
            "classical vs quantum",
            "quantum"
        ]):

            return {
                "action": "benchmark",
                "message": "Opening Benchmark Report..."
            }

        # ----------------------------------------
        # Unknown
        # ----------------------------------------

        return {
            "action": "unknown",
            "message": "Sorry, I couldn't understand that command."
        }
        # =====================================================
    # ADVANCED COMMANDS
    # =====================================================

    def advanced_commands(self, user_input):

        query = self.normalize(user_input)

        # ----------------------------------------
        # Plant Commands
        # ----------------------------------------

        for i in range(1, 21):

            if f"plant {i}" in query:

                return {
                    "action": "show_plant",
                    "plant": f"Plant {i}",
                    "message": f"Showing Plant {i}..."
                }

        # ----------------------------------------
        # Warehouse Commands
        # ----------------------------------------

        for i in range(1, 51):

            if f"warehouse {i}" in query:

                return {
                    "action": "show_warehouse",
                    "warehouse": f"Warehouse {i}",
                    "message": f"Showing Warehouse {i}..."
                }

        # ----------------------------------------
        # Report Commands
        # ----------------------------------------

        if any(word in query for word in [
            "download report",
            "generate report",
            "planner report",
            "create report",
            "report"
        ]):

            return {
                "action": "report",
                "message": "Generating Planner Report..."
            }

        # ----------------------------------------
        # PDF Export
        # ----------------------------------------

        if any(word in query for word in [
            "pdf",
            "export pdf",
            "download pdf"
        ]):

            return {
                "action": "pdf",
                "message": "Exporting PDF..."
            }

        # ----------------------------------------
        # PowerPoint Export
        # ----------------------------------------

        if any(word in query for word in [
            "ppt",
            "pptx",
            "powerpoint",
            "presentation",
            "export ppt"
        ]):

            return {
                "action": "ppt",
                "message": "Creating PowerPoint..."
            }

        # ----------------------------------------
        # Excel Export
        # ----------------------------------------

        if any(word in query for word in [
            "excel",
            "xlsx",
            "csv",
            "export excel",
            "download excel"
        ]):

            return {
                "action": "excel",
                "message": "Exporting Excel..."
            }

        # ----------------------------------------
        # Refresh
        # ----------------------------------------

        if any(word in query for word in [
            "refresh",
            "reload",
            "update dashboard",
            "refresh dashboard"
        ]):

            return {
                "action": "refresh",
                "message": "Refreshing Dashboard..."
            }

        # ----------------------------------------
        # Reset
        # ----------------------------------------

        if any(word in query for word in [
            "reset",
            "clear filters",
            "reset filters",
            "remove filters"
        ]):

            return {
                "action": "reset",
                "message": "Resetting Dashboard Filters..."
            }

        # ----------------------------------------
        # Dashboard Summary
        # ----------------------------------------

        if any(word in query for word in [
            "summary",
            "dashboard summary",
            "summarize dashboard",
            "executive summary"
        ]):

            return {
                "action": "summary",
                "message": "Generating Dashboard Summary..."
            }

        # ----------------------------------------
        # Recommendations
        # ----------------------------------------

        if any(word in query for word in [
            "recommendation",
            "recommend",
            "suggestion",
            "improve dashboard",
            "optimization suggestion"
        ]):

            return {
                "action": "recommendations",
                "message": "Generating AI Recommendations..."
            }

        # ----------------------------------------
        # Top Warehouse
        # ----------------------------------------

        if any(word in query for word in [
            "best warehouse",
            "top warehouse",
            "highest revenue warehouse"
        ]):

            return {
                "action": "best_warehouse",
                "message": "Finding Best Warehouse..."
            }

        # ----------------------------------------
        # Top Plant
        # ----------------------------------------

        if any(word in query for word in [
            "best plant",
            "top plant",
            "highest revenue plant"
        ]):

            return {
                "action": "best_plant",
                "message": "Finding Best Plant..."
            }

        return None
    
        # =====================================================
    # SMART COMMAND PARSER
    # =====================================================

    def execute(self, user_input):
        """
        Main entry point for Qora AI command detection.
        """

        # First check advanced commands
        result = self.advanced_commands(user_input)

        if result is not None:
            return result

        # Then check basic commands
        return self.parse(user_input)

    # =====================================================
    # CONVERSATIONAL COMMANDS
    # =====================================================

    def chat_command(self, user_input):

        query = self.normalize(user_input)

        conversation_patterns = {

            "show revenue": "show_revenue",
            "display revenue": "show_revenue",
            "open revenue": "show_revenue",
            "revenue chart": "show_revenue",

            "show dashboard": "dashboard",
            "open dashboard": "dashboard",
            "go to dashboard": "dashboard",
            "dashboard": "dashboard",

            "show analytics": "analytics",
            "open analytics": "analytics",
            "analytics": "analytics",

            "show graphs": "analytics",
            "display graphs": "analytics",

            "show orders": "orders",
            "order table": "orders",

            "show carbon": "carbon",
            "carbon emissions": "carbon",

            "show shipping": "shipping",
            "shipping cost": "shipping",

            "show fill rate": "show_fillrate",

            "show benchmark": "benchmark",

            "show report": "report",
            "planner report": "report",

            "download pdf": "pdf",
            "download ppt": "ppt",
            "download excel": "excel",

            "refresh": "refresh",
            "reload dashboard": "refresh",

            "reset": "reset",
            "clear filters": "reset",

            "summary": "summary",
            "dashboard summary": "summary",

            "recommendations": "recommendations",
            "ai recommendations": "recommendations",

            "best warehouse": "best_warehouse",
            "best plant": "best_plant"
        }

        for phrase, action in conversation_patterns.items():

            if phrase in query:

                return {
                    "action": action,
                    "message": f"Executing '{action}'..."
                }

        return None

    # =====================================================
    # SIRI / ALEXA STYLE COMMANDS
    # =====================================================

    def assistant_command(self, user_input):

        query = self.normalize(user_input)

        wake_words = [
            "qora",
            "hey qora",
            "hello qora",
            "hi qora",
            "assistant",
            "ai",
            "qora ai"
        ]

        for wake in wake_words:

            if wake in query:

                cleaned = query.replace(wake, "").strip()

                if cleaned == "":
                    return {
                        "action": "greeting",
                        "message": "Hello! How can I help you?"
                    }

                result = self.execute(cleaned)

                return result

        return self.execute(query)

    # =====================================================
    # HELP
    # =====================================================

    def help_commands(self):

        return [

            "Show Dashboard",

            "Open Analytics",

            "Show Orders",

            "Show Revenue",

            "Show Shipping Cost",

            "Show Carbon Emissions",

            "Show Fill Rate",

            "Show Plant 1",

            "Show Warehouse 5",

            "Best Warehouse",

            "Best Plant",

            "Dashboard Summary",

            "Generate Report",

            "Export PDF",

            "Export PPT",

            "Export Excel",

            "Refresh Dashboard",

            "Reset Filters",

            "AI Recommendations"

        ]

    # =====================================================
    # ABOUT
    # =====================================================

    def about(self):

        return """
Qora AI Command Engine

Features:
• Natural language dashboard control
• Dashboard navigation
• Analytics commands
• Report generation
• Export support
• Smart recommendations
• Plant & warehouse commands
• Siri/Alexa style command recognition
"""

# =========================================================
# END OF FILE
# =========================================================