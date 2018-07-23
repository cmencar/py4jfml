from py4jfml.operator.AndLogicalType import *
from py4jfml.operator.OrLogicalType import *
from py4jfml.parameter.OneParamType import *
from py4jfml.parameter.TwoParamType import *
from py4jfml.parameter.ThreeParamType import *
from py4jfml.parameter.FourParamType import *
from py4jfml.knowledgebasevariable.AggregatedFuzzyVariableType import *
from py4jfml.knowledgebasevariable.FuzzyVariableType import *
from py4jfml.knowledgebasevariable.AnYaDataCloudType import *
from py4jfml.knowledgebasevariable.TskVariableType import *
from py4jfml.knowledgebasevariable.TsukamotoVariableType import *

from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class CircularDefinitionType:
    '''
    Python class for circularDefinitionType complex type.
    '''
    def __init__(self, andLogical=None, orLogical=None, var=None):
        '''
        Constructor of class FuzzyTermType CustomShapeType
        :param andLogical:
        :param orLogical:
        :param var:
        :param log:
        '''

        #Calling java default constructor
        if andLogical==None and orLogical==None and var==None:
            self.java_cdt = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularDefinitionType()

        #Call of the java constructor using an instance of AndLogicalType and an instance of KnowledgeBaseVariable
        elif orLogical==None:
            assert type(andLogical)==AndLogicalType
            assert type(var)==AggregatedFuzzyVariableType or type(var)==FuzzyVariableType or type(var)==AnYaDataCloudType or type(var)==TskVariableType or type(var)==TsukamotoVariableType
            self.java_cdt = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularDefinitionType(andLogical.java_lt, var.java_kbv)

        #Call of the java constructor using an instance of OrLogicalType and an instance of KnowledgeBaseVariable
        elif andLogical==None:
            assert type(orLogical)==OrLogicalType
            assert type(var)==AggregatedFuzzyVariableType or type(var)==FuzzyVariableType or type(var)==AnYaDataCloudType or type(var)==TskVariableType or type(var)==TsukamotoVariableType
            self.java_cdt = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularDefinitionType(orLogical.java_lt, var.java_kbv)

        #Call of the java constructor using an instance of AndLogicalType, an instance of OrLogicalType and an instance of KnowledgeBaseVariable
        else:
            assert type(andLogical)==AndLogicalType and type(orLogical)==OrLogicalType
            assert type(var)==AggregatedFuzzyVariableType or type(var)==FuzzyVariableType or type(var)==AnYaDataCloudType or type(var)==TskVariableType or type(var)==TsukamotoVariableType
            self.java_cdt = gateway.entry_point.getJFMLMembershipfunction_Factory().createCircularDefinitionType(andLogical.java_lt, orLogical.java_lt, var.java_kbv)

    def copy(self):
        '''
        Creates a copy of the object
        :return: a new instance of CircularDefinitionType
        '''
        return self.java_cdt.copy()

    def setAnd(self,andLogical):
        '''
        Sets the value of the property and.
        :param andLogical: allowed object is AndLogicalType
        '''
        assert type(andLogical)==AndLogicalType
        self.java_cdt.setAnd(andLogical.java_alt)

    def setOr(self,orLogical):
        '''
        Sets the value of the property or
        :param orLogical: allowed object is OrLogicalType
        '''
        assert type(orLogical)==OrLogicalType
        self.java_cdt.setOr(orLogical.java_olt)

    def setVariable(self,var):
        '''
        Set the FuzzyVariableType which contains the terms
        :param var: allowed object is KnowledgeBaseVariable
        '''
        assert type(var)==AggregatedFuzzyVariableType or type(var)==FuzzyVariableType or type(var)==AnYaDataCloudType or type(var)==TskVariableType or type(var)==TsukamotoVariableType
        self.java_cdt.setVariable(var.java_kbv)

    def getAnd(self):
        '''
        Gets the value of the property and
        :return: possible object is AndLogicalType
        '''
        return self.java_cdt.getAnd()

    def getOr(self):
        '''
        Gets the value of the property or
        :return: possible object is OrLogicalType
        '''
        return self.java_cdt.getOr()

    def getVariable(self):
        '''
        Get the FuzzyVariableType which contains the terms
        :return: possible object is AggregatedFuzzyVariableType or FuzzyVariableType or AnYaDataCloudType or TskVariableType or TsukamotoVariableType
        '''
        return self.java_cdt.getVariable()

    def getXValuesDefuzzifier(self):
        '''
        This function returns a list with values [x1, x2, x3, ...] which represents points in the x domain of the function needed by defuzzifer
        :return: an list with floats
        '''
        return self.java_cdt.getXValuesDefuzzifier()

    def __str__(self):
        '''
        Gets the object as a string
        :return: possible object is string
        '''
        return self.java_cdt.toString()

    #Methods inherited from abstract class jfml.membershipfunction.MembershipFunction

    def setDomainLeft(self, domainLeft):
        '''
        Sets the left domain value
        :param domainLeft: the left domain value
        '''
        assert type(domainLeft) == float
        self.java_cdt.setDomainLeft(float(domainLeft))

    def setDomainRight(self, domainRight):
        '''
        Sets the right domain value
        :param domainRight: the right domain value
        '''
        assert type(domainRight) == float
        self.java_cdt.setDomainRight(float(domainRight))

    def setParameter(self, p):
        '''
        Sets the parameter
        :param p: the parameter
        '''
        assert type(p)==OneParamType or type(p)==TwoParamType or type(p)==ThreeParamType or type(p)==FourParamType
        self.java_cdt.setParameter(p.java_p)

    def getDomainLeft(self):
        '''
        Gets the left domain
        :return: the left domain
        '''
        return self.java_cdt.getDomainLeft()

    def getDomainRight(self):
        '''
        Gets the right domain
        :return: the right domain
        '''
        return self.java_cdt.getDomainRight()

    def getName(self):
        '''
        Gets the name of the function
        :return: the name of the function
        '''
        return self.java_cdt.getName()

    def getParameter(self):
        '''
        Gets the Parameter associated to this function
        :return: the Parameter associated to this function
        '''
        return self.java_cdt.getParameter()