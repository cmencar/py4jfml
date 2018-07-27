from py4j.java_collections import ListConverter
from py4j.java_gateway import JavaGateway
from py4jfml.knowledgebasevariable.AggregatedFuzzyVariableType import AggregatedFuzzyVariableType
from py4jfml.knowledgebasevariable.AnYaDataCloudType import AnYaDataCloudType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.knowledgebasevariable.TskVariableType import TskVariableType
from py4jfml.knowledgebasevariable.TsukamotoVariableType import TsukamotoVariableType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.term.AggregatedFuzzyTermType import AggregatedFuzzyTermType
from py4jfml.term.FuzzyTermType import FuzzyTermType
from py4jfml.term.TsukamotoTermType import TsukamotoTermType

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
            assert type(c)==ClauseType
            self.java_at.addClause(c.java_ct)
        elif c==None and variable!=None and term!=None:
            assert type(variable)==AnYaDataCloudType or type(variable)==AggregatedFuzzyVariableType or type(variable)==FuzzyVariableType or type(variable) == TskVariableType or type(variable)==TsukamotoVariableType
            assert type(term)==str or type(term)==AggregatedFuzzyTermType or type(term)==FuzzyTermType or type(term)==TsukamotoTermType
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



