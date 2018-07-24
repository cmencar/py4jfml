from py4jfml.parameter import OneParamType
from py4jfml.parameter import TwoParamType
from py4jfml.parameter import ThreeParamType
from py4jfml.parameter import FourParamType
from py4jfml.membershipfunction import CustomShapeType
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class CustomMembershipFunction:
    '''
    Python Class for implementing custom membership functions
    '''
    def __init__(self,c=None,p=None,domainLeft=None,domainRight=None):
        '''
        Constructor of class CustomMembershipFunction
        :param c: a CustomShapeType
        :param p: a Parameter
        :param domainLeft: left domain
        :param domainRight: right domain
        '''

        if c==None and p==None and domainLeft==None and domainRight==None:
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCustomMembershipFunction()

        elif c!=None and p==None and domainLeft==None and domainRight==None:
            assert type(c)==CustomShapeType
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCustomMembershipFunction(c.java_mf)

        elif c!=None and p==None and domainLeft!=None and domainRight!=None:
            assert type(c)==CustomShapeType and type(domainLeft)==float and type(domainRight)==float
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCustomMembershipFunction(c.java_mf,domainLeft,domainRight)

        elif c==None and p!=None and domainLeft==None and domainRight==None:
            assert type(p)==OneParamType or type(p)==TwoParamType or type(p)==ThreeParamType or type(p)==FourParamType
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCustomMembershipFunction(p.java_p)

    def getMembershipDegree(self,x):
        '''
        Get membership degree value.
        :param x: Variable's 'x' value
        :return: Float value, output must be in range [0,1]
        '''
        assert type(x)==float
        return self.java_mf.getMembershipDegree(x)

    def getXValuesDefuzzifier(self):
        '''
        This function returns a list with values [x1, x2, x3, ...] which represents points in the x domain of the function needed by defuzzifer
        :return: a list with floats
        '''
        return self.java_mf.getXValuesDefuzzifier()

    def __str__(self):
        '''
        Gets the object as a string
        :return: possible object is string
        '''
        return self.java_mf.toString()

    #Methods inherited from abstract class jfml.membershipfunction.MembershipFunction

    def setDomainLeft(self, domainLeft):
        '''
        Sets the left domain value
        :param domainLeft: the left domain value
        '''
        assert type(domainLeft)==float
        self.java_mf.setDomainLeft(domainLeft)

    def setDomainRight(self, domainRight):
        '''
        Sets the right domain value
        :param domainRight: the right domain value
        '''
        assert type(domainRight)==float
        self.java_mf.setDomainRight(domainRight)

    def setParameter(self, p):
        '''
        Sets the parameter
        :param p: the parameter
        '''
        assert type(p)==OneParamType or type(p)==TwoParamType or type(p)==ThreeParamType or type(p)==FourParamType
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