from py4jfml.membershipfunction import CustomShapeType
from py4jfml.parameter import TwoParamType
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class TsukamotoTermType:
    '''
    Python class for tsukamotoTermType complex type
    '''
    def __init__(self,name=None,type_java=None,paramList=None,pointsList=None,psm=None):
        '''
        Constructor of class TsukamotoTermType
        :param name: the name of the Fuzzy Term
        :param type_java: the type (see static variables in FuzzyTerm)
        :param paramList: a list of parameters
        :param pointList: the list of PointType
        :param psm: an instance of PointSetMonotonicShapeType
        '''

        #Calling java default constructor
        if name==None and type_java==None and paramList==None and pointsList==None and psm==None:
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createTsukamotoTermType()

        #Call of the java constructor using the name, the type of fuzzy term and an array of parameters
        elif name!=None and type_java!=None and paramList!=None and pointsList==None and psm==None:
            assert type(name)==str and type(type_java)==int and type(paramList)==list
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createTsukamotoTermType(name,type_java,paramList)

        #Call of the java constructor of a PointSet term using the name and a list of PointType
        elif name!=None and type_java!=None and paramList==None and pointsList!=None and psm==None:
            assert type(name)==str and type(type_java)==int and type(pointsList)==list
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createTsukamotoTermType(name,type_java,pointsList)

        #Call of the java constructor using the name and an instance of PointSetMonotonicShapeType
        elif name!=None and type_java==None and paramList==None and pointsList==None and psm!=None:
            #assert type(name)==str and type(psm)==PointSetMonotonicShapeType
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createTsukamotoTermType(name,psm)

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

    def setComplement(self, value):
        """
        Sets the value of the property complement
        :param value: allowed object is String
        """
        assert type(value) == str
        self.java_t.setComplement(str(value))

    def setCustomMonotonicShape(self,value):
        '''
        Sets the value of the property customMonotonicShape.
        :param value: allowed object is CustomShapeType
        '''
        assert type(value)==CustomShapeType
        self.java_t.setCustomMonotonicShape(value.java_cst)

    def setLeftGaussianShape(self,value):
        '''
        Sets the value of the property leftGaussianShape
        :param value: allowed object is TwoParamType
        '''
        assert type(value)==TwoParamType
        self.java_t.setLeftGaussianShape(value.java_p)

    def setLeftLinearShape(self,value):
        '''
        Sets the value of the property leftLinearShape
        :param value: allowed object is TwoParamType
        '''
        assert type(value)==TwoParamType
        self.java_t.setLeftLinearShape(value.java_p)

    def setPointSetMonotonicShape(self,value):
        '''
        Sets the value of the property pointSetMonotonicShape
        :param value: allowed object is PointSetMonotonicShapeType
        '''
        #assert type(value)==PointSetMonotonicShapeType
        self.java_t.setPointSetMonotonicShape(value.java_psmst)

    def setRightGaussianShape(self,value):
        '''
        Sets the value of the property rightGaussianShape
        :param value: allowed object is TwoParamType
        '''
        assert type(value)==TwoParamType
        self.java_t.setRightGaussianShape(value.java_p)

    def setRightLinearShape(self,value):
        '''
        Sets the value of the property rightLinearShape
        :param value: allowed object is TwoParamType
        '''
        assert type(value)==TwoParamType
        self.java_t.setRightLinearShape(value.java_p)

    def setSShape(self,value):
        '''
        Sets the value of the property sShape
        :param value: allowed object is TwoParamType
        '''
        assert type(value)==TwoParamType
        self.java_t.setSShape(value.java_p)

    def setZShape(self,value):
        '''
        Sets the value of the property zShape
        :param value: allowed object is TwoParamType
        '''
        assert type()==TwoParamType
        self.java_t.setZShape(value.java_p)

    def getName(self):
        '''
        Gets the value of the property name
        :return: possible object is String
        '''
        return self.java_t.getName()

    def getComplement(self):
        '''
        Gets the value of the property complement
        :return: possible object is String
        '''
        return self.java_t.getComplement()

    def getCustomMonotonicShape(self):
        '''
        Gets the value of the property customMonotonicShape
        :return: possible object is CustomShapeType
        '''
        return self.java_t.getCustomMonotonicShape()

    def getLeftGaussianShape(self):
        '''
        Gets the value of the property leftGaussianShape
        :return: possible object is TwoParamType
        '''
        return self.java_t.getLeftGaussianShape()

    def getLeftLinearShape(self):
        '''
        Gets the value of the property leftLinearShape
        :return: possible object is TwoParamType
        '''
        return self.java_t.getLeftLinearShape()

    def getParam(self):
        '''
        Gets a list of floats with the parameters of this fuzzy term
        :return: a list of floats with the parameters of this fuzzy term
        '''
        return self.java_t.getParam()

    def getPointSetMonotonicShape(self):
        '''
        Gets the value of the property pointSetMonotonicShape
        :return: possible object is PointSetMonotonicShapeType
        '''
        return self.java_t.getPointSetMonotonicShape()

    def getRightGaussianShape(self):
        '''
        Gets the value of the property rightGaussianShape
        :return: possible object is TwoParamType
        '''
        return self.java_t.getRightGaussianShape()

    def getRightLinearShape(self):
        '''
        Gets the value of the property rightLinearShape
        :return: possible object is TwoParamType
        '''
        return self.java_t.getRightLinearShape()

    def getSShape(self):
        '''
        Gets the value of the property sShape
        :return: possible object is TwoParamType
        '''
        return self.java_t.getSShape()

    def getZShape(self):
        '''
        Gets the value of the property zShape
        :return: possible object is TwoParamType
        '''
        return self.java_t.getZShape()

    def __str__(self):
        '''
        Gets the object as a string
        :return: possible object is string
        '''
        return self.java_t.toString()

    #Methods inherited from abstract class jfml.term.FuzzyTerm

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

    def getMembershipValue(self,x):
        '''
        Gets the membership degree by calculating the membership value of the parameter x to this term
        :param x: the float value x
        :return: the membership float value of the parameter x to this term
        '''
        assert type(x)==float
        return self.java_t.getMembershipValue(float(x))

    def getXValuesDefuzzifier(self):
        '''
        This function returns a list with values [x1, x2, x3, ...] which represents points in the x domain of the function needed by defuzzifer
        :return: a list with floats
        '''
        return self.java_t.getXValuesDefuzzifier()