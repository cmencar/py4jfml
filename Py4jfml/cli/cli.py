import click
import command.Command as cmd

@click.command()
@click.option('-l', '--load', default="", help=": Load xml file")
@click.option('-e', '--evaluate', nargs=2, help=": Evaluate")
#@click.option('-w', '--write', default="", help=": Write xml file")
#@click.option('-t', '--tipper', default="", help=": Tipper")
#@click.option('-m', '--mamdani', default="", help=": Mamdani Rule Base")

def commandComposer(load, evaluate):
    if load is not "" and len(evaluate) > 0:
        macroObj = cmd.MacroCommand()
        #Method Load
        loadObj = cmd.Load()
        macroObj.add(loadObj)
        macroObj.execute(0, load)
        #Method Evaluate
        evalObj = cmd.Evaluate()
        macroObj.add(evalObj)
        macroObj.execute(1, evaluate[0], evaluate[1])
    elif load is not "":
        #Method Load
        loadObj = cmd.Load()
        macroObj = cmd.MacroCommand()
        macroObj.add(loadObj)
        macroObj.execute(0, load)

if __name__ == '__main__':
    commandComposer()