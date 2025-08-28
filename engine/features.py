import os
from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
from engine.command import speck
#play assistant sound

@eel.expose
def playAssistentSound():
    music_dir = "www\\assets\\audio\\AI.mp3"
    playsound(music_dir)  # Use playsound to play the audio file

def openCommand():
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    if query != "":
        speck("opening"+query)
        os.system(f"start {query}")
    else:
        speck("Please specify what to open.")
