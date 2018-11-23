from py4j.java_gateway import JavaGateway
from py4jfml.knowledgebasevariable import AggregatedFuzzyVariableType as afvt
from py4jfml.knowledgebasevariable import AnYaDataCloudType as adct
from py4jfml.knowledgebasevariable import FuzzyVariableType as fvt
from py4jfml.knowledgebasevariable import TskVariableType as tskvt
from py4jfml.knowledgebasevariable import TsukamotoVariableType as tvt
from py4jfml.rule import TskClauseType as tskct
from py4jfml.term import AggregatedFuzzyTermType as aftt
from py4jfml.term import FuzzyTermType as ftt
from py4jfml.term import TskTermType as tsktt
from py4jfml.term import TsukamotoTermType as ttt

gateway = JavaGateway()


class TskConsequentClausesType:
    '''
    Python class for tskConsequentClausesType complex type.
    '''

    def __init__(self):
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
            assert type(c)==tskct.TskClauseType
            self.java_tskcct.addTskClause(c.tskct)
        elif c==None and v!=None and t!=None:
            assert type(v)==adct.AnYaDataCloudType or type(v)==afvt.AggregatedFuzzyVariableType or type(v)==fvt.FuzzyVariableType or type(v)==tskvt.TskVariableType or type(v)==tvt.TsukamotoVariableType
            assert type(t)==str or type(t)==aftt.AggregatedFuzzyTermType or type(t)==ftt.FuzzyTermType or type(t)==ttt.TsukamotoTermType or type(t)==tsktt.TskTermType
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

