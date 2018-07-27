from py4j.java_gateway import JavaGateway
from py4jfml.knowledgebasevariable import AggregatedFuzzyVariableType as afvt
from py4jfml.knowledgebasevariable import AnYaDataCloudType as adct
from py4jfml.knowledgebasevariable import FuzzyVariableType as fvt
from py4jfml.knowledgebasevariable import TskVariableType as tskvt
from py4jfml.knowledgebasevariable import TsukamotoVariableType as tvt
from py4jfml.term import AggregatedFuzzyTermType as aftt
from py4jfml.term import FuzzyTermType as ftt
from py4jfml.term import TsukamotoTermType as ttt

gateway = JavaGateway()

class ClauseType:
    '''
    Python class for clauseType complex type
    '''

    def __init__(self, variable=None, term=None, modifier=None):
        '''
        :param variable: possible object is KnowledgeBaseVariable
        :param term: possible object is FuzzyTerm
        :param modifier: a String with the modifier according to StandardModifierType
        '''
        if variable==None and term==None and modifier==None:
            self.java_ct = gateway.entry_point.getJFMLRule_Factory().createClauseType()
        elif variable!=None and term!=None and modifier==None:
            assert type(variable)==adct.AnYaDataCloudType or type(variable)==afvt.AggregatedFuzzyVariableType or type(variable)==fvt.FuzzyVariableType or type(variable)==tskvt.TskVariableType or type(variable)==tvt.TsukamotoVariableType
            assert type(term)==aftt.AggregatedFuzzyTermType or type(term)==ftt.FuzzyTermType or type(term)==ttt.TsukamotoTermType
            self.java_ct = gateway.entry_point.getJFMLRule_Factory().createClauseType(variable.java_kbv, term.java_t)
        elif variable!=None and term!=None and modifier!=None:
            assert type(variable)==adct.AnYaDataCloudType or type(variable)==afvt.AggregatedFuzzyVariableType or type(variable)==fvt.FuzzyVariableType or type(variable)==tskvt.TskVariableType or type(variable)==tvt.TsukamotoVariableType
            assert type(term)==aftt.AggregatedFuzzyTermType or type(term)==ftt.FuzzyTermType or type(term)==ttt.TsukamotoTermType
            assert type(modifier)==str
            self.java_ct = gateway.entry_point.getJFMLRule_Factory().createClauseType(variable.java_kbv, term.java_t, modifier)

    def getModifier(self):
        '''
        Gets the value of the property modifier
        :return: possible object is String
        '''
        return self.java_ct.getModifier()


    def getTerm(self):
        '''
        Gets the value of the property term
        :return:  the property term
        '''
        return self.java_ct.getTerm()

    def getVariable(self):
        '''
        Gets the value of the property variable
        :return: the property variable
        '''
        return self.java_ct.getVariable()

    def modifierMembershipDegree(self, x):
        '''
        Apply a modification to the membership degree x according to modifier property
        :param x: degree
        :return: degree
        '''
        assert type(x)==float
        return self.java_ct.modifierMembershipDegree(x)

    def setModifier(self, value):
        '''
        Sets the value of the property modifier
        :param value: allowed object is String
        '''
        assert type(value)==str
        return self.java_ct.setModifier(value)

    def setTerm(self, value):
        '''
        Sets the value of the property term
        :param value: a FuzzyTerm
        '''
        assert type(value)==aftt.AggregatedFuzzyTermType or type(value)==ftt.FuzzyTermType or type(value)==ttt.TsukamotoTermType
        self.java_ct.setTerm(value.java_t)

    def setVariable(self, variable):
        '''
        Sets the value of the property variable
        :param variable: possible object is KnowledgeBaseVariable
        '''
        assert type(variable)==adct.AnYaDataCloudType or type(variable)==afvt.AggregatedFuzzyVariableType or type(variable)==fvt.FuzzyVariableType or type(variable)==tskvt.TskVariableType or type(variable)==tvt.TsukamotoVariableType
        self.java_ct.setVariable(variable.java_kbv)

    def __str__(self):
        '''
        Returns a String object representing this object
        :return: possible object is string
        '''
        return self.java_ct.toString()
