import subprocess
from threading import Thread
import time
import os
import platform
import jar_files

name = "py4jfml"

#Thread to run PY4J server
class Java_EntryPointThread:
    '''
    Python class to run PY4J server.
    '''

    def __init__(self):
        #upperDir = os.path.dirname(os.getcwd())
        upperDir = os.path.dirname(jar_files.__file__)
        if(platform.system()=='Linux'):
            self.process = subprocess.Popen(['java', '-jar', upperDir + '/JFML_EntryPoint.jar'])
        if(platform.system()=='Windows'):
            self.process = subprocess.Popen(['java', '-jar', upperDir + '\JFML_EntryPoint.jar'])

    def terminate_process(self):
        self.process.terminate()

entryPointThread = Java_EntryPointThread()
time.sleep(1)
