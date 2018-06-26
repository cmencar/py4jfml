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
        subprocess.call(['java', '-jar', upperDir+'/jar_files/Java_EntryPoint.jar'])

EntryPointThread = Java_EntryPointThread()
EntryPointThread.start()
time.sleep(1)