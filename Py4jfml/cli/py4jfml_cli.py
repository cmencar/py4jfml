import click
import command.Command as cmd

@click.command()
@click.option('-l', '--load', default="", help="Load a file xml")
@click.option('-e', '--evaluate', default="", help="Evaluate using a file csv")
@click.option('-i', '--evaluates', default="", help="Evaluate using values")
@click.option('-o', '--output', default="", help="Output a file csv")

def startCLI(load, evaluate, evaluates, output):
    '''
    Command Line Interface Help\n
    '''
    args = {}
    #Check for Load
    if load is not "":
        cmdCompO = cmd.CommandComposer()
        #Add Load arguments to execute
        args['load'] = load
        #Check for Evaluate using a file csv
        if evaluate is not "":
            #Load + Evaluate
            #Add Evaluate arguments to execute
            args['evaluate'] = evaluate
        #Check for Evaluate using values
        elif evaluates is not "":
            #Load + Evaluates
            #Add Evaluate arguments to execute
            args['evaluates'] = evaluates
            #Check for Output
        if output is not "":
            #Load + (Evaluate OR Evaluates) + Output
            cmdCompO = cmd.CommandComposer()
                #Add Output arguments to execute 
            args['output'] = output
                #Compose commands
            cmdCompO.compose(args)
        elif evaluate is not "" or evaluates is not "":
            #Load + (Evaluate OR Evaluates)
            #Compose commands
            app = cmdCompO.compose(args)
            import sys
                #Print results
            for index, elem in enumerate(app):
                res = str(elem)
                sys.stdout.write(res + '\n')
        else:
            #Load
            #Compose commands
            cmdCompO.compose(args)

if __name__ == '__main__':
    startCLI()
