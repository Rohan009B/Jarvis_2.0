# import pyttsx3
# import speech_recognition as sr
# import eel
# engine = pyttsx3.init()
# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# @eel.expose
# def speck(text):
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id) 
#     # engine.setProperty('rate', 174) 
#     print(voices)
#     engine.say(text)
#     engine.runAndWait()

# @eel.expose
# def TakeCommand():
    
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         eel.DisplayMessage("Listening...")
#         r.pause_threshold = 0.8
#         r.adjust_for_ambient_noise(source, duration=1)
#         audio = r.listen(source , 10 , 6)

#     try:
#         print("Recognizing...")    
#         eel.DisplayMessage("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"Recognized: {query}")
#         eel.DisplayMessage(query)
#         speck(query)
#         eel.ShowHood()
#     except Exception as e:
#         print(f"Recognition Error: {e}")
#         eel.DisplayMessage("Sorry, I didn't catch that.")
#         return "None"
#     return query.lower()

# # text = TakeCommand()
# # speck(text)

import pyttsx3
import speech_recognition as sr
import eel

engine = pyttsx3.init()

@eel.expose
def speck(text):
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.say(text)
    engine.runAndWait()

# def TakeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         eel.DisplayMessage("Listening...")
#         r.pause_threshold = 0.8
#         r.adjust_for_ambient_noise(source, duration=1)
#         audio = r.listen(source, timeout=10, phrase_time_limit=6)

#     try:
#         print("Recognizing...")
#         eel.DisplayMessage("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"Recognized: {query}")
#         eel.DisplayMessage(query)
#         speck(query)
#         eel.ShowHood()
#     except Exception as e:
#         print(f"Recognition Error: {e}")
#         eel.DisplayMessage("Sorry, I didn't catch that.")
#         return "None"

#     return query.lower()

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
        # speck(query)
        eel.ShowHood()
        return query.lower()
    except Exception as e:
        print(f"Recognition Error: {e}")
        eel.DisplayMessage("Sorry, I didn't catch that.")
        return "None"

@eel.expose
def allCommands():
    print("allCommands triggered")
    query = TakeCommand()
    print(query)
    if  "open" in query:
        from engine.features import openCommand
        openCommand(query)
    else:
        print("No open command recognized")
   