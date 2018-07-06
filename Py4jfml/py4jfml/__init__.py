import subprocess
from threading import Thread
import time
import os

#definizione thread per avviare il server py4j
class Java_EntryPointThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        upperDir = os.path.dirname(os.getcwd())
        subprocess.call(['java', '-jar', upperDir+'/jar_files/JFML_EntryPoint.jar'])

entryPointThread = Java_EntryPointThread()
entryPointThread.start()
time.sleep(1)