from py4j.java_gateway import JavaGateway

from py4jfml.knowledgebasevariable.AggregatedFuzzyVariableType import AggregatedFuzzyVariableType
from py4jfml.knowledgebasevariable.AnYaDataCloudType import AnYaDataCloudType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.knowledgebasevariable.TskVariableType import TskVariableType
from py4jfml.knowledgebasevariable.TsukamotoVariableType import TsukamotoVariableType

gateway = JavaGateway()


class KnowledgeBaseType:
    '''
    Python class for knowledgeBaseType complex type
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.java_kbt = gateway.entry_point.getJFMLKnowledgebase_Factory().createKnowledgeBaseType()

    def addVariable(self, var):
        '''
        Adds a variable to the list of varibles
        :param var: the variable to add
        '''
        assert type(var)==AnYaDataCloudType or type(var)==AggregatedFuzzyVariableType or type(var)==FuzzyVariableType or type(var)==TskVariableType or type(var)==TsukamotoVariableType
        self.java_kbt.addVariable(var.java_kbv)


    def getKnowledgeBaseVariables(self):
        '''
        :return: List of KnowledgeBaseVariable
        '''
        return self.java_kbt.getKnowledgeBaseVariables()

    def getNetworkAddress(self):
        '''
        Gets the value of the networkAddress property
        :return: possible object is String
        '''
        return self.java_kbt.getNetworkAddress()

    def getVariable(self, name):
        '''
        Return a KnowledgeBaseVariable instance identifies by its name
        :param name: the name of the variable
        :return: the KnowledgeBaseVariable or null if the param name no match
        '''
        assert type(name)==str
        return self.java_kbt.getVariable()

    def getVariables(self):
        '''
        Gets the value of the Variable property
        :return: a list of Objects
        '''
        return self.java_kbt.getVariables()

    def setNetworkAddress(self, value):
        '''
        Sets the value of the networkAddress property
        :param value: value of the network address,  allowed object is String
        '''
        assert type(value)==str
        self.java_kbt.setNetworkAddress(value)

    def __str__(self):
        '''
        Returns a String object representing this object
        :return: allowed object is String
        '''
        return self.java_kbt.toString()
