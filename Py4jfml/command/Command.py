import py4jfml.Py4Jfml as fml
from py4jfml.FuzzyInferenceSystem import *
import command.State as st

class Command(object):
    _sto = None
    def execute(self):
         pass

class Load(Command):
    _sto = st.Singleton()

    def execute(self, str):
        fis = fml.Py4jfml.load(str)
        self._sto.setStrXml(fis)

#Da implementare
class Write(Command):
    _sto = st.Singleton()

    def execute(self, str):
        pass

class Evaluate(Command):
    _sto = st.Singleton()

    def execute(self, value1, value2):
        fis = self._sto.getStrXml()
        #Set input values
        food = fis.getVariable("food")
        service = fis.getVariable("service")
        #Parse value1 into Float
        fvalue1 = float(value1)
        food.setValue(fvalue1)
        #Parse value2 into Float
        fvalue2 = float(value2)
        service.setValue(fvalue2)
        #Call method evaluate()
        fis.evaluate()
        results = []
        tip = fis.getVariable("tip")
        name = tip.getName()
        value = tip.getValue()
        results.append(name)
        results.append(value)
        #Print results
        print(results[0], " = ", results[1])

#Composite
class MacroCommand(Command):
    """
    Define behavior for components having children.
    Store child components.
    Implement child-related operations in the Command class.
    """
    _children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, index):
        self._children.remove(index)

    def execute(self, index, *args):
        self._children[index].execute(*args)