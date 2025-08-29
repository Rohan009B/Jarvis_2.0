import pyttsx3
import speech_recognition as sr
import eel
import time


engine = pyttsx3.init()

@eel.expose
def speck(text):
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.say(text)
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
def allCommands():
    try:
        print("allCommands triggered")
        query = TakeCommand()
        print(query)
        if  "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube":
            from engine.features import playYouTube
            playYouTube(query)
        else:
            print("No open command recognized")
    except:
        print("Error")

    eel.ShowHood()
   