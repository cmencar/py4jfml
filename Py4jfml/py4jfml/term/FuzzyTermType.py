from py4jfml.membershipfunction.PointSetShapeType import *
from py4jfml.membershipfunction.CustomShapeType import *
from py4jfml.membershipfunction.CircularDefinitionType import *
from py4jfml.parameter.OneParamType import *
from py4jfml.parameter.TwoParamType import *
from py4jfml.parameter.ThreeParamType import *
from py4jfml.parameter.FourParamType import *
from py4j.java_gateway import JavaGateway
from py4j.java_collections import ListConverter
gateway = JavaGateway()

class FuzzyTermType:
    """
    Python class for fuzzyTermType complex type.
    """
    def __init__(self, name=None, type_java=None, param=None, circular=None, custom=None, point=None, complement=None, points=None):
        '''
        Constructor of class FuzzyTermType
        :param name: the name of the fuzzy term
        :param type_java: the type (see static variables in FuzzyTerm)
        :param circular: an instance of CircularDefinitionType
        :param custom: an instance of CustomShapeType
        :param point: an instance of PointSetShapeType
        :param complement: the complement (true or false)
        :param points: the list of PointType
        :param param: a list of parameters
        '''

        #Calling java default constructor
        if name==None and type_java==None and param==None and circular==None and custom==None and point==None and complement==None and points==None:
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createFuzzyTermType()

        #Call of the java constructor using the name and an instance of CircularDefinitionType
        elif type_java==None and param==None and custom==None and point==None and complement==None and points==None:
            assert type(name)==str and type(circular)==CircularDefinitionType
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createFuzzyTermType(str(name), circular.java_cdt)

        #Call of the java constructor using the name and an instance of CustomShapeType
        elif type_java==None and param==None and circular==None and point==None and complement==None and points==None:
            assert type(name)==str and type(custom)==CustomShapeType
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createFuzzyTermType(str(name), custom.java_cst)

        #Call of the java constructor using the name, the type of fuzzy term and an array of parameters
        elif circular==None and custom==None and point==None and complement==None and points==None:
            assert type(name)==str and type(type_java)==int and type(param)==list
            java_param_list = ListConverter().convert(param, gateway._gateway_client)
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createFuzzyTermType(str(name), int(type_java), java_param_list)

        #Call of the java constructor of a PointSet term using the name and a list of PointType
        elif circular==None and custom==None and point==None and complement==None and param==None:
            assert type(name)==str and type(type_java)==int and type(points)==list
            java_points_list = ListConverter().convert(points, gateway._gateway_client)
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createFuzzyTermType(str(name), int(type_java), java_points_list)

        #Call of the java constructor using the name and an instance of PointSetShapeType
        elif type_java==None and param==None and circular==None and custom==None and complement==None and points==None:
            assert type(name)==str and type(point)==PointSetShapeType
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createFuzzyTermType(str(name), point.java_psst)

        #Call of the java constructor using the name, the complement and a CircularDefinitionType
        elif type_java==None and param==None and point==None and custom==None and points==None:
            assert type(name)==str and type(complement)==str and type(circular)==CircularDefinitionType
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createFuzzyTermType(str(name), str(complement), circular.java_cdt)

        #Call of the java constructor using the name, the complement and a PointSetShapeType
        elif type_java==None and param==None and circular==None and custom==None and points==None:
            assert type(name)==str and type(complement)==str and type(point)==PointSetShapeType
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createFuzzyTermType(str(name), str(complement), point.java_psst)

    def copy(self):
        '''
        Creates a copy of the fuzzy term
        :return: a copy of the term
        '''
        return self.java_t.copy()

    def setCircularDefinition(self,value):
        '''
        Sets the value of the property circularDefinition
        :param value: allowed object is CircularDefinitionType
        '''
        assert type(value)==CircularDefinitionType
        self.java_t.setCircularDefinition(value.java_cdt)

    def setComplement(self, value):
        """
        Sets the value of the property complement
        :param value: allowed object is String
        """
        assert type(value)==str
        self.java_t.setComplement(str(value))

    def setCustomShape(self,value):
        '''
        Sets the value of the property customShape
        :param value: allowed object is CustomShapeType
        '''
        assert type(value)==CustomShapeType
        self.java_t.setCustomShape(value.java_cst)

    def setGaussianShape(self,value):
        '''
        Sets the value of the property gaussianShape
        :param value: allowed object is TwoParamType
        '''
        assert type(value)==TwoParamType
        self.java_t.setGaussianShape(value.java_p)

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

    def setName(self,value):
        '''
        Sets the value of the property name
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_t.setName(str(value))

    def setPiShape(self,value):
        '''
        Sets the value of the property piShape
        :param value: allowed object is TwoParamType
        '''
        assert type(value)==TwoParamType
        self.java_t.setPiShape(value.java_p)

    def setPointSetShape(self,value):
        '''
        Sets the value of the property pointSetShape
        :param value: allowed object is PointSetShapeType
        '''
        assert type(value)==PointSetShapeType
        self.java_t.setPointSetShape(value.java_psst)

    def setRectangularShape(self,value):
        '''
        Sets the value of the property rectangularShape
        :param value: allowed object is TwoParamType
        '''
        assert type(value)==TwoParamType
        self.java_t.setRectangularShape(value.java_p)

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

    def setSingletonShape(self,value):
        '''
        Sets the value of the property singletonShape
        :param value: allowed object is OneParamType
        '''
        assert type(value)==OneParamType
        self.java_t.setSingletonShape(value.java_p)

    def setSShape(self,value):
        '''
        Sets the value of the property sShape
        :param value: possible object is PointSetShapeType
        '''
        assert type(value)==PointSetShapeType
        self.java_t.setSShape(value.java_psst)

    def setTrapezoidShape(self,value):
        '''
        Sets the value of the property trapezoidShape
        :param value: allowed object is FourParamType
        '''
        assert type(value)==FourParamType
        self.java_t.setTrapezoidShape(value.java_p)

    def setTriangularShape(self,value):
        '''
        Sets the value of the property triangularShape
        :param value: allowed object is ThreeParamType
        '''
        assert type(value)==ThreeParamType
        self.java_t.setTriangularShape(value.java_p)

    def setZShape(self,value):
        '''
        Sets the value of the property zShape.
        :param value: allowed object is TwoParamType
        '''
        assert type(value)==TwoParamType
        self.java_t.setZShape(value.java_p)

    def getCircularDefinition(self):
        '''
        Gets the value of the property circularDefinition
        :return: possible object is CircularDefinitionType
        '''
        return self.java_t.getCircularDefinition()

    def getComplement(self):
        '''
        Gets the value of the property complement
        :return: possible object is String
        '''
        return self.java_t.getComplement()

    def getCustomShape(self):
        '''
        Gets the value of the property customShape
        :return: possible object is CustomShapeType
        '''
        return self.java_t.getCustomShape()

    def getGaussianShape(self):
        '''
        Gets the value of the property gaussianShape
        :return: possible object is TwoParamType
        '''
        return self.java_t.getGaussianShape()

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

    def getName(self):
        '''
        Gets the value of the property name.
        :return: possible object is String
        '''
        return self.java_t.getName()

    def getParam(self):
        '''
        Gets a list of floats with the parameters of this fuzzy term
        :return: a list of floats with the parameters of this fuzzy term
        '''
        return self.java_t.getParam()

    def getPiShape(self):
        '''
        Gets the value of the property piShape
        :return: possible object is TwoParamType
        '''
        return self.java_t.getPiShape()

    def getPointSetShape(self):
        '''
        Gets the value of the property pointSetShape
        :return: possible object is PointSetShapeType
        '''
        return self.java_t.getPointSetShape()

    def getRectangularShape(self):
        '''
        Gets the value of the property rectangularShape
        :return: possible object is TwoParamType
        '''
        return self.java_t.getRectangularShape()

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

    def getSingletonShape(self):
        '''
        Gets the value of the property singletonShape
        :return: possible object is OneParamType
        '''
        return self.java_t.getSingletonShape()

    def getSShape(self):
        '''
        Gets the value of the property sShape
        :return: possible object is TwoParamType
        '''
        return self.java_t.getSShape()

    def getTrapezoidShape(self):
        '''
        Gets the value of the property trapezoidShape
        :return: possible object is FourParamType
        '''
        return self.java_t.getTrapezoidShape()

    def getTriangularShape(self):
        '''
        Gets the value of the property triangularShape.
        :return: possible object is ThreeParamType
        '''
        return self.java_t.getTriangularShape()

    def getZShape(self):
        '''
        Gets the value of the property zShape.
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