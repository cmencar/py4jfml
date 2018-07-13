from py4j.java_gateway import JavaGateway
from py4j.java_collections import ListConverter
gateway = JavaGateway()

class FuzzyTermType:
    """
    Definisce i termini del sistema fuzzy
    """

    def __init__(self, name, type_java, param):
        """
        Costruttore FuzzyTermType
        :param name: contiene il nome dei termini
        :param type_java: contiene i tipi descritti nella classe FuzzyTerm
        :param param: è un array di numeri float che indicano i parametri dei grafici
        :param java_ftt: contiene il collegamento con JFML
        """
        assert type(name) == str and type(type_java) == int and type(param) == list
        java_list = ListConverter().convert(param, gateway._gateway_client)
        self.java_ftt = gateway.entry_point.getJFMLTerm_Factory().createFuzzyTermType(str(name), int(type_java), java_list)

    def setComplement(self, value):
        """
        Imposta i valori dei complementi
        :param value: contiene il complemento
        """
        assert type(value) == str
        self.java_ftt.setComplement(str(value))