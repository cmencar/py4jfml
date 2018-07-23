from py4j.java_gateway import JavaGateway

from py4jfml.knowledgebasevariable import AnYaDataCloudType, AggregatedFuzzyVariableType, FuzzyVariableType, TskVariableType, TsukamotoVariableType
from py4jfml.rule import ClauseType
from py4jfml.term import AggregatedFuzzyTermType, FuzzyTermType, TsukamotoTermType, TskTermType

gateway = JavaGateway()

class ConsequentClausesType:
    '''
    Python class for consequentClausesType complex type
    '''

    def __int__(self, clauses=None):
        '''
        :param clauses: list of ClauseType
        '''
        if clauses==None:
            self.java_cct = gateway.entry_point.getJFMLRule_Factory().createConsequentClausesType()
        else:
            assert type(clauses)==list
            self.java_cct = gateway.entry_point.getJFMLRule_Factory().createConsequentClausesType(clauses)

    def addClause(self, c=None, v=None, t=None):
        '''
        if c is not none, adds a ClauseType to the list
        else, adds a ClauseType with a KnowledgeBaseVariable and a Term
        :param c: a ClauseType
        :param v:  the KnowledgeBaseVariable
        :param t: the Term
        '''
        if c!=None and v==None and t==None:
            assert type(c)==ClauseType
            self.java_cct.addClause(c.java_ct)
        elif c==None and v!=None and t!=None:
            assert type(v)==AnYaDataCloudType or type(v)==AggregatedFuzzyVariableType or type(v)==FuzzyVariableType or type(v)==TskVariableType or type(v)==TsukamotoVariableType
            assert type(t)==AggregatedFuzzyTermType or type(t)==FuzzyTermType or type(t)==TsukamotoTermType or type(t)==TskTermType
            self.java_cct.addClause(v.java_kbv, t.java_t)

    def getClause(self):
        '''
        Gets the value of the clause property
        :return: possible object is a list of clause type
        '''
        return self.java_cct.getClause()






