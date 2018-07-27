from py4j.java_collections import ListConverter
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class AnYaDataCloudType():
    '''
    Python class for anYaDataCloudType complex type.
    '''

    def __init__(self, name=None, terms=None):
        '''
        :param name:
        :param terms:
        '''
        if name==None and terms==None:
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createAnYaDataCloudType()
        elif name!=None and terms==None:
            assert type(name)==str
            self.java_kbvv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createAnYaDataCloudType(name)
        elif name!=None and terms!=None:
            assert type(name)==str and type(terms)==list
            javalist_terms = ListConverter().convert(terms, gateway._gateway_client)
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createAnYaDataCloudType(name, javalist_terms)


    # Method of class KnowledgeBaseVariable
    def isInput(self):
        '''
        Tests if the variable is input type
        :return: true if the variable is input type; false otherwise
        '''
        return self.java_kbv.isInput()


    def copy(self):
        '''
        Returns a new instance of the variable
        :return: a new instance of the variable
        '''
        return self.java_kbv.copy()

    def getName(self):
        '''
        Gets the value of the property name
        :return: possible object is String
        '''
        return self.java_kbv.getName()

    def getNetworkAddress(self):
        '''
        Gets the value of the property networkAddress
        :return: possible object is String
        '''
        return self.java_kbv.getNetworkAddress()

    def getTerm(self, name):
        '''
        Gets a Term instance by name or null otherwise
        :param name: term name
        :return: a Term instance by name or null otherwise
        '''
        assert type(name)==str
        return self.java_kbv.getTerm(name)

    def getTerms(self):
        '''
        Gets the value of the datum property
        :return: a list of terms
        '''
        return self.java_kbv.getTerms()

    def getValue(self):
        '''
        Gets the value of the variable
        :return: the value of the variable
        '''
        return self.java_kbv.getValue()

    def hasTerm(self, name):
        '''
        Returns true if the variable contains a Term with the name as param
        :param name: the name of the Term
        :return: true if the variable contains a Term with the name; false otherwise
        '''
        assert type(name) == str
        return self.java_kbv.hasTerm(name)

    def isOutput(self):
        '''
        Tests if the variable is output type
        :return: true if the variable is output type; false otherwise
        '''
        return self.java_kbv.isOutput()

    def reset(self):
        '''
        Resets the value of the variable
        '''
        return self.java_kbv.reset()

    def setName(self, value):
        '''
        Sets the value of the property name
        :param value: allowed object is string
        '''
        assert type(value) == str
        self.java_kbv.setName(value)

    def setNetworkAddress(self, value):
        '''
        Sets the value of the property networkAddress
        :param value: allowed object is string
        '''
        assert type(value) == str
        self.java_kbv.setNetworkAddress(value)

    def setTerms(self, datum):
        '''
        :param datum:
        '''
        assert type(datum)==list
        javalist_datum = ListConverter().convert(datum, gateway._gateway_client)
        self.java_kbv.setTerms(javalist_datum)

    def setValue(self, x):
        '''
        Sets the value of the variable
        :param value: allowed object is float
        '''
        assert type(x) == float
        self.java_kbv.setValue(x)

    def __str__(self):
        '''
        Returns a String object representing this variable
        :return: a String object representing this variable
        '''
        return self.java_kbv.toString()

