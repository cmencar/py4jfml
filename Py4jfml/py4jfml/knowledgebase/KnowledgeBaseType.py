from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4jfml.knowledgebasevariable.FuzzyVariableType import *

class KnowledgeBaseType:
    """
    Conoscenza di base del sistema fuzzy
    """
    def __init__(self):
        """
        Costruttore della conoscenza di base
        """
        self.java_kb = gateway.entry_point.getJFMLKnowledgebase_Factory().createKnowledgeBaseType()

    def addVariable(self,var):
        """
        Aggiunge la variabile alla conoscenza base
        :param var: contiene la variabile da aggiungere
        """
        assert type(var) == FuzzyVariableType
        self.java_kb.addVariable(var.java_fvt)