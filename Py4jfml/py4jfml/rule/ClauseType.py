from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4jfml.knowledgebasevariable.FuzzyVariableType import *
from py4jfml.term.FuzzyTermType import *

class ClauseType:
    """
    Definisce le clausole di un sistema fuzzy
    """

    def __init__(self, variable, term, modifier=None):
        """
        Costruttore ClauseType
        :param variable: contiene un oggetto KnowledgeBaseVariable
        :param term: contiene un oggetto FuzzyTerm
        :param modifier: contiene il modificatore di una stringa secondo lo StandardModifierType
        :param java_ct: contiene il collegamento con JFML
        """
        if modifier == None:
            assert type(variable) == FuzzyVariableType and type(term) == FuzzyTermType
            self.java_clauseT = gateway.entry_point.getJFMLRule_Factory().createClauseType(variable.java_fvt, term.java_ftt)
        else:
            assert type(variable) == FuzzyVariableType and type(term) == FuzzyTermType and type(modifier) == str
            self.java_clauseT = gateway.entry_point.getJFMLRule_Factory().createClauseType(variable.java_fvt, term.java_ftt, modifier)