from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4jfml.rule.FuzzyRuleType import *

class MamdaniRuleBaseType:
    """
    Definisce le regole di base Mamdani del sistema fuzzy
    """

    def __init__(self,name):
        """
        Costruttore Mamdani
        :param name: contiene il nome delle regole base Mamdani
        :param java_mrbt: contiene il collegamento con JFML
        """
        assert type(name) == str
        self.java_mrbt= gateway.entry_point.getJFMLRulebase_Factory().createMamdaniRuleBaseType(str(name))

    def addRule(self, rule):
        """
        Aggiunge una lista di regole Mamdani
        :param rule: contiene una lista di regole Mamdani
        """
        assert type(rule == FuzzyRuleType)
        self.java_mrbt.addRule(rule.java_frt)