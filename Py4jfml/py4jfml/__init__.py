import subprocess
from threading import Thread
import time
import os
import platform

#Thread to run PY4J server
class Java_EntryPointThread:
    '''
    Python class to run PY4J server.
    '''

    def __init__(self):
        upperDir = os.path.dirname(os.getcwd())
        if(platform.system()=='Linux'):
            self.process = subprocess.Popen(['java', '-jar', upperDir + '/jar_files/JFML_EntryPoint.jar'])
        if(platform.system()=='Windows'):
            self.process = subprocess.Popen(['java', '-jar', upperDir + '\jar_files\JFML_EntryPoint.jar'])

    def terminate_process(self):
        self.process.terminate()

entryPointThread = Java_EntryPointThread()
time.sleep(1)