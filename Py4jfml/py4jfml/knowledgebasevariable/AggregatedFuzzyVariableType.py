from py4jfml.term.AggregatedFuzzyTermType import *
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()



class AggregatedFuzzyVariableType:
    '''
    Python class for aggregatedFuzzyVariableType complex type.
    Represents an input fuzzy variable that can be used to aggregate two or more fuzzy variables related to a given FLS
    '''

    def __init__(self, name=None, fuzzyVarType=None):
        '''
        :param name: is used to define a unique name for the aggregated fuzzy variable
        :param fuzzyVarType: is used to define the position of the aggregated fuzzy variable into rule (consequent part or antecedent part). Output or input
        '''
        if name==None and fuzzyVarType==None:
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createAggregatedFuzzyVariableType()
        elif name!=None and fuzzyVarType==None:
            assert type(name)==str
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createAggregatedFuzzyVariableType(name)
        elif name!=None and fuzzyVarType!=None:
            assert type(name)==str and type(fuzzyVarType)==str
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createAggregatedFuzzyVariableType(name, fuzzyVarType)


    # 2 Methods of class FuzzyVariable

    def defuzzify(self):
        '''
        Method to defuzzify
        '''
        self.java_kbv.defuzzify()

    '''
    def setDefuzzifier(self, defuzz):
        #Sets the defuzzifier
        #:param defuzz: defuzzifier
        assert type(defuzz)==Defuzzifier
        self.java_afvt.setDefuzzifier(defuzz.java_d)
    '''

    # Method of class KnowledgeBaseVariable
    def isInput(self):
        '''
        Tests if the variable is input type
        :return: true if the variable is input type; false otherwise
        '''
        return self.java_kbv.isInput()

    def addAggregatedFuzzyTerm(self, aft):
        '''
        Add a AggregatedFuzzyTermType
        :param aft: AggregatedFuzzyTermType
        '''
        assert type(aft)==AggregatedFuzzyTermType
        self.java_kbv.addAggregatedFuzzyTerm(aft.java_t)

    def copy(self):
        '''
        Returns a new instance of the variable
        :return: a new instance of the variable
        '''
        return self.java_kbv.copy()

    def getAggregatedFuzzyTerm(self, i):
        '''
        Returns the i-th AggregatedFuzzyTermType
        :param i: index
        :return: the i-th AggregatedFuzzyTermType
        '''
        assert type(i)==int
        return self.java_kbv.getAggregatedFuzzyTerm(i)

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
        Gets the value of the aggregatedFuzzyTerm property
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

