"""
=========================================================
QORA AI
voice.py

Voice Input / Output Engine

Provides speech recognition
and text-to-speech support.

=========================================================
"""

try:
    import speech_recognition as sr
except ImportError:
    sr = None

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None


class VoiceEngine:

    def __init__(self):

        self.recognizer = sr.Recognizer() if sr else None

        if pyttsx3:
            self.engine = pyttsx3.init()
            self.engine.setProperty("rate", 170)
            self.engine.setProperty("volume", 1.0)
        else:
            self.engine = None

    # =====================================================
    # TEXT TO SPEECH
    # =====================================================

    def speak(self, text):

        if self.engine is None:
            return "Text-to-Speech library not installed."

        self.engine.say(str(text))
        self.engine.runAndWait()

        return "Speech completed."

    # =====================================================
    # SPEAK WITHOUT RETURN
    # =====================================================

    def say(self, text):

        if self.engine is not None:
            self.engine.say(str(text))
            self.engine.runAndWait()

    # =====================================================
    # MICROPHONE INPUT
    # =====================================================

    def listen(self, timeout=5):

        if self.recognizer is None:
            return "SpeechRecognition library not installed."

        try:
            with sr.Microphone() as source:

                self.recognizer.adjust_for_ambient_noise(source)

                print("Listening...")

                audio = self.recognizer.listen(
                    source,
                    timeout=timeout
                )

            return self.recognizer.recognize_google(audio)

        except Exception as e:

            return str(e)

    # =====================================================
    # SPEAK DASHBOARD SUMMARY
    # =====================================================

    def speak_summary(self, summary):

        self.say(summary)

        return "Dashboard summary spoken."

    # =====================================================
    # VOICE STATUS
    # =====================================================

    def status(self):

        return {

            "Speech Recognition": sr is not None,

            "Text To Speech": pyttsx3 is not None

        }
    
        # =====================================================
    # VOICE COMMANDS
    # =====================================================

    def recognize_command(self, timeout=5):

        text = self.listen(timeout)

        if not isinstance(text, str):
            return None

        return text.lower()

    # =====================================================
    # PROCESS COMMAND
    # =====================================================

    def process_command(self, command):

        if not command:
            return "No command detected."

        command = command.lower()

        if "hello" in command:
            return "Hello! I am Qora AI."

        elif "summary" in command:
            return "Generating dashboard summary."

        elif "report" in command:
            return "Preparing planner report."

        elif "refresh" in command:
            return "Refreshing dashboard."

        elif "help" in command:
            return (
                "Available commands include summary, report, "
                "refresh, analytics and exit."
            )

        elif "exit" in command:
            return "Ending voice session."

        return "Command not recognized."

    # =====================================================
    # VOICE RESPONSE
    # =====================================================

    def respond(self, text):

        self.say(text)

        return text

    # =====================================================
    # LISTEN AND RESPOND
    # =====================================================

    def listen_and_respond(self):

        command = self.recognize_command()

        response = self.process_command(command)

        self.respond(response)

        return response

    # =====================================================
    # VOICE SETTINGS
    # =====================================================

    def set_rate(self, rate):

        if self.engine:
            self.engine.setProperty("rate", rate)

    def set_volume(self, volume):

        if self.engine:
            self.engine.setProperty("volume", volume)

    # =====================================================
    # AVAILABLE VOICES
    # =====================================================

    def available_voices(self):

        if self.engine is None:
            return []

        voices = self.engine.getProperty("voices")

        return [voice.name for voice in voices]

    # =====================================================
    # CHANGE VOICE
    # =====================================================

    def set_voice(self, index=0):

        if self.engine is None:
            return False

        voices = self.engine.getProperty("voices")

        if 0 <= index < len(voices):
            self.engine.setProperty("voice", voices[index].id)
            return True

        return False

    # =====================================================
    # VOICE HISTORY
    # =====================================================

    def voice_history(self):

        if not hasattr(self, "_history"):
            self._history = []

        return self._history

    def add_history(self, text):

        if not hasattr(self, "_history"):
            self._history = []

        self._history.append(text)

        if len(self._history) > 100:
            self._history.pop(0)

        # =====================================================
    # EXPORT TRANSCRIPT
    # =====================================================

    def export_transcript(self):

        if not hasattr(self, "_history"):
            self._history = []

        return "\n".join(self._history)

    # =====================================================
    # SAVE TRANSCRIPT
    # =====================================================

    def save_transcript(self, filename="voice_transcript.txt"):

        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.export_transcript())

        return filename

    # =====================================================
    # VOICE SESSION REPORT
    # =====================================================

    def session_report(self):

        history = self.voice_history()

        return {
            "Total Commands": len(history),
            "Speech Recognition": self.recognizer is not None,
            "Text To Speech": self.engine is not None,
            "Current Rate":
                self.engine.getProperty("rate")
                if self.engine else None,
            "Current Volume":
                self.engine.getProperty("volume")
                if self.engine else None
        }

    # =====================================================
    # DIAGNOSTICS
    # =====================================================

    def diagnostics(self):

        return {
            "Recognizer Available": self.recognizer is not None,
            "TTS Available": self.engine is not None,
            "Voices Installed": len(self.available_voices())
        }

    # =====================================================
    # RESET ENGINE
    # =====================================================

    def reset(self):

        if hasattr(self, "_history"):
            self._history.clear()

        return "Voice engine has been reset."

    # =====================================================
    # EXPORT
    # =====================================================

    def export(self):

        return {
            "status": self.status(),
            "diagnostics": self.diagnostics(),
            "session": self.session_report(),
            "history": self.voice_history(),
            "transcript": self.export_transcript()
        }

# =====================================================
# END OF FILE
# =====================================================        