from py4j.java_gateway import JavaGateway
from py4jfml.term import TsukamotoTermType

gateway = JavaGateway()

class TsukamotoVariableType:
    '''
    Python class for tsukamotoVariableType complex type
    '''

    def __init__(self, name=None, domainLeft=None, domainRight=None):
        '''
        Constructor
        :param name: name of the variable
        :param domainLeft: left domain
        :param domainRight: right domain
        '''
        if name==None and domainLeft==None and domainRight==None:
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createTsukamotoVariableType()
        elif name!=None and domainLeft!=None and domainRight!=None:
            assert type(name)==str and type(domainLeft)==float and type(domainRight)==float
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createTsukamotoVariableType(name, domainLeft, domainRight)


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

    def addTsukamotoTerm(self, name=None, termType=None, param=None, t=None):
        '''
        :param name:
        :param type:
        :param param:
        '''
        if name!=None and termType!=None and param!=None and t==None:
            assert type(name)==str and type(termType)==int and type(param)==list
            self.java_kbv.addTsukamotoTerm(name, termType, param)
        elif name==None and termType==None and param==None and t!=None:
            assert type(t)==TsukamotoTermType
            self.java_kbv.addTsukamotoTerm(t.java_t)

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
        :return: allowed object is Float
        '''
        return self.java_kbv.getDefaultValue()

    def getDomainleft(self):
        '''
        Gets the value of the property domainleft
        :return: possible object is float
        '''
        return self.java_kbv.getDomainleft()

    def getDomainright(self):
        '''
        Gets the value of the property domainright
        :return: possible object is float
        '''
        return self.java_kbv.getDomainright()

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

    def getTsukamotoTerm(self, i):
        '''
        Returns the i-th FuzzyTerm
        :param i: index
        :return: the i-th FuzzyTerm
        '''
        assert type(i)==int
        return self.java_kbv.getTsukamotoTerm(i)

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

    def setDomainleft(self, value):
        '''
        Sets the value of the property domainleft
        :param value: allowed object is float
        '''
        assert type(value)==float
        self.java_kbv.setDomainleft(value)

    def setDomainright(self, value):
        '''
        Sets the value of the property domainright
        :param value: allowed object is float
        '''
        assert type(value)==float
        self.java_kbv.setDomainright(value)

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


