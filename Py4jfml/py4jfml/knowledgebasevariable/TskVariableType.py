from py4j.java_gateway import JavaGateway

from py4jfml.knowledgebasevariable import AggregatedFuzzyVariableType, FuzzyVariableType

gateway = JavaGateway()

class TskVariableType:
    '''
    Python class for tskVariableType complex type
    '''

    def __init__(self, name=None):
        '''
        :param name:
        '''
        if name==None:
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createTskVariableType()
        else:
            assert type(name)==str
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createTskVariableType(name)


    # Method of class KnowledgeBaseVariable
    def isInput(self):
        '''
        Tests if the variable is input type
        :return: true if the variable is input type; false otherwise
        '''
        return self.java_kbv.isInput()


    def addEvaluation(self, wi, zi):
        '''
        Adds an evaluation
        :param wi: value w
        :param zi: value z
        '''
        assert type(wi)==float and type(zi)==float
        self.java_kbv.addEvaluation(wi, zi)

    def addInputVariable(self, fv):
        '''
        Adds an input variable
        :param fv: fuzzy variable to add
        '''
        assert type(fv)==AggregatedFuzzyVariableType or type(fv)==FuzzyVariableType
        self.java_kbv.addInputVariable(fv.java_kbv)

    def addTskTerm(self, name, order, coeff):
        '''
        Adds a tsk term
        :param name:
        :param order:
        :param coeff:
        '''
        assert type(name)==str and type(order)==int and type(coeff)==list
        self.java_kbv.addTskTerm(name, order, coeff)

    def copy(self):
        '''
        Returns a new instance of the variable
        :return: a new instance of the variable
        '''
        return self.java_kbv.copy()

    def getCombination(self):
        '''
        Gets the value of the property combination
        :return: possible object is String
        '''
        return self.java_kbv.getCombination()

    def getDefaultValue(self):
        '''
        Gets the value of the property defaultValue
        :return: possible object is Float
        '''
        return self.java_kbv.getDefaultValue()

    def getInputVariables(self):
        '''
        :return: a list of fuzzy variables
        '''
        return self.java_kbv.getInputVariables()

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

    def getScale(self):
        '''
        Gets the value of the property scale
        :return: possible object is String
        '''
        return self.java_kbv.getScale()

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
        Gets the value of the tsukamotoTerm property
        :return: a list of terms
        '''
        return self.java_kbv.getTerms()

    def getType(self):
        '''
        Gets the value of the property type
        :return: possible object is String
        '''
        return self.java_kbv.getType()

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
        assert type(name)==str
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

    def setCombination(self, value):
        '''
        Sets the value of the property combination
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_kbv.setCombination(value)

    def setDefaultValue(self, value):
        '''
        Sets the value of the property defaultValue
        :param value: allowed object is Float
        '''
        assert type(value)==float
        self.java_kbv.setDefaultValue(value)

    def setInputVariables(self, kbvs):
        '''
        :param kbvs: a list of Knowledge base variables
        '''
        assert type(kbvs)==list
        self.java_kbv.setInputVariables(kbvs)

    def setName(self, value):
        '''
        Sets the value of the property name
        :param value: allowed object is string
        '''
        assert type(value)==str
        self.java_kbv.setName(value)

    def setNetworkAddress(self, value):
        '''
        Sets the value of the property networkAddress
        :param value: allowed object is string
        '''
        assert type(value)==str
        self.java_kbv.setNetworkAddress(value)

    def setScale(self, value):
        '''
        Sets the value of the property scale
        :param value: allowed object is string
        '''
        assert type(value)==str
        self.java_kbv.setScale(value)

    def setType(self, value):
        '''
        Sets the value of the property type
        :param value: allowed object is string
        '''
        assert type(value)==str
        self.java_kbv.setType(value)

    def setValue(self, x):
        '''
        Sets the value of the variable
        :param value: allowed object is float
        '''
        assert type(x)==float
        self.java_kbv.setValue(x)

    def __str__(self):
        '''
        Returns a String object representing this variable
        :return: a String object representing this variable
        '''
        return self.java_kbv.toString()