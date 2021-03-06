from py4jfml.operator import AndLogicalType as alt
from py4jfml.operator import OrLogicalType as olt
from py4jfml.parameter import OneParamType as onept
from py4jfml.parameter import TwoParamType as twopt
from py4jfml.parameter import ThreeParamType as threept
from py4jfml.parameter import FourParamType as fourpt
from py4jfml.knowledgebasevariable import AggregatedFuzzyVariableType as afvt
from py4jfml.knowledgebasevariable import FuzzyVariableType as  fvt
from py4jfml.knowledgebasevariable import AnYaDataCloudType as aydc
from py4jfml.knowledgebasevariable import TskVariableType as tskvt
from py4jfml.knowledgebasevariable import TsukamotoVariableType as tvt
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class CircularDefinitionType:
    '''
    Python class for circularDefinitionType complex type
    '''
    def __init__(self, andLogical=None, orLogical=None, var=None):
        '''
        Constructor of class CircularDefinitionType
        :param andLogical:
        :param orLogical:
        :param var:
        :param log:
        '''

        #Calling java default constructor
        if andLogical==None and orLogical==None and var==None:
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularDefinitionType()

        #Call of the java constructor using an instance of AndLogicalType and an instance of KnowledgeBaseVariable
        elif andLogical!=None and orLogical==None and var!=None:
            assert type(andLogical)==alt.AndLogicalType
            assert type(var)==afvt.AggregatedFuzzyVariableType or type(var)==fvt.FuzzyVariableType or type(var)==aydc.AnYaDataCloudType or type(var)==tskvt.TskVariableType or type(var)==tvt.TsukamotoVariableType
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularDefinitionType(andLogical.java_lt, var.java_kbv)

        #Call of the java constructor using an instance of OrLogicalType and an instance of KnowledgeBaseVariable
        elif andLogical==None and orLogical!=None and var!=None:
            assert type(orLogical)==olt.OrLogicalType
            assert type(var)==afvt.AggregatedFuzzyVariableType or type(var)==fvt.FuzzyVariableType or type(var)==aydc.AnYaDataCloudType or type(var)==tskvt.TskVariableType or type(var)==tvt.TsukamotoVariableType
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularDefinitionType(orLogical.java_lt, var.java_kbv)

        #Call of the java constructor using an instance of AndLogicalType, an instance of OrLogicalType and an instance of KnowledgeBaseVariable
        elif andLogical != None and orLogical != None and var != None:
            assert type(andLogical)==alt.AndLogicalType and type(orLogical)==olt.OrLogicalType
            assert type(var)==afvt.AggregatedFuzzyVariableType or type(var)==fvt.FuzzyVariableType or type(var)==aydc.AnYaDataCloudType or type(var)==tskvt.TskVariableType or type(var)==tvt.TsukamotoVariableType
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularDefinitionType(andLogical.java_lt, orLogical.java_lt, var.java_kbv)

    def copy(self):
        '''
        Creates a copy of the object
        :return: a new instance of CircularDefinitionType
        '''
        return self.java_mf.copy()

    def setAnd(self,andLogical):
        '''
        Sets the value of the property and.
        :param andLogical: allowed object is AndLogicalType
        '''
        assert type(andLogical)==alt.AndLogicalType
        self.java_mf.setAnd(andLogical.java_lt)

    def setOr(self,orLogical):
        '''
        Sets the value of the property or
        :param orLogical: allowed object is OrLogicalType
        '''
        assert type(orLogical)==olt.OrLogicalType
        self.java_mf.setOr(orLogical.java_lt)

    def setVariable(self,var):
        '''
        Set the FuzzyVariableType which contains the terms
        :param var: allowed object is KnowledgeBaseVariable
        '''
        assert type(var)==afvt.AggregatedFuzzyVariableType or type(var)==fvt.FuzzyVariableType or type(var)==aydc.AnYaDataCloudType or type(var)==tskvt.TskVariableType or type(var)==tvt.TsukamotoVariableType
        self.java_mf.setVariable(var.java_kbv)

    def getAnd(self):
        '''
        Gets the value of the property and
        :return: possible object is AndLogicalType
        '''
        return self.java_mf.getAnd()

    def getOr(self):
        '''
        Gets the value of the property or
        :return: possible object is OrLogicalType
        '''
        return self.java_mf.getOr()

    def getVariable(self):
        '''
        Get the FuzzyVariableType which contains the terms
        :return: possible object is AggregatedFuzzyVariableType or FuzzyVariableType or AnYaDataCloudType or TskVariableType or TsukamotoVariableType
        '''
        return self.java_mf.getVariable()

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