import click
import command.Command as cmd

@click.command()
@click.option('-l', '--load', default="", help=": Load xml file", multiple=True)
@click.option('-e', '--evaluate', nargs=2, help=": Evaluate", multiple=True)
@click.option('-o', '--output', default="", help=": Output")
#@click.option('-e3', '--evaluate3', nargs=3, help=": Evaluate 3", multiple=True)
#@click.option('-w', '--write', default="", help=": Write xml file")
#@click.option('-t', '--tipper', default="", help=": Tipper")
#@click.option('-m', '--mamdani', default="", help=": Mamdani Rule Base")

def startCLI(load, evaluate, output):
    '''
    Start the Command Line Interface.
    :param load: path of file xml; type allowed is String.
    :param evaluate: evaluate[0] = first value, evaluate[1] = second value; type allowed is int.
    '''
    args = {}
    if load is not "" and len(evaluate) > 0:
        #Call Load + Evaluate
        cmdCompO = cmd.CommandComposer()
        args['load'] = []
        args['evaluate'] = []
        for index, elem in enumerate(load):
            args['load'].append(elem)
            li = []
            for a in evaluate[index]:
                li.append(a)
            args['evaluate'].append(li)
        if output is not "":
            cmdCompO = cmd.CommandComposer()
            args['output'] = output
        cmdCompO.compose(args)

if __name__ == '__main__':
    startCLI()