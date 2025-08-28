import os
import eel
eel.init('www')
from engine.features import *
from engine.command import *

playAssistentSound()

os.system('start msedge.exe --app="http://localhost:8000//main.html"')
eel.start('main.html', mode=None, host='localhost', block=True)

