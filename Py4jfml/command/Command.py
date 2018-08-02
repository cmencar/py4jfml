import py4jfml.Py4Jfml as fml
from py4jfml.FuzzyInferenceSystem import *
import command.State as st

class Command:
    '''
    Command class.
    :param _state: Create State object (Singleton).
    '''
    _state = st.State()
    def execute(self, args):
        '''
        Demands the execute of commands to the child commands.
        :param args: argumnets; typr allowed is List.
        '''
        pass

class Load(Command):
    '''
    Load class.
    '''
    def execute(self, args):
        '''
        Execute the command Load.
        :param args: path of file xml; type allowed is String.
        '''
        assert type(args) == str
        #Load file xml and get FIS
        fis = fml.Py4jfml.load(args)
        #Save the name of file xml
        from pathlib import Path
        filename = Path(args).name
        self._state.fields['filename'] = filename
        #Save FIS file
        self._state.fields['fis'] = fis

#To do
class Write(Command):
    '''
    Write class.
    '''
    def execute(self, args):
        assert type(args) == list
        pass

class Evaluate(Command):
    '''
    Evaluate class.
    '''
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
        #Save name
        if 'names' in self._state.fields:
            self._state.fields['names'].append(name)
        else:
            self._state.fields['names'] = [name]
        #Save results
        if 'results' in self._state.fields:
            self._state.fields['results'].append(value)
        else:
            self._state.fields['results'] = [value]

class Output(Command):
    '''
    Output class.
    '''
    def execute(self, args):
        '''
        Execute the command Output.
        :param args: path of file csv; type allowed is String.
        '''
        assert type(args) == str
        import csv
        with open(args, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for e in self._state.fields['results']:
                s = str(e)
                writer.writerow(s)


#Composite
class MacroCommand(Command):
    '''
    MacroCommand class.
    Define behavior for components having children.
    Store child components.
    Implement child-related operations in the Command class.
    :param _children: Initialize child commands.
    '''
    _children = []

    def add(self, component):
        '''
        Add a command to the self._children.
        :param component: constructor of command; types allowed are children of Command class.
        '''
        assert type(component) == Load or type(component) == Evaluate or type(component) == Output
        #Append component in child list
        self._children.append(component)

    def execute(self, args):
        '''
        Execute a command by self._children.
        :param args: args[0] = name of command, args[1] = arguments; type allowed is List.
        '''
        assert type(args) == list
        for index, child in enumerate(self._children):
            child.execute(args[index])

class CommandComposer():
    '''
    CommandComposer class.
    :param _ops: Initialize commands.
    '''
    def compose(self, args):
        '''
        Create and execute command using MacroCommand class.
        :param args: args[0] = name of command, args[1] = arguments; type allowed is Dictionary.
        '''
        assert type(args) == dict
        #Create MacroCommand object
        cmdo = MacroCommand()
        #Create a list of arguments
        lis = []
        #Create a dictionary that contain each operations in args with True as default value
        ops = {}
        for op in args:
            ops[op] = True;
        #Check if there is Load
        if ops['load']:
            for index, elem in enumerate(args['load']):
                #Create Load object
                loadObj = Load()
                #Add Load command 
                cmdo.add(loadObj)
                #Add arguments of command Load
                lis.append(elem)
                #Check if there is Evaluate after Load
                if ops['evaluate']:
                    #Create Evaluate object
                    evalObj = Evaluate()
                    #Add Evaluate command
                    cmdo.add(evalObj)
                    #Add arguments of command Evaluate
                    lis.append(args['evaluate'][index])
                    if ops['output']:
                        outObj = Output()
                        cmdo.add(outObj)
                        lis.append(args['output'])
            #Execute commands
            cmdo.execute(lis)