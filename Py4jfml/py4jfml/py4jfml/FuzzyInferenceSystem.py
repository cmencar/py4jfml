from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4jfml.knowledgebase.KnowledgeBaseType import *
from py4jfml.rulebase.MamdaniRuleBaseType import *
from py4jfml.knowledgebasevariable.FuzzyVariableType import *

class FuzzyInferenceSystem:
    """
    La classe FuzzyInferenceSystem crea il sistema fuzzy
    """

    def __init__(self,name=None):
        """
        Costruttori del FuzzyInferenceSystem
        :param name: nome del sistema fuzzy
        :param java_fis: colleggamento alla JFML
        """
        if name==None:
            self.java_fis = gateway.entry_point.getJFML_Factory().createFuzzyInferenceSystem()
        elif type(name) == str:
            assert type(name) == str
            self.java_fis = gateway.entry_point.getJFML_Factory().createFuzzyInferenceSystem(str(name))
        elif(type(name)== FuzzyInferenceSystem):
            self.java_fis = name.fuzzyInferenceSystem
        else:
            self.java_fis = name

    def setKnowledgeBase(self, value):
        """
        Imposta il valore della conoscenza di base
        :param value: variabile contenete il valore
        """
        assert type(value) == KnowledgeBaseType
        self.java_fis.setKnowledgeBase(value.java_kb)

    def addRuleBase(self,r):
        """
        Aggiunge le regole base
        :param r: variabile contenete la regola
        """
        assert type(r) == MamdaniRuleBaseType
        self.java_fis.addRuleBase(r.java_mrbt)

    def getVariable(self,name):
        """
        Ottiene il nome della variabile
        :param name: contiene il nome della variabile
        """
        assert type(name) == str
        return FuzzyVariableType(self.java_fis.getVariable(str(name)))

    def evaluate(self):
        """
        Valuta il sistema fuzzy
        """
        self.java_fis.evaluate()

    def __str__(self):
        """
        Stampa su console il sistema fuzzy
        """
        return self.java_fis.toString()