from py4j.java_collections import ListConverter
from py4j.java_gateway import JavaGateway
from py4jfml.knowledgebasevariable import AggregatedFuzzyVariableType as afvt
from py4jfml.knowledgebasevariable import AnYaDataCloudType as adct
from py4jfml.knowledgebasevariable import FuzzyVariableType as fvt
from py4jfml.knowledgebasevariable import TskVariableType as tskvt
from py4jfml.knowledgebasevariable import TsukamotoVariableType as tvt
from py4jfml.rule import ClauseType as ct
from py4jfml.term import AggregatedFuzzyTermType as aftt
from py4jfml.term import FuzzyTermType as ftt
from py4jfml.term import TsukamotoTermType as ttt

gateway = JavaGateway()

class AntecedentType:
    '''
    Python class for antecedentType complex type.
    '''

    def __init__(self, clauses=None):
        '''
        :param clauses: list of ClauseType
        '''
        if clauses==None:
            self.java_at = gateway.entry_point.getJFMLRule_Factory().createAntecedentType()
        else:
            assert type(clauses)==list
            javalist_clauses = ListConverter().convert(clauses, gateway._gateway_client)
            self.java_at = gateway.entry_point.getJFMLRule_Factory().createAntecedentType(javalist_clauses)

    def addClause(self, c=None, variable=None, term=None):
        '''
        Adds a ClauseType to the list of ClauseType
        :param c: the ClauseType
        :param variable: the KnowledgeBaseVariable
        :param term: the FuzzyTerm or the name of the FuzzyTerm
        '''
        if c != None and variable == None and term == None:
            assert type(c)==ct.ClauseType
            self.java_at.addClause(c.java_ct)
        elif c==None and variable!=None and term!=None:
            assert type(variable)==adct.AnYaDataCloudType or type(variable)==afvt.AggregatedFuzzyVariableType or type(variable)==fvt.FuzzyVariableType or type(variable)==tskvt.TskVariableType or type(variable)==tvt.TsukamotoVariableType
            assert type(term)==str or type(term)==aftt.AggregatedFuzzyTermType or type(term)==ftt.FuzzyTermType or type(term)==ttt.TsukamotoTermType
            if type(term)==str:
                self.java_at.addClause(variable.kbv, term)
            else:
                self.java_at.addClause(variable.kbv, term.java_t)


    def getClauses(self):
        '''
        Gets the value of the clause property
        :return: the value of the clause property
        '''
        return self.java_at.getClauses()



