from py4jfml.parameter import OneParamType as onept
from py4jfml.parameter import TwoParamType as twopt
from py4jfml.parameter import ThreeParamType as threept
from py4jfml.parameter import FourParamType as fourpt
from py4jfml.membershipfunction import PointType as pt
from py4j.java_collections import ListConverter
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class PointSetMonotonicShapeType:
    '''
    Python class for pointSetMonotonicShapeType complex type
    '''
    def __init__(self,domainLeft=None,domainRight=None,points=None):
        '''
        Constructor of class PointSetMonotonicShapeType
        :param domainLeft: left domain
        :param domainRight: right domain
        :param points: list of PointType
        '''

        if domainLeft==None and domainRight==None and points==None:
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createPointSetMonotonicShapeType()

        elif domainLeft!=None and domainRight!=None and points==None:
            assert type(domainLeft)==float and type(domainRight)==float
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createPointSetMonotonicShapeType(domainLeft,domainRight)

        elif domainLeft!=None and domainRight!=None and points!=None:
            assert type(domainLeft)==float and type(domainRight)==float and type(points)==list
            java_points_list = gateway.jvm.java.util.ArrayList()
            for p in points:
                java_points_list.add(p.java_mf)
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createPointSetMonotonicShapeType(domainLeft,domainRight,java_points_list)

        elif domainLeft==None and domainRight==None and points!=None:
            assert type(points)==list
            java_points_list = gateway.jvm.java.util.ArrayList()
            for p in points:
                java_points_list.add(p.java_mf)
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createPointSetMonotonicShapeType(java_points_list)

    def addPoint(self,x=None,y=None,p=None):
        '''
        Add a point to the list
        :param x: float value
        :param y: float value
        :param p: a PointType
        '''
        if x!=None and y!=None and p==None:
            assert type(x) == float and type(y) == float
            self.java_mf.addPoint(x, y)
        elif x==None and y==None and p!=None:
            assert type(p)==pt.PointType
            self.java_mf.addPoint(p)

    def setInterpolationMethod(self,value):
        '''
        Sets the value of the property interpolationMethod
        :param value: allowed object is MonotonicInterpolationMethodType
        '''
        assert type(value) == str
        java_mimt = gateway.entry_point.getJFMLEnemeration_Factory().createJFMLEnumeration_MonotonicInterpolationMethodType()
        java_mimt_value = java_mimt.fromValue(value)
        self.java_mf.setInterpolationMethod(java_mimt_value)

    def setPoints(self,points):
        '''
        Set points
        :param points: a list of PointType
        '''
        assert type(points)==list
        java_points_list = gateway.jvm.java.util.ArrayList()
        for p in points:
            java_points_list.add(p.java_mf)
        self.java_mf.setPoints(java_points_list)

    def getFi(self,y):
        '''
        This function returns the inverse value. Given y, return x where f(x)=y
        :param y: a float value
        :return: a float value
        '''
        assert type(y)==float
        return self.java_mf.getFi(y)

    def getInterpolationMethod(self):
        '''
        Gets the value of the property interpolationMethod
        :return: possible object is MonotonicInterpolationMethodType
        '''
        return self.java_mf.getInterpolationMethod()

    def getMembershipDegree(self,x):
        '''
        Get membership degree value
        :param x: Variable's 'x' value
        :return: float value, output must be in range [0,1]
        '''
        assert type(x)==float
        return self.java_mf.getMembershipDegree(x)

    def getPoints(self):
        '''
        Gets the value of the point property
        :return: Objects of the following type(s) are allowed in the list PointType
        '''
        return self.java_mf.getPoints()

    def getXValuesDefuzzifier(self):
        '''
        This function returns a list with values [x1, x2, x3, ...] which represents points in the x domain of the function needed by defuzzifer
        :return: an list with floats
        '''
        return self.java_mf.getXValuesDefuzzifier()

    def __str__(self):
        '''
        Gets the object as a string
        :return: possible object is string
        '''
        return self.java_mf.toString()

    #Methods inherited from abstract class jfml.membershipfunction.MembershipFunction

    def setDomainLeft(self,domainLeft):
        '''
        Sets the left domain value
        :param domainLeft: the left domain value
        '''
        assert type(domainLeft)==float
        self.java_mf.setDomainLeft(float(domainLeft))

    def setDomainRight(self,domainRight):
        '''
        Sets the right domain value
        :param domainRight: the right domain value
        '''
        assert type(domainRight)==float
        self.java_mf.setDomainRight(float(domainRight))

    def setParameter(self,p):
        '''
        Sets the parameter
        :param p: the parameter
        '''
        assert type(p)==onept.OneParamType or type(p)==twopt.TwoParamType or type(p)==threept.ThreeParamType or type(p)==fourpt.FourParamType
        self.java_mf.setParameter(p.java_p)

    def getDomainLeft(self):
        '''
        Gets the left domain
        :return: the left domain
        '''
        return self.java_mf.getDomainLeft()

    def getDomainRight(self):
        '''
        Gets the right domain
        :return: the right domain
        '''
        return self.java_mf.getDomainRight()

    def getName(self):
        '''
        Gets the name of the function
        :return: the name of the function
        '''
        return self.java_mf.getName()

    def getParameter(self):
        '''
        Gets the Parameter associated to this function
        :return: the Parameter associated to this function
        '''
        return self.java_mf.getParameter()