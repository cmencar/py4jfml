import click
import command.Command as cmd

@click.command()
@click.option('-l', '--load', default="", help=": Load xml file")
@click.option('-e', '--evaluate', nargs=2, help=": Evaluate")
#@click.option('-w', '--write', default="", help=": Write xml file")
#@click.option('-t', '--tipper', default="", help=": Tipper")
#@click.option('-m', '--mamdani', default="", help=": Mamdani Rule Base")

def startCLI(load, evaluate):
    '''
    Start the Command Line Interface.
    :param load: path of file xml; type allowed is String.
    :param evaluate: evaluate[0] = first value, evaluate[1] = second value; type allowed is int.
    '''
    if load is not "" and len(evaluate) > 0:
        #Call Load + Evaluate
        cmdCompO = cmd.CommandComposer()
        args = {'load':load, 'evaluate':[evaluate[0],evaluate[1]]}
        cmdCompO.callMacro(args)
    elif load is not "":
        #Call Load
        cmdCompO = cmd.CommandComposer()
        args = {'load':load}
        cmdCompO.callMacro(args)

if __name__ == '__main__':
    startCLI()