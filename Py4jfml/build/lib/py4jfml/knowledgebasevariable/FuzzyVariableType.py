from py4j.java_gateway import JavaGateway
from py4jfml.defuzzifier import DefuzzifierLeftMostMax as dlmm
from py4jfml.defuzzifier import DefuzzifierRightMostMax as drmm
from py4jfml.defuzzifier import DefuzzifierCenterOfArea as dcoa
from py4jfml.defuzzifier import DefuzzifierCenterOfGravity as dcog
from py4jfml.defuzzifier import DefuzzifierCenterOfGravitySingletons as dcogs
from py4jfml.defuzzifier import DefuzzifierMeanMax as dmm
from py4jfml.term import FuzzyTermType as ftt

gateway = JavaGateway()

class FuzzyVariableType:
    '''
    Python class for the fuzzyVariableType complex type from IEEE Standard 1855
    '''

    def __init__(self, name=None, domainLeft=None, domainRight=None):
        '''
        Constructor
        :param name: name of the variable
        :param domainLeft: left domain
        :param domainRight: right domain
        '''
        if name==None and domainLeft==None and domainRight==None:
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createFuzzyVariableType()
        elif name!=None and domainLeft!=None and domainRight!=None:
            assert type(name)==str and type(domainLeft)==float and type(domainRight)==float
            self.java_kbv = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createFuzzyVariableType(name, domainLeft, domainRight)

    # 2 Methods of class FuzzyVariable

    def defuzzify(self):
        '''
        Method to defuzzify
        '''
        self.java_kbv.defuzzify()

    def setDefuzzifier(self, defuzz):
        #Sets the defuzzifier
        #:param defuzz: defuzzifier
        assert type(defuzz)==dcoa.DefuzzifierCenterOfArea or type(defuzz)==dcog.DefuzzifierCenterOfGravity or type(defuzz)==dcogs.DefuzzifierCenterOfGravitySingletons \
               or type(defuzz)==dlmm.DefuzzifierLeftMostMax or type(defuzz)==dmm.DefuzzifierMeanMax or type(defuzz)==drmm.DefuzzifierRightMostMax
        self.java_kbv.setDefuzzifier(defuzz.java_d)



    #Method of class KnowledgeBaseVariable
    def isInput(self):
        '''
        Tests if the variable is input type
        :return: true if the variable is input type; false otherwise
        '''
        return self.java_kbv.isInput()



    def accumulation(self, x, y):
        '''
        :param x:
        :param y:
        :return: the accumulation as a float
        '''
        assert type(x)==float and type(y)==float
        return self.java_kbv.accumulation(x,y)

    def addFuzzyTerm(self, ft=None, name=None, fuzzyTermType=None, param=None):
        '''
        Add a Fuzzy Term
        :param ft: fuzzy term
        :param name: fuzzy term name
        :param type: fuzzy term type
        :param param: array of parameters
        '''
        if ft!=None and name==None and fuzzyTermType==None and param==None:
            assert type(ft)==ftt.FuzzyTermType
            self.java_kbv.addFuzzyTerm(ft.java_t)
        if ft==None and name!=None and fuzzyTermType!=None and param!=None:
            assert type(name)==str and type(fuzzyTermType)==int and type(param)==list
            javaarray_param = gateway.new_array(gateway.jvm.float, len(param))
            for p in param:
                javaarray_param[param.index(p)] = p
            self.java_kbv.addFuzzyTerm(name, fuzzyTermType, javaarray_param)

    def copy(self):
        '''
        Returns a new instance of the variable
        :return: a new instance of the variable
        '''
        return self.java_kbv.copy()

    def getAccumulation(self):
        '''
        Gets the value of the property accumulation
        :return: possible object is String
        '''
        return self.java_kbv.getAccumulation()

    def getDefaultValue(self):
        '''
        Gets the value of the property defaultValue
        :return: possible object is Float
        '''
        return self.java_kbv.getDefaultValue()

    def getDefuzzifier(self):
        '''
        :return: possible object is Defuzzifier
        '''
        return self.java_kbv.getDefuzzifier()

    def getDefuzzifierName(self):
        '''
        Gets the value of the property defuzzifier
        :return: possible object is String
        '''
        return self.java_kbv.getDefuzzifierName()

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

    def getFuzzyTerm(self, i):
        '''
        Returns the i-th FuzzyTerm
        :param i: index of the FuzzyTerm
        :return: the i-th FuzzyTerm
        '''
        assert type(i)==int
        return self.java_kbv.getFuzzyTerm(i)

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
        Gets the value of the fuzzyTerm property
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
        If the variable is input type, return value setter. If the variable is output, return the deffuzifier value or the calculated tsk value Defuzzifier method
        :return: the defuzzification value
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

    def setAccumulation(self, value):
        '''
        Sets the value of the property accumulation.
        :param value: allowed object is String
        '''
        assert type(value) == str
        self.java_kbv.setAccumulation(value)

    def setDefaultValue(self, value):
        '''
        Sets the value of the property defaultValue
        :param value: allowed object is Float
        '''
        assert type(value)==float
        self.java_kbv.setDefaultValue(value)

    def setDefuzzifierName(self, value):
        '''
        Sets the value of the property defuzzifier
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_kbv.setDefuzzifierName(value)

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