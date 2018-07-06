from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4jfml.FuzzyInferenceSystem import *

class Py4jfml:
    """
    La classe Py4jfml permette di caricare o scirvere un file xml contenente un sistema fuzzy
    """

    @staticmethod
    def load(xml_fileName):
        """
        il metodo load permette di caricare un file xml
        :param xml_fileName: contiene il percorso del file
        :param JFML: crea una istanza vuota della classe scritta in java
        :param xml: contiene il file xml
        :param java_fis: è la variabile che si collega alla libreria JFML
        :param fuzzyInferenceSystem: è la variabile che contiene il file appena caricato
        :return: fuzzyInferenceSystem
        """
        assert type(xml_fileName) == str
        JFML = gateway.entry_point.getJFML_Factory().createJFML()
        xml = gateway.jvm.java.io.File(str(xml_fileName))
        java_fis = JFML.load(xml)
        fuzzyInferenceSystem = FuzzyInferenceSystem(java_fis)
        return fuzzyInferenceSystem

    @staticmethod
    def writeFSTtoXML(fst, str_output):
        """"
        il metodo writeFSTtoXML permette di scrivere un file xml
        :param fst: contiene il sistema fuzzy
        :param str_output: contiene il percorso del file
        :param JFML: crea una istanza vuota della classe scritta in java
        :param xmlOutput: contiene il file xml
        :return: JFML.writeFSTtoXML(fst.java_fis, xmlOutput)
                """
        assert type(fst) == FuzzyInferenceSystem and type(str_output) == str
        JFML = gateway.entry_point.getJFML_Factory().createJFML()
        xmlOutput = gateway.jvm.java.io.File(str(str_output))
        return JFML.writeFSTtoXML(fst.java_fis, xmlOutput)