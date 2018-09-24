import os
from py4j.java_gateway import JavaGateway
from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem

gateway = JavaGateway()

class Py4jfml:
    """
    Python Main class to load and write FML systems in/from files
    """
    @staticmethod
    def load(xml_fileName):
        """
        Static method to create a fuzzySystem from a xml file according to the IEEE1855 standard
        :param xml_fileName: xml file path, allowed object is String
        :return: an instance of FuzzyInferenceSystem
        """
        assert type(xml_fileName)==str
        JFML = gateway.entry_point.getJFML_Factory().createJFML()
        xml = gateway.jvm.java.io.File(str(xml_fileName))
        java_fis = JFML.load(xml)
        fuzzyInferenceSystem = FuzzyInferenceSystem(java_fis)
        return fuzzyInferenceSystem

    @staticmethod
    def writeFSTtoXML(fst, str_output):
        """"
        Static method to write a FuzzySystem in a xml file
        :param fst: allowed object is FuzzyInferenceSystem
        :param str_output: xml output file path, allowed object is String
        """
        assert type(fst) == FuzzyInferenceSystem and type(str_output) == str
        JFML = gateway.entry_point.getJFML_Factory().createJFML()
        if not os.path.isfile(str_output):
            f = open(str_output,'w+')
            f.close()
        xmlOutput = gateway.jvm.java.io.File(str(str_output))
        JFML.writeFSTtoXML(fst.java_fis, xmlOutput)

'''
    @staticmethod
    def kill():
        """
        Static method to kill every thread of Py4JFML
        """
        os._exit(0)
'''