from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4jfml.FuzzyTermType import *

class FuzzyVariableType:
    """
    Definisce i tipi di variabile fuzzy
    """

    def __init__(self,name=None,domainLeft=None,domainRight=None):
        """
        Costruttori dei tipi di variabile fuzzy
        :param name: nome della regola
        :param domainLeft: dominio sinistro
        :param domainRight: dominio destro
        :param java_fvt: contiene il collegamento con JFML
        """
        if(name==None):
            self.java_fvt = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createFuzzyVariableType()
        elif(type(name) == str and type(domainRight)== float and type(domainLeft)==float):
            assert type(name) == str and type(domainRight)== float and type(domainLeft)==float
            self.java_fvt = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createFuzzyVariableType(str(name),float(domainLeft) ,float(domainRight))
        else:
            self.java_fvt = name

    def addFuzzyTerm(self, ft):
        """
        Aggiunge la regola al sistema fuzzy
        :param ft: regola fuzzy
        """
        assert  type(ft) == FuzzyTermType
        self.java_fvt.addFuzzyTerm(ft.java_ftt)

    def setValue(self, x):
        """
        Imposta il valore alle regole fuzzy
        :param x: contiene il valore
        """
        assert type(x) == float
        self.java_fvt.setValue(float(x))

    def getValue(self):
        """
        Ottiene il valore delle regole fuzzy
        :return: restituisce il valore
        """
        return self.java_fvt.getValue()

    def getName(self):
        """
        Ottiene il nome delle regole fuzzy
        :return: restituisce il nome delle regole fuzzy
        """
        return self.java_fvt.getName()

    def setDefaultValue(self, value):
        """
        Imposta i valori di default
        :param value: valore di default
        """
        assert type(value) == float
        self.java_fvt.setDefaultValue(float(value))

    def setAccumulation(self, value):
        """
        Imposta il valore di accumulazione
        :param value: valore di accumulazione
        :return: restituisce il valore di accumulazione
        """
        assert type(value) == str
        self.java_fvt.setAccumulation(str(value))

    def setDefuzzifierName(self, value):
        """
        Imposta il nome del defuzzifier
        :param value: nome deffuzifier
        :return: restituisce il nome
        """
        assert type(value) == str
        self.java_fvt.setDefuzzifierName(str(value))

    def setType(self, value):
        """
        Imposta il tipo delle regole fuzzy
        :param value: tipo
        """
        assert  type(value) == str
        self.java_fvt.setType(str(value))
