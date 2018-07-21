from py4jfml.knowledgebasevariable.AnYaDataCloudType import *
from py4jfml.knowledgebasevariable.AggregatedFuzzyVariableType import *
from py4jfml.knowledgebasevariable.FuzzyVariableType import *
from py4jfml.knowledgebasevariable.TskVariableType import *
from py4jfml.knowledgebasevariable.TsukamotoVariableType import *
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()


class TskClauseType:
    '''
    Python class for tskClauseType complex type
    '''

    def __int__(self, variable=None, term=None):
        '''
        :param variable: possible object is KnowledgeBaseVariable
        :param term: possible object is FuzzyTerm
        '''
        if variable==None and term==None:
            self.java_tskct = gateway.entry_point.getJFMLRule_Factory().createTskClauseType()
        '''
        elif variable!=None and term!=None:
            assert type(variable)==AnYaDataCloudType or type(variable)==AggregatedFuzzyVariableType or type(variable)==FuzzyVariableType or type(variable)==TskVariableType or type(variable)==TsukamotoVariableType
            #INSERIRE ASSERT SU PARAMETRO TERM
            #self.java_tskct = gateway.entry_point.getJFMLRule_Factory().createTskClauseType(variable.kbv, term)
        '''

    def getTerm(self):
        '''
        Gets the value of the property term
        :return: possible object is Object
        '''
        return self.java_tskct.getTerm()

    def getVariable(self):
        '''
        Gets the value of the property variable
        :return: possible object is Object
        '''
        return self.java_tskct.getVariable()

    '''
    def setTerm(self, value):
        
        Sets the value of the property term
        :param value: allowed object is Object
        
        #INSERIRE ASSERT SU FUZZY TERM
        self.java_tskct.setTerm(value)
    '''

    def setVariable(self, value):
        '''
        Sets the value of the property variable
        :param value: allowed object is Object
        '''
        assert type(value)==AnYaDataCloudType or type(value)==AggregatedFuzzyVariableType or type(value)==FuzzyVariableType or type(value)==TskVariableType or type(value)==TsukamotoVariableType
        self.java_tskct.setVariable(value.kbv)