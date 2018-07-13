from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4jfml.rule.AntecedentType import *
from py4jfml.rule.ConsequentType import *

class FuzzyRuleType:
    """
    Definisce il tipo di regole fuzzy
    """

    def __init__(self, name=None, connector=None, connectorMethod=None, weight=0.):
        """
        Costruttore FuzzyRuleType
        :param name: contiene il nome delle regole fuzzy
        :param connector: contiene il connettore che collega le diverse clausole nella parte antecedente (e/o)
        :param connectorMethod: contiene l'algoritmo da utilizzare se il connettore scelto è e od o.
        :param weight: contiene il peso della regola da utilizzare
        :param java_frt contiene il collegamento con JFML
        """
        if name==None:
            self.java_frt = gateway.entry_point.getJFMLRule_Factory().createFuzzyRuleType()
        else:
            assert type(name) == str and type(connector) == str and type(connectorMethod) == str and type(weight) == float
            self.java_frt= gateway.entry_point.getJFMLRule_Factory().createFuzzyRuleType(str(name), str(connector), str(connectorMethod), float(weight))

    def setAntecedent(self, value):
        """
        Imposta il valore antecedente alle regole
        :param value: contiene il valore antecedente alle regole
        """
        assert  type(value) == AntecedentType
        self.java_frt.setAntecedent(value.java_at)

    def setConsequent(self, value):
        """
        Imposta il valore conseguente alle regole
        :param value: contiene il valore conseguente alle regole
        """
        assert type(value) == ConsequentType
        self.java_frt.setConsequent(value.java_ct)