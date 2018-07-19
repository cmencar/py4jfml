import subprocess
from threading import Thread
import time
import os
import platform

#Thread to run PY4J server
class Java_EntryPointThread(Thread):
    '''
    Python class to run PY4J server.
    '''
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        upperDir = os.path.dirname(os.getcwd())
        if(platform.system()=='Linux'):
            subprocess.call(['java', '-jar', upperDir + '/jar_files/JFML_EntryPoint.jar'])
        if(platform.system()=='Windows'):
            subprocess.call(['java', '-jar', upperDir + '\jar_files\JFML_EntryPoint.jar'])

entryPointThread = Java_EntryPointThread()
entryPointThread.start()
time.sleep(1)