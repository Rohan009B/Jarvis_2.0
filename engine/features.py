import os
import re
from shlex import quote
import struct
import subprocess
import time
import webbrowser
from playsound import playsound
import eel
import pvporcupine
import pyaudio
import pyautogui

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.config import ASSISTANT_NAME

from engine.command import speck
import pywhatkit as kit
import _sqlite3

from engine.helper import extract_yt_term, remove_words
from hugchat import hugchat

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

#Find Contacts
def findContacts(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove).strip().lower()

    try:
        cursor.execute("SELECT name, mobile_no FROM contacts")
        results = cursor.fetchall()

        matched_contacts = []
        for name, mobile_no in results:
            if query in name.lower():
                matched_contacts.append((name, mobile_no))

        if len(matched_contacts) == 0:
            speck('Contact not found')
            return 0, 0
        elif len(matched_contacts) == 1:
            name, mobile_number = matched_contacts[0]
        else:
            # If multiple matches, ask user
            speck("I found multiple contacts. Please say the full name.")
            print("Multiple matches:", matched_contacts)
            return 0, 0

        mobile_number_str = str(mobile_number)
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, name

    except Exception as e:
        speck('Error finding contact')
        print(f"DB Error: {e}")
        return 0, 0


def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        jarvis_message = "Message sent successfully to " + name
    elif flag == 'call':
        message = ''
        jarvis_message = 'Calling ' + name
    else:
        message = ''
        jarvis_message = 'Starting video call with ' + name

    encoded_message = quote(message)
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"  # ✅ fixed
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp
    subprocess.run(full_command, shell=True)
    time.sleep(6)  # wait for WhatsApp to load

    # Press Enter to send the message automatically
    if flag == 'message':
        pyautogui.press("enter")

    speck(jarvis_message)

#chat Bot
# Chat Bot
def chatBot(query):
    try:
        # ✅ Always normalize query
        if query is None:
            query = ""
        elif isinstance(query, list):
            query = " ".join(map(str, query))
        else:
            query = str(query)

        user_input = query.lower().strip()

        # ✅ Initialize HugChat
        bot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
        conv_id = bot.new_conversation()
        bot.change_conversation(conv_id)

        # ✅ Get response
        response = bot.chat(user_input)

        print(f"ChatBot Response: {response}")
        return response

    except Exception as e:
        print(f"ChatBot Error: {e}")
        return "Sorry, I couldn't process that request."

    
