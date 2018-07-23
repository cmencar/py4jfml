from py4j.java_gateway import JavaGateway

from py4jfml.knowledgebasevariable import AnYaDataCloudType, AggregatedFuzzyVariableType, FuzzyVariableType, TskVariableType, TsukamotoVariableType
from py4jfml.rule import TskClauseType
from py4jfml.term import AggregatedFuzzyTermType, FuzzyTermType, TsukamotoTermType, TskTermType

gateway = JavaGateway()


class TskConsequentClausesType:
    '''
    Python class for tskConsequentClausesType complex type.
    '''

    def __int__(self):
        '''
        '''
        self.java_tskcct = gateway.entry_point.getJFMLRule_Factory().createTskConsequentClausesType()

    def addTskClause(self, c=None, v=None, t=None):
        '''
        Adds a TskClauseType
        :param v: the KnowledgeBaseVariable
        :param t: the Term
        :param c: TskClauseType
        '''
        if c!=None and v==None and t==None:
            assert type(c)==TskClauseType
            self.java_tskcct.addTskClause(c.tskct)
        elif c==None and v!=None and t!=None:
            assert type(v)==AnYaDataCloudType or type(v)==AggregatedFuzzyVariableType or type(v)==FuzzyVariableType or type(v) == TskVariableType or type(v)==TsukamotoVariableType
            assert type(t)==str or type(t)==AggregatedFuzzyTermType or type(t)==FuzzyTermType or type(t)==TsukamotoTermType or type(t)==TskTermType
            if type(t)==str:
                self.java_tskcct.addTskClause(v.java_kbv, t)
            else:
                self.java_tskcct.addTskClause(v.java_kbv, t.java_t)


    def getTskClause(self):
        '''
        Gets the value of the tskClause property
        :return: the value of the tskClause property
        '''
        return self.java_tskcct.getTskClause()

