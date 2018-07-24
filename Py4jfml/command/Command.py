import py4jfml.Py4Jfml as fml
from py4jfml.FuzzyInferenceSystem import *
import command.State as st

class Command:
    '''
    Command class.
    :param _state: Initialize State.
    '''
    _state = None
    def execute(self, args):
        '''
        Demands the execute of commands to the child commands.
        :param args: argumnets; typr allowed is List.
        '''
        pass

class Load(Command):
    '''
    Load class.
    :param _state: Create State object (Singleton).
    '''
    _state = st.State()

    def execute(self, args):
        '''
        Execute the command Load.
        :param args: path of file xml; type allowed is String.
        '''
        assert type(args) == str
        #Load file xml and get FIS
        fis = fml.Py4jfml.load(args)
        #Save path of file xml
        self._state.fields['filename'] = args
        #Save FIS file
        self._state.fields['fis'] = fis

#To do
class Write(Command):
    '''
    Write class.
    :param _state: Create State object (Singleton).
    '''
    _state = st.State()

    def execute(self, args):
        assert type(args) == list
        pass

class Evaluate(Command):
    '''
    Evaluate class.
    :param _state: Create State object (Singleton).
    '''
    _state = st.State()

    def execute(self, args):
        '''
        Execute the command Evaluate.
        :param args: args[0] = first value, args[1] = second value; type allowed is List.
        '''
        assert type(args) == list
        #Get fis in state fields
        fis = self._state.fields['fis']
        food = fis.getVariable('food')
        service = fis.getVariable('service')
        #Parse args[0] into Float
        farg0 = float(args[0])
        food.setValue(farg0)
        #Parse args[1] into Float
        farg1 = float(args[1])
        service.setValue(farg1)
        #Call method evaluate()
        fis.evaluate()
        #Create tipper
        tip = fis.getVariable('tip')
        #Get tipper name
        name = tip.getName()
        #Get tipper value
        value = tip.getValue()
        #Print results
        print(name, ' = ', value)

#Composite
class MacroCommand(Command):
    '''
    MacroCommand class.
    Define behavior for components having children.
    Store child components.
    Implement child-related operations in the Command class.
    :param _children: Initialize child commands.
    '''
    _children = {}

    def add(self, key, component):
        '''
        Add a command to the self._children.
        :param key: name of command; type allowed is String.
        :param component: constructor of command; types allowed are children of Command class.
        '''
        assert type(key) == str
        assert type(component) == Load or type(component) == Evaluate
        self._children[key] = component

    def remove(self, key):
        '''
        Remove a command by name.
        :param key: name of command; type allowed is String.
        '''
        assert type(key) == str
        self._children.pop(key, None)

    def execute(self, args):
        '''
        Execute a command by self._children.
        :param args: args[0] = name of command, args[1] = arguments; type allowed is List.
        '''
        assert type(args) == list
        self._children[args[0]].execute(args[1])

class CommandComposer():
    '''
    CommandComposer class.
    :param _ops: Initialize commands.
    '''
    _ops = {'load':False, 'evaluate':False}
    def callMacro(self, args):
        '''
        Create and execute command using MacroCommand class.
        :param args: args[0] = name of command, args[1] = arguments; type allowed is Dictionary.
        '''
        assert type(args) == dict
        #Create MacroCommand object
        cmdo = MacroCommand()
        #Check and active commands
        for i in self._ops:
            for y in args:
                if i == y:
                    self._ops[y] = True;
        #Check if there is Load
        if self._ops['load']:
            #Create Load object
            loadObj = Load()
            #Add Load command 
            cmdo.add('load', loadObj)
            lis = ['load', args['load']]
            #Execute Load command 
            cmdo.execute(lis)
            #Check if there is Evaluate after Load
            if self._ops['evaluate']:
                #Create Evaluate object
                evalObj = Evaluate()
                #Add Evaluate command
                cmdo.add('evaluate', evalObj)
                lis = ['evaluate', args['evaluate']]
                #Execute Evaluate command 
                cmdo.execute(lis)