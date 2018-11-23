# Py4JFML
A python library for using JFML


To use this library in UNIX-based systems you need to follow this steps.
  
  
  1. If you don't have setuptools installed on your machine, you have to run:
  
    $ sudo apt-get install python3-setuptools
  
  
  2. Then, after downloading Py4jfml, you need to install the library locally.  
  Navigate to the directory '../py4jfml-master/Py4jfml' and run:
  
  	$ pip install .
  
  
  3. Finally, you need to run setup.py to update PYTHONPATHs and dependencies in python3.  
  You should do this every time you edit file setup.py:
  
  	$ sudo python3 setup.py develop
  

Now you are ready to use Py4jfml library.


  If you want to try the library, you can run one of the test files available in testlib directory:
    
    $ python3 testfilename.py
