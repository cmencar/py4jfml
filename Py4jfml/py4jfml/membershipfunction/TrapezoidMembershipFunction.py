from py4jfml.parameter import OneParamType
from py4jfml.parameter import TwoParamType
from py4jfml.parameter import ThreeParamType
from py4jfml.parameter import FourParamType
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class TrapezoidMembershipFunction:
    '''
    Python class for representing Trapezoid functions
    '''
    def __init__(self,p=None,domainLeft=None,domainRight=None):
        '''
        Constructor of class TrapezoidMembershipFunction
        :param p: parameter -> a, b, c and d. Parameters must satisfy a <= b <= c <= d
        :param domainLeft: left domain
        :param domainRight: right domain
        '''

        #Calling java default constructor
        if p==None and domainLeft==None and domainRight==None:
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createTrapezoidMembershipFunction()

        #Call of the java constructor with Parameter instance with the parameters of the function
        elif p!=None and domainLeft==None and domainRight==None:
            assert type(p)==OneParamType or type(p)==TwoParamType or type(p)==ThreeParamType or type(p)==FourParamType
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createTrapezoidMembershipFunction(p.java_p)

        #Call of the java constructor with Parameter instance with the parameters of the function
        elif p!=None and domainLeft!=None and domainRight!=None:
            assert type(p)==OneParamType or type(p)==TwoParamType or type(p)==ThreeParamType or type(p)==FourParamType
            assert type(domainLeft)==float and type(domainRight)==float
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createTrapezoidMembershipFunction(p.java_p,domainLeft,domainRight)

    def getMembershipDegree(self,x):
        '''
        Get membership degree value
        :param x: Variable's 'x' value
        :return: float value, output must be in range [0,1]
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
        self.java_mf.setDomainLeft(float(domainLeft))

    def setDomainRight(self, domainRight):
        '''
        Sets the right domain value
        :param domainRight: the right domain value
        '''
        assert type(domainRight)==float
        self.java_mf.setDomainRight(float(domainRight))

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