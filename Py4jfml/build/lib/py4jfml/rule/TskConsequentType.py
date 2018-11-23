from py4j.java_gateway import JavaGateway
from py4jfml.knowledgebasevariable import AggregatedFuzzyVariableType as afvt
from py4jfml.knowledgebasevariable import AnYaDataCloudType as adct
from py4jfml.knowledgebasevariable import FuzzyVariableType as fvt
from py4jfml.knowledgebasevariable import TskVariableType as tskvt
from py4jfml.knowledgebasevariable import TsukamotoVariableType as tvt
from py4jfml.rule import TskClauseType as tskct
from py4jfml.rule import TskConsequentClausesType as tskcct
from py4jfml.term import TskTermType as tsktt

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
            assert type(thenConseq)==tskcct.TskConsequentClausesType and type(elseConseq)==tskct.TskConsequentClausesType
            self.java_tskct = gateway.entry_point.getJFMLRule_Factory().createTskConsequentType(thenConseq.java_tskcct, elseConseq.java_tskcct)

    def addTskElseClause(self, c=None, variable=None, term=None):
        '''
        Adds a TSK ELSE TSKClauseType
        :param c: a TSK ELSE TskClauseType
        :param variable: the KnowledgeBaseVariable
        :param term: the TKSTerm
        '''
        if c != None and variable == None and term == None:
            assert type(c)==tskct.TskClauseType
            self.java_tskct.addTskElseClause(c.java_tskct)
        elif c==None and variable!=None and term!=None:
            assert type(variable)==adct.AnYaDataCloudType or type(variable)==afvt.AggregatedFuzzyVariableType or type(variable)==fvt.FuzzyVariableType or type(variable)==tskvt.TskVariableType or type(variable)==tvt.TsukamotoVariableType
            assert type(term)==tsktt.TskTermType
            self.java_tskct.addTskElseClause(term.java_t)


    def addTskThenClause(self, c=None, variable=None, term=None):
        '''
        Adds a TSK THEN TSKClauseType
        :param c: a Tsk THEN TskClauseType
        :param variable: the KnowledgeBaseVariable
        :param term: the TSKTerm
        '''
        if c != None and variable == None and term == None:
            assert type(c)==tskct.TskClauseType
            self.java_tskct.addTskThenClause(c.java_tskct)
        elif c==None and variable!=None and term!=None:
            assert type(variable)==adct.AnYaDataCloudType or type(variable)==afvt.AggregatedFuzzyVariableType or type(variable)==fvt.FuzzyVariableType or type(variable)==tskvt.TskVariableType or type(variable)==tvt.TsukamotoVariableType
            assert type(term)==tsktt.TskTermType or type(term)==str
            if type(term)==str:
                self.java_tskct.addTskThenClause(variable.java_kbv, term)
            else:
                self.java_tskct.addTskThenClause(variable.java_kbv, term.java_t)


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
        assert type(value)==tskcct.TskConsequentClausesType
        self.java_tskct.setElse(value.java_tskcct)

    def setThen(self, value):
        '''
        Sets the value of the property tskthen
        :param value: allowed object is TskConsequentClausesType
        '''
        assert type(value)==tskcct.TskConsequentClausesType
        self.java_tskct.setThen(value.java_tskcct)

