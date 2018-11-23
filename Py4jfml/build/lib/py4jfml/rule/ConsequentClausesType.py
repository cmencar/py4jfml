from py4j.java_gateway import JavaGateway
from py4jfml.knowledgebasevariable import AggregatedFuzzyVariableType as afvt
from py4jfml.knowledgebasevariable import AnYaDataCloudType as adct
from py4jfml.knowledgebasevariable import FuzzyVariableType as fvt
from py4jfml.knowledgebasevariable import TskVariableType as tskvt
from py4jfml.knowledgebasevariable import TsukamotoVariableType as tvt
from py4jfml.rule import ClauseType as ct
from py4jfml.term import AggregatedFuzzyTermType as afvt
from py4jfml.term import FuzzyTermType as ftt
from py4jfml.term import TskTermType as tsktt
from py4jfml.term import TsukamotoTermType as ttt

gateway = JavaGateway()

class ConsequentClausesType:
    '''
    Python class for consequentClausesType complex type
    '''

    def __init__(self, clauses=None):
        '''
        :param clauses: list of ClauseType
        '''
        if clauses==None:
            self.java_cct = gateway.entry_point.getJFMLRule_Factory().createConsequentClausesType()
        else:
            assert type(clauses)==list
            java_clauses_list = gateway.jvm.java.util.ArrayList()
            for c in clauses:
                java_clauses_list.add(c.java_ct)
            self.java_cct = gateway.entry_point.getJFMLRule_Factory().createConsequentClausesType(java_clauses_list)

    def addClause(self, c=None, v=None, t=None):
        '''
        if c is not none, adds a ClauseType to the list
        else, adds a ClauseType with a KnowledgeBaseVariable and a Term
        :param c: a ClauseType
        :param v:  the KnowledgeBaseVariable
        :param t: the Term
        '''
        if c!=None and v==None and t==None:
            assert type(c)==ct.ClauseType
            self.java_cct.addClause(c.java_ct)
        elif c==None and v!=None and t!=None:
            assert type(v)==adct.AnYaDataCloudType or type(v)==afvt.AggregatedFuzzyVariableType or type(v)==fvt.FuzzyVariableType or type(v)==tskvt.TskVariableType or type(v)==tvt.TsukamotoVariableType
            assert type(t)==afvt.AggregatedFuzzyTermType or type(t)==ftt.FuzzyTermType or type(t)==ttt.TsukamotoTermType or type(t)==tsktt.TskTermType
            self.java_cct.addClause(v.java_kbv, t.java_t)

    def getClause(self):
        '''
        Gets the value of the clause property
        :return: possible object is a list of clause type
        '''
        return self.java_cct.getClause()






