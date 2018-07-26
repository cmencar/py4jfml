from py4j.java_gateway import JavaGateway
from py4jfml.knowledgebasevariable.AggregatedFuzzyVariableType import AggregatedFuzzyVariableType
from py4jfml.knowledgebasevariable.AnYaDataCloudType import AnYaDataCloudType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.knowledgebasevariable.TskVariableType import TskVariableType
from py4jfml.knowledgebasevariable.TsukamotoVariableType import TsukamotoVariableType
from py4jfml.rule.TskClauseType import TskClauseType
from py4jfml.rule.TskConsequentClausesType import TskConsequentClausesType
from py4jfml.term.TskTermType import TskTermType

gateway = JavaGateway()


class TskConsequentType:
    '''
    Python class for tskConsequentType complex type.
    '''

    def __init__(self, thenConseq=None, elseConseq=None):
        '''
        :param thenConseq: a then TskConsequentClausesType
        :param elseConseq: an else TskConsequentClausesType
        '''
        if thenConseq==None and elseConseq==None:
            self.java_tskct = gateway.entry_point.getJFMLRule_Factory().createTskConsequentType()
        elif thenConseq!=None and elseConseq!=None:
            assert type(thenConseq)==TskConsequentClausesType and type(elseConseq)==TskConsequentClausesType
            self.java_tskct = gateway.entry_point.getJFMLRule_Factory().createTskConsequentType(thenConseq.java_tskcct, elseConseq.java_tskcct)

    def addTskElseClause(self, c=None, variable=None, term=None):
        '''
        Adds a TSK ELSE TSKClauseType
        :param c: a TSK ELSE TskClauseType
        :param variable: the KnowledgeBaseVariable
        :param term: the TKSTerm
        '''
        if c != None and variable == None and term == None:
            assert type(c) == TskClauseType
            self.java_tskct.addTskElseClause(c.java_tskct)
        elif c==None and variable!=None and term!=None:
            assert type(variable)==AnYaDataCloudType or type(variable)==AggregatedFuzzyVariableType or type(variable)==FuzzyVariableType or type(variable) == TskVariableType or type(variable)==TsukamotoVariableType
            assert type(term)==TskTermType
            self.java_tskct.addTskElseClause(term.java_t)


    def addTskThenClause(self, c=None, variable=None, term=None):
        '''
        Adds a TSK THEN TSKClauseType
        :param c: a Tsk THEN TskClauseType
        :param variable: the KnowledgeBaseVariable
        :param term: the TSKTerm
        '''
        if c != None and variable == None and term == None:
            assert type(c) == TskClauseType
            self.java_tskct.addTskThenClause(c.java_tskct)
        elif c==None and variable!=None and term!=None:
            assert type(variable)==AnYaDataCloudType or type(variable)==AggregatedFuzzyVariableType or type(variable)==FuzzyVariableType or type(variable) == TskVariableType or type(variable)==TsukamotoVariableType
            assert type(term)==TskTermType or type(term)==str
            if type(term)==str:
                self.java_tskct.addTskThenClause(variable.kbv, term)
            else:
                self.java_tskct.addTskThenClause(variable.kbv, term.java_t)


    def getTskElse(self):
        '''
        Gets the value of the property tskelse
        :return: possible object is TskConsequentClausesType
        '''
        return self.java_tskct.getTskElse()

    def getThen(self):
        '''
        Gets the value of the property tskthen
        :return: possible object is TskConsequentClausesType
        '''
        return self.java_tskct.getThen()

    def setElse(self, value):
        '''
        Sets the value of the property tskelse
        :param value: allowed object is TskConsequentClausesType
        '''
        assert type(value)==TskConsequentClausesType
        self.java_tskct.setElse(value.java_tskcct)

    def setThen(self, value):
        '''
        Sets the value of the property tskthen
        :param value: allowed object is TskConsequentClausesType
        '''
        assert type(value)==TskConsequentClausesType
        self.java_tskct.setThen(value.java_tskcct)

