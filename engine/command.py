import pyttsx3
import speech_recognition as sr
import eel
import time


engine = pyttsx3.init()
engine = pyttsx3.init(driverName='sapi5')

@eel.expose
def speck(text):
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.say(text)
    eel. receiverMessage(text)
    engine.runAndWait()
    
@eel.expose
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except Exception as e:
            print(f"Mic Listen Error: {e}")
            eel.DisplayMessage("Mic error. Try again.")
            return "None"

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Recognized: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        # speck(query)
        return query.lower()
    except Exception as e:
        print(f"Recognition Error: {e}")
        eel.DisplayMessage("Sorry, I didn't catch that.")
        return "None"

@eel.expose
def allCommands(message=None):
    try:
        print("allCommands triggered")

        if message is None or message == "":
            # Voice mode
            query = TakeCommand()

            # ✅ Ensure query is a string
            if isinstance(query, list):
                query = " ".join(map(str, query))

            eel.senderText(query)

        else:
            # Text mode (from chatbox)
            query = message
            if isinstance(query, list):   # ✅ safety
                query = " ".join(map(str, query))
            query = query.lower().strip()
            eel.senderText(query)

        print(f"Query received: {query}")

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import playYouTube
            playYouTube(query)

        elif "send message" in query or "phone call" in query or "vedio call" in query:
            from engine.features import findContacts, whatsApp
            flag = ""
            contacts_no, name = findContacts(query)
            if contacts_no != 0:
                if "send message" in query:
                    flag = 'message'
                    speck("What message do you want to send?")
                    message_text = TakeCommand() if message is None else query
                    if isinstance(message_text, list):   # ✅ flatten here too
                        message_text = " ".join(map(str, message_text))
                    whatsApp(contacts_no, message_text, flag, name)
                elif "phone call" in query:
                    flag = 'call'
                    whatsApp(contacts_no, "", flag, name)
                else:
                    flag = 'vedio call'
                    whatsApp(contacts_no, "", flag, name)

        else:
            from engine.features import chatBot
            response = chatBot(query)   # ✅ now always string
            eel.senderText(response)

    except Exception as e:
        print(f"Error: {e}")

    eel.ShowHood()
