# import os
# import re
# import webbrowser
# from playsound import playsound
# import eel
# from engine.config import ASSISTANT_NAME
# from engine.command import speck
# import pywhatkit as kit
# import _sqlite3
# #play assistant sound
# con = _sqlite3.connect("jarvis2_0.db")
# cursor = con.cursor()

# @eel.expose
# def playAssistentSound():
#     music_dir = "www\\assets\\audio\\AI.mp3"
#     playsound(music_dir)  # Use playsound to play the audio file

# def openCommand(query):
#     query = query.replace(ASSISTANT_NAME, "")
#     query = query.replace("open", "")
#     query = query.lower()
#     # if query != "":
#     #     speck("opening"+query)
#     #     os.system(f"start {query}")
#     # else:
#     #     speck("Please specify what to open.")
#     app_name = query.strip()
#     if app_name != "":
#         try:
#             cursor.execute(
#                 'SELECT path FROM sys_command WHERE LOWER(name) LIKE ?', ('%' + app_name + '%',)
#             )
#             results = cursor.fetchall()
#             if len(results) != 0:
#                 speck(f"Opening " +query)
#                 os.startfile(results[0][0])
#             elif len(results) == 0:
#                 cursor.execute(
#                 'SELECT url FROM web_command WHERE LOWER(name) LIKE ?', ('%' + app_name + '%',)
#                 )
#                 results = cursor.fetchall()

#                 if len(results) != 0:
#                     speck(f"Opening " +query)
#                     webbrowser.open(results[0][0])
#                 else:
#                     speck("Opening "+query)
#                     try:
#                         os.system('start' +query)
#                     except:
#                         speck("Not Found")
#         except :
#             speck("Some thing went Wroung")


# def playYouTube(query):
#     search_term = extract_yt_term(query)
#     speck("Playong " +search_term+ "on YouTube")
#     kit.playonyt(search_term)

# def extract_yt_term(command):
#     pattern =  r'play\s+(.*?)\s+on\s+youtube'
#     match = re.search(pattern, command , re.IGNORECASE)
#     return match.group(1) if match else None  

import os
import re
import struct
import time
import webbrowser
from playsound import playsound
import eel
import pvporcupine
import pyaudio
from engine.config import ASSISTANT_NAME
from engine.command import speck
import pywhatkit as kit
import _sqlite3

from engine.helper import extract_yt_term

# ✅ Connect to SQLite database
con = _sqlite3.connect("jarvis2_0.db")
cursor = con.cursor()

# ✅ Play assistant startup sound
@eel.expose
def playAssistentSound():
    music_dir = "www\\assets\\audio\\AI.mp3"
    playsound(music_dir)

# ✅ Open app or website based on query
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower().strip()
    app_name = query

    if app_name != "":
        speck("I heard: open " + app_name) 
        try:
            # 🔍 Try to open local app from sys_command table
            cursor.execute(
                'SELECT path FROM sys_command WHERE LOWER(name) LIKE ?', ('%' + app_name + '%',)
            )
            results = cursor.fetchall()

            if results:
                speck("Opening " + app_name) 
                os.startfile(results[0][0])
                return

            # 🌐 Try to open website from web_command table
            cursor.execute(
                'SELECT url FROM web_command WHERE LOWER(name) LIKE ?', ('%' + app_name + '%',)
            )
            results = cursor.fetchall()

            if results:
                speck("Opening " + app_name) 
                webbrowser.open(results[0][0])
                return

            # 🧭 Fallback: Try system command
            speck("Opening " + app_name) 
            try:
                os.system('start ' + app_name)
            except Exception:
                speck("Not Found")

        except Exception as e:
            speck("Something went wrong")
            print(f"Error: {e}")

# ✅ Play YouTube video based on voice command
def playYouTube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speck("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speck("Could not extract search term from query")

# # ✅ Extract YouTube search term from command
# def extract_yt_term(command):
#     pattern = r'play\s+(.*?)\s+on\s+youtube'
#     match = re.search(pattern, command, re.IGNORECASE)
#     return match.group(1) if match else None


def hotword():
    porcupine = None
    paud = None
    audio_stream =None
    try :
        #tained Keyboard
        porcupine = pvporcupine.create(keywords = ['jarvis','alexa'])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.simple_rate, channels=1, format=pyaudio.paInt6, input=True, frames_per_buffer=porcupine.frame_length)
        
        #looping streaming
        while True:
            keywords = audio_stream.read(porcupine.frame_length)
            keywords = struct.unpack_from("h"*porcupine.frame_length,keywords)

            #proccesing
            keyword_index = porcupine.process(keywords)

            #checking Keywors 
            if keyword_index >= 0 :
                print("Hot Word Detected")
                eel.activate_siriwave()
                #Use ShorCut Key
                # import pyautogui as autogyi
                # autogyi.keyDown("Alt")
                # autogyi.press("j")
                # time.sleep(2)
                # autogyi.keyUp("Alt")
    except :
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()