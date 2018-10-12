import pydoc
from cli import Messages
from cli import py4jfmlcli
from command import Command
from command import State
from command.Command import Load
from command.Command import Evaluate
from command.Command import Output
from command.Command import MacroCommand
from command.Command import CommandComposer
from py4jfml.Py4Jfml import Py4jfml

pydoc.help(Command)
pydoc.help(State)
pydoc.help(py4jfmlcli)
pydoc.help(Messages)

Py4jfml.kill()