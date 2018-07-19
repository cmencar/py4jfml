from py4jfml.parameter.OneParamType import *
from py4jfml.parameter.TwoParamType import *
from py4jfml.parameter.ThreeParamType import *
from py4jfml.parameter.FourParamType import *
from py4j.java_gateway import JavaGateway
from py4j.java_collections import ListConverter
gateway = JavaGateway()

class PointSetShapeType:
    '''
    Python class for pointSetShapeType complex type
    '''
    def __init__(self, domainLeft=None, domainRight=None, points=None):
        '''
        Constructor of class PointSetShapeType
        :param domainLeft: left domain
        :param domainRight: right domain
        :param points: list of PointType
        '''

        #Calling java default constructor
        if domainLeft==None and domainRight==None and points==None:
            self.java_psst = gateway.entry_point.getJFMLMembershipfunction_Factory().createPointSetShapeType()

        #Call of the java constructor with left and right domain
        elif points==None:
            assert type(domainLeft)==float and type(domainRight)==float
            self.java_psst = gateway.entry_point.getJFMLMembershipfunction_Factory().createPointSetShapeType(domainLeft,domainRight)

        #Call of the java constructor with a list of PointType
        elif domainLeft==None and domainRight==None:
            assert type(points)==list
            java_points_list = ListConverter().convert(points, gateway._gateway_client)
            self.java_psst = gateway.entry_point.getJFMLMembershipfunction_Factory().createPointSetShapeType(java_points_list)

        #Call of the java constructor with left and right domain and a list of PointType
        else:
            assert type(domainLeft)==float and type(domainRight)==float and type(points)==list
            java_points_list = ListConverter().convert(points, gateway._gateway_client)
            self.java_psst = gateway.entry_point.getJFMLMembershipfunction_Factory().createPointSetShapeType(domainLeft,domainRight,java_points_list)

    def copy(self):
        '''
        Copy a PointSetShapeType
        :return: possible object is PointSetShapeType
        '''
        return self.java_psst.copy()

    def setDegree(self,value):
        '''
        Sets the value of the property degree
        :param value: allowed object is Integer
        '''
        assert type(value)==int
        self.java_psst.setDegree(int(value))

    def setInterpolationMethod(self,value):
        '''
        Sets the value of the property interpolationMethod
        :param value: allowed object is InterpolationMethodType
        '''
        #assert type(value)==InterpolationMethodType
        self.java_psst.setInterpolationMethod(value.java_imt)

    def getDegree(self):
        '''
        Gets the value of the property degree.
        :return: possible object is int
        '''
        return self.java_psst.getDegree()

    def getInterpolationMethod(self):
        '''
        Gets the value of the property interpolationMethod
        :return: possible object is InterpolationMethodType
        '''
        return self.java_psst.getInterpolationMethod()

    def getMembershipDegree(self,x):
        '''
        Get membership degree value.
        :param x: Variable's 'x' value
        :return: Note: Output must be in range [0,1]
        '''
        assert type(x)==float
        return self.java_psst.getMembershipDegree(float(x))

    def getPoints(self):
        '''
        Gets the value of the point property
        :return: Objects of the following type(s) are allowed in the list PointType
        '''
        return self.java_psst.getPoints()

    def getXValuesDefuzzifier(self):
        '''
        This function returns a list with values [x1, x2, x3, ...] which represents points in the x domain of the function needed by defuzzifer
        :return: a list with floats
        '''
        return self.java_psst.getXValuesDefuzzifier()

    def __str__(self):
        '''
        Gets the object as a string
        :return: possible object is string
        '''
        return self.java_psst.toString()

    #Methods inherited from abstract class jfml.membershipfunction.MembershipFunction

    def setDomainLeft(self,domainLeft):
        '''
        Sets the left domain value
        :param domainLeft: the left domain value
        '''
        assert type(domainLeft)==float
        self.java_psst.setDomainLeft(float(domainLeft))

    def setDomainRight(self,domainRight):
        '''
        Sets the right domain value
        :param domainRight: the right domain value
        '''
        assert type(domainRight)==float
        self.java_psst.setDomainRight(float(domainRight))

    def setParameter(self,p):
        '''
        Sets the parameter
        :param p: the parameter
        '''
        assert type(p)==OneParamType or type(p)==TwoParamType or type(p)==ThreeParamType or type(p)==FourParamType
        self.java_psst.setParameter(p.java_p)

    def getDomainLeft(self):
        '''
        Gets the left domain
        :return: the left domain
        '''
        return self.java_psst.getDomainLeft()

    def getDomainRight(self):
        '''
        Gets the right domain
        :return: the right domain
        '''
        return self.java_psst.getDomainRight()

    def getName(self):
        '''
        Gets the name of the function
        :return: the name of the function
        '''
        return self.java_psst.getName()

    def getParameter(self):
        '''
        Gets the Parameter associated to this function
        :return: the Parameter associated to this function
        '''
        return self.java_psst.getParameter()