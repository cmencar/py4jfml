import py4jfml.Py4Jfml as fml
from py4jfml.FuzzyInferenceSystem import *
import command.State as st

class Command:
    '''
    Command class.
    :param state: Create State object (Singleton).
    '''
    state = st.State()
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
        import os.path
        try:
            os.stat(args)
        except os.error:
            print('File xml not found')
            import sys
            sys.exit()

        #Load file xml and get FIS
        fis = fml.Py4jfml.load(args)
        #Save the name of file xml
        from pathlib import Path
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
        :param args: values; type allowed is List.
        '''
        assert type(args) == list
        #Get fis in state fields
        fis = self.state.fields['fis']
        food = fis.getVariable('food')
        service = fis.getVariable('service')

        for elem in args:
            try:
                if len(elem) is not 2:
                    raise ValueError()
            except:
                print('Wrong number of arguments')
                import sys
                sys.exit()
            #Parse fargs[0] into Float
            argFood = float(elem[0])
            food.setValue(argFood)
            #Parse fargs[1] into Float
            argService = float(elem[1])
            service.setValue(argService)
            #Call method evaluate()
            fis.evaluate()
            #Create tipper
            tip = fis.getVariable('tip')
            #Get tipper value
            value = tip.getValue()
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
        import csv
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
        :param args: args[0] = name of command, args[1] = arguments; type allowed is List.
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
        if 'load' in ops:
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
                    import csv
                    try:
                        #Read file csv
                        with open(args['evaluate'], 'r') as csvfile:
                            reader = csv.reader(csvfile)
                            for index, row in enumerate(reader):
                                app = []
                                for elem in row:
                                    app.append(elem)
                                fargs.append(app)
                    except FileNotFoundError:
                        print('File csv not found')
                        import sys
                        sys.exit()
                #Evaluate using values
                else:
                    fargs.append(args['evaluates'].split(','))
                #Add arguments of command Evaluate
                lis.append(fargs)
                #Check if there is Output after Evaluate
                if 'output' in ops:
                    #Create Output object
                    outObj = Output()
                    #Add Output command
                    cmdo.add(outObj)
                    #Add arguments of command Output
                    lis.append(args['output'])
            #Execute commands
            cmdo.execute(lis)
            #If no command output, return the results
            if 'output' not in ops:
                #Return results
                return cmdo.children[0].state.fields['results']