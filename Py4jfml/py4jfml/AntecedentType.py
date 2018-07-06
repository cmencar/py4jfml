from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4jfml.ClauseType import *


class AntecedentType:
    """
    Definisce le regole antecedenti del sistema fuzzy
    """

    def __init__(self):
        """
        Costruttore AntecedentType
        :param java_at: contiene il collegamento con JFML
        """
        self.java_at = gateway.entry_point.getJFMLRule_Factory().createAntecedentType()

    def addClause(self, c):
        """
        Aggiunge una lista di clausole nelle regole Antecedenti
        :param c: lista di clausole
        """
        assert type(c) == ClauseType
        self.java_at.addClause(c.java_clauseT)