from py4jfml.parameter import OneParamType as onept
from py4jfml.parameter import TwoParamType as twopt
from py4jfml.parameter import ThreeParamType as threept
from py4jfml.parameter import FourParamType as fourpt
from py4jfml.membershipfunction import CircularDefinitionType as cdt
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class CircularMembershipFunction:
    '''
    Python Class for CircularDefinition membership
    '''
    def __init__(self,p=None,domainLeft=None,domainRight=None):
        '''
        Constructor of class CircularMembershipFunction
        :param p: a CircularDefinitionType
        :param domainLeft: left domain
        :param domainRight: right domain
        '''

        #Calling java default constructor
        if p==None and domainLeft==None and domainRight==None:
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularMembershipFunction()

        #Call of the java constructor with a CircularDefinitionType as param
        elif p!=None and domainLeft==None and domainRight==None:
            assert type(p)==cdt.CircularDefinitionType
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularMembershipFunction(p.java_mf)

        #Call of the java constructor with a a CircularDefinitionType and the left and right domain
        elif p!=None and domainLeft!=None and domainRight!=None:
            assert type(p)==cdt.CircularDefinitionType and type(domainLeft)==float and type(domainRight)==float
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularMembershipFunction(p.java_mf,domainLeft,domainRight)

    def getMembershipDegree(self,x):
        '''
        Get membership degree value
        :param x: Variable's 'x' value
        :return: Float value, output must be in range [0,1]
        '''
        assert type(x)==float
        return self.java_mf.getMembershipDegree(x)

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