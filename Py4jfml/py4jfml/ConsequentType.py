from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4jfml.ClauseType import *

class ConsequentType:
    """
    Definisce le regole conseguenti del sistema fuzzy
    """

    def __init__(self):
        """
        Costruttore ConsequentType
        """
        self.java_ct = gateway.entry_point.getJFMLRule_Factory().createConsequentType()

    def addThenClause(self, c):
        """
        Aggiunge una lista di clausole nelle regole conseguenti
        :param c: lista di clausole
        """
        assert type(c) == ClauseType
        self.java_ct.addThenClause(c.java_clauseT)
