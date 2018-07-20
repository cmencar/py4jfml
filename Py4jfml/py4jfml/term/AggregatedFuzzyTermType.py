from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class AggregatedFuzzyTermType:
    '''
    Python class for aggregatedFuzzyTermType complex type
    '''
    def __init__(self,name=None,andAgg=None,orAgg=None,agg=None):
        '''
        Constructor of class AggregatedFuzzyTermType
        :param name: the name of the term
        :param andAgg: the And AndAggregatedType
        :param orAgg: the Or OrAggregatedType
        :param agg: an instance of AndAggregatedType or OrAggregatedType
        '''

        #Calling java default constructor
        if name==None and andAgg==None and orAgg==None and agg==None:
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createAggregatedFuzzyTermType()

        #Call of the java constructor using the name
        if name!=None and andAgg==None and orAgg==None and agg==None:
            assert type(name)==str
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createAggregatedFuzzyTermType(name)

        #Call of the java constructor using the name and an AggregatedType
        if name!=None and andAgg==None and orAgg==None and agg!=None:
            assert type(name)==str
            #assert type(agg)==AndAggregatedType or type(agg)==OrAggregatedType
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createAggregatedFuzzyTermType(name,agg)

        #Call of the java constructor using the name and the AndAggregatedType and the OrAggregatedType
        if name!=None and andAgg!=None and orAgg!=None and agg==None:
            #assert type(name)==str and type(andAgg)==AndAggregatedType and type(orAgg)==OrAggregatedType
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createAggregatedFuzzyTermType(name,andAgg,orAgg)

    def copy(self):
        '''
        Creates a copy of the fuzzy term
        :return: a copy of the term
        '''
        return self.java_t.copy()

    def setName(self,value):
        '''
        Sets the value of the property name
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_t.setName(str(value))

    def setAnd(self, value):
        '''
        Sets the value of the property and
        :param value: allowed object is AndAggregatedType
        '''
        #assert type(value)==AndAggregatedType
        self.java_t.setAnd(value.java_at)

    def setOr(self, value):
        '''
        Sets the value of the property or
        :param value: allowed object is OrAggregatedType
        '''
        #assert type(value)==OrAggregatedType
        self.java_t.setOr(value.java_at)

    def getAnd(self):
        '''
        Gets the value of the property and
        :return: possible object is AndAggregatedType
        '''
        return self.java_t.getAnd()

    def getOr(self):
        '''
        Gets the value of the property or
        :return: possible object is OrAggregatedType
        '''
        return self.java_t.getOr()

    def getName(self):
        '''
        Gets the value of the property name
        :return: possible object is String
        '''
        return self.java_t.getName()

    def getComplement(self):
        '''
        Gets the complement (true or false)
        :return: the complement
        '''
        return self.java_t.getComplement()

    def getMembershipValue(self,x):
        '''
        Gets the membership degree by calculating the membership value of the parameter x to this term
        :param x: the float value x
        :return: the membership value of the parameter x to this term
        '''
        assert type(x)==float
        return self.java_t.getMembershipValue(float(x))

    def __str__(self):
        '''
        Gets the object as a string
        :return: possible object is string
        '''
        return self.java_t.toString()

    #Methods inherited from abstract class  jfml.term.FuzzyTerm

    def initializeMembershipFunction(self,domainLeft,domainRight):
        '''
        This function initializes the membership function associated to this term
        :param domainLeft: the left domain
        :param domainRight: the right domain
        '''
        assert type(domainLeft)==float and type(domainRight)==float
        self.java_t.initializeMembershipFunction(domainLeft,domainRight)

    def setType(self,valueType):
        '''
        Sets the value for the type according to the static variables
        :param valueType: the value for the type. Possible values:
        - TYPE_rightLinearShape
        - TYPE_leftLinearShape
        - TYPE_piShape
        - TYPE_triangularShape
        - TYPE_gaussianShape
        - TYPE_rightGaussianShape
        - TYPE_leftGaussianShape
        - TYPE_trapezoidShape
        - TYPE_singletonShape
        - TYPE_rectangularShape
        - TYPE_zShape
        - TYPE_sShape
        - TYPE_pointSetShape
        - TYPE_pointSetMonotonicShape
        - TYPE_circularDefinition
        - TYPE_customShape
        - TYPE_customMonotonicShape
        '''
        assert type(valueType)==int
        self.java_t.setType(int(valueType))

    def getFi(self,y):
        '''
        Gets the x value from y
        :param y: float value
        :return: the x float value from y
        '''
        assert type(y)==float
        return self.java_t.getFi(float(y))

    def getMembershipFunction(self):
        '''
        Gets the MembershipFunction associated to this term
        :return: the MembershipFunction associated to this term
        '''
        return self.java_t.getMembershipFunction()

    def getXValuesDefuzzifier(self):
        '''
        This function returns a list with values [x1, x2, x3, ...] which represents points in the x domain of the function needed by defuzzifer
        :return: a list with floats
        '''
        return self.java_t.getXValuesDefuzzifier()