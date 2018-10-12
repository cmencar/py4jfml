import sys as s
import click
import command.Command as cmd
import cli.Messages as msg
from py4jfml.Py4Jfml import Py4jfml

@click.command()
@click.option('-l', '--load', default='', help='Load a file xml.')
@click.option('-e', '--evaluate', default='', help='Evaluate using a file csv.')
@click.option('-i', '--evaluates', default='', help='Evaluate using values.')
@click.option('-o', '--output', default='', help='Output a file csv.')

def startCLI(load, evaluate, evaluates, output):
    args = {}
    try:
        if load is not '' and evaluate is '' and evaluates is '':
            Py4jfml.kill()
            s.exit(msg.getMsg('OnlyLoad'))
        #Check for Load
        elif load is not '':
            cmdCompO = cmd.CommandComposer()
            #Add Load arguments to execute
            args['load'] = load
            load = ''
            #flag becomes True if Evaluate or Evaluates isn't ''
            flag = False
            #Check for Evaluate using a file csv
            if evaluate is not '':
                #Load + Evaluate
                #Add Evaluate arguments to execute
                args['evaluate'] = evaluate
                flag = True
            #Check for Evaluate using values
            elif evaluates is not '':
                #Load + Evaluates
                #Add Evaluate arguments to execute
                args['evaluates'] = evaluates
                flag = True
            if flag:
                #Check for Output
                if output is not '':
                    #Load + (Evaluate OR Evaluates) + Output
                    cmdCompO = cmd.CommandComposer()
                    #Add Output arguments to execute 
                    args['output'] = output
                    output = ''
                    #Compose commands
                    cmdCompO.compose(args)
                elif evaluate is not '' or evaluates is not '':
                    evaluate = ''
                    evaluates = ''
                    #Load + (Evaluate OR Evaluates)
                    #Compose commands
                    app = cmdCompO.compose(args)
                    #Print results
                    for index, elem in enumerate(app):
                        res = str(elem)
                        s.stdout.write(res + '\n')
            Py4jfml.kill()
        else:
            Py4jfml.kill()
            s.exit(msg.getMsg('NoOption'))
    except IndexError:
        Py4jfml.kill()
        s.exit(msg.getMsg('IndexError'))
    except ValueError:
        Py4jfml.kill()
        s.exit(msg.getMsg('ValueError'))
    except FileNotFoundError:
        Py4jfml.kill()
        s.exit(msg.getMsg('FileNotFoundError'))
    except IOError:
        Py4jfml.kill()
        s.exit(msg.getMsg('IOError'))
    except NameError:
        Py4jfml.kill()
        s.exit(msg.getMsg('NameError'))

if __name__ == '__main__':
    startCLI()