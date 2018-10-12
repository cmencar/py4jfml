import os as path
import csv
import py4jfml.Py4Jfml as fml
import command.State as st
from pathlib import Path

class Command:
    '''
    Command class.
    :param state: Create State object (Singleton).
    '''
    state = st.State()
    def execute(self, args):
        '''
        Demands the execute of commands to the child commands.
        :param args: arguments.
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
        filename = Path(args).name
        self.state.fields['filename'] = filename
        #Save FIS file
        self.state.fields['fis'] = fis

class Evaluate(Command):
    '''
    Evaluate class.
    '''
    def execute(self, args):
        '''
        Execute the command Evaluate.
        :param args: values to evaluate; type allowed is List.
        '''
        assert type(args) == list
        #Get fis in state fields
        fis = self.state.fields['fis']

        #Get names of input variables
        names = []
        for e in fis.getVariables():
            name = e.getName()
            names.append(name)
        #Save name of result variable
        resultName = names[-1]
        #Pop last element because is not an input variable
        names.pop()

        vars = []

        #Get variables 
        for i, e in enumerate(names):
            #Convert the name into String
            nameStr=str(e)
            app = fis.getVariable(nameStr)
            vars.append(app)

        for elem in args:
            for i,e in enumerate(vars):
                #Remove whitespace
                nospace = elem[i].replace(' ','')
                #Parse nospace into Float if it is int or float otherwise raise exception
                elemFloat = float(nospace)
                e.setValue(elemFloat)
            #Check if numbers of value is different from input needed
            if len(names) is not len(elem):
                raise IndexError()
            #Call method evaluate()
            fis.evaluate()
            #Create result
            result = fis.getVariable(resultName)
            #Get result
            value = result.getValue()
            #Save results
            if 'results' in self.state.fields:
                self.state.fields['results'].append(value)
            else:
                self.state.fields['results'] = [value]

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
        #Write file csv
        with open(args, 'w') as csvfile:
            writer = csv.writer(csvfile)
            ad = []
            for e in self.state.fields['results']:
                s = str(e)
                ad.append(s)
            writer.writerow(ad)

#Composite
class MacroCommand(Command):
    '''
    MacroCommand class.
    Define behavior for components having children.
    Store child components.
    Implement child-related operations in the Command class.
    :param children: Initialize child commands.
    '''
    children = []

    def add(self, component):
        '''
        Add a command to the self.children.
        :param component: constructor of command; types allowed are children of Command class.
        '''
        assert type(component) == Load or type(component) == Evaluate or type(component) == Output
        #Add component in child list
        self.children.append(component)

    def execute(self, args):
        '''
        Execute a command by self.children.
        :param args: arguments of commands; type allowed is List.
        '''
        assert type(args) == list
        for index, child in enumerate(self.children):
            child.execute(args[index])

class CommandComposer():
    '''
    CommandComposer class.
    :param _ops: Initialize commands.
    '''
    def compose(self, args):
        '''
        Create and execute command using MacroCommand class.
        :param args: args['name of command'] = arguments; type allowed is Dictionary.
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
        if 'load' in ops:
            #Check file extension
            ext = args['load'][-4:]
            if ext != '.xml':
                raise NameError()
            #Check if file exist
            path.stat(args['load'])
            #Check if file is empty
            if path.stat(args['load']).st_size == 0:
                raise IOError()
            #Create Load object
            loadObj = Load()
            #Add Load command 
            cmdo.add(loadObj)
            #Add arguments of command Load
            lis.append(args['load'])
            #Check if there is Evaluate after Load
            if 'evaluate' in ops or 'evaluates' in ops:
                #Create Evaluate object
                evalObj = Evaluate()
                #Add Evaluate command
                cmdo.add(evalObj)
                #Add arguments of command Evaluate
                fargs = []
                #Evaluate using a file csv
                if 'evaluate' in ops:
                    #Check file extension
                    ext = args['evaluate'][-4:]
                    if ext != '.csv':
                        raise NameError()
                    #Check if file exist
                    path.stat(args['evaluate'])
                    #Check if file is empty
                    if path.stat(args['evaluate']).st_size == 0:
                        raise IOError()
                    #Read file csv
                    with open(args['evaluate'], 'r') as csvfile:
                        reader = csv.reader(csvfile)
                        for index, row in enumerate(reader):
                            app = []
                            for elem in row:
                                app.append(elem)
                            fargs.append(app)
                #Evaluate using values
                else:
                    fargs.append(args['evaluates'].split(','))
                #Add arguments of command Evaluate
                lis.append(fargs)
                #Check if there is Output after Evaluate
                if 'output' in ops:
                    #Check file extension
                    ext = args['output'][-4:]
                    if ext != '.csv':
                        raise NameError()
                    #Create Output object
                    outObj = Output()
                    #Add Output command
                    cmdo.add(outObj)
                    #Add arguments of command Output
                    lis.append(args['output'])
            #Execute commands
            cmdo.execute(lis)
            #If no command output, return the results
            if ('evaluate' in ops or 'evaluates' in ops) and 'output' not in ops:
                #Return results
                return cmdo.children[0].state.fields['results']