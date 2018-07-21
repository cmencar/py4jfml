from py4jfml.rule.ClauseType import *
from py4jfml.rule.ConsequentClausesType import *
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class ConsequentType:
    '''
    Python class for consequentType complex type
    '''

    def __init__(self, thenConseq=None, elseConseq=None):
        '''
        :param thenConseq: a then ConsequentClausesType
        :param elseConseq: an else ConsequentClausesType
        '''
        if thenConseq==None and elseConseq==None:
            self.java_ct = gateway.entry_point.getJFMLRule_Factory().createConsequentType()
        elif thenConseq!=None and elseConseq!=None:
            assert type(thenConseq)==ConsequentClausesType and type(elseConseq)==ConsequentClausesType
            self.java_ct = gateway.entry_point.getJFMLRule_Factory().createConsequentType(thenConseq.java_cct, elseConseq.java_cct)

    def addElseClause(self, c=None, variable=None, term=None):
        '''
        Adds an ELSE ClauseType
        :param c: an ELSE ClauseType
        :param variable: the KnowledgeBaseVariable
        :param term: the FuzzyTerm or the name of the FuzzyTerm
        '''
        if c!=None and variable==None and term==None:
            assert type(c)==ClauseType
            self.java_ct.addElseClause(c.java_ct)
        elif c==None and variable!=None and term!=None:
            assert type(variable)==AnYaDataCloudType or type(variable)==AggregatedFuzzyVariableType or type(variable)==FuzzyVariableType or type(variable) == TskVariableType or type(variable)==TsukamotoVariableType
            assert type(term)==str or type(term)==AggregatedFuzzyTermType or type(term)==FuzzyTermType or type(term)==TsukamotoTermType
            if type(term)==str:
                self.java_ct.addElseClause(variable.kbv, term)
            else:
                self.java_ct.addElseClause(variable.kbv, term.java_t)


    def addThenClause(self, c=None, variable=None, term=None):
        '''
        Adds a THEN ClauseType
        :param c: a THEN ClauseType
        :param variable: the KnowledgeBaseVariable
        :param term: the FuzzyTerm or the name of the FuzzyTerm
        '''
        if c!=None and variable==None and term==None:
            assert type(c)==ClauseType
            self.java_ct.addThenClause(c.java_ct)
        elif c==None and variable!=None and term!=None:
            assert type(variable)==AnYaDataCloudType or type(variable)==AggregatedFuzzyVariableType or type(variable)==FuzzyVariableType or type(variable) == TskVariableType or type(variable)==TsukamotoVariableType
            assert type(term)==str or type(term)==AggregatedFuzzyTermType or type(term)==FuzzyTermType or type(term)==TsukamotoTermType
            if type(term)==str:
                self.java_ct.addThenClause(variable.kbv, term)
            else:
                self.java_ct.addThenClause(variable.kbv, term.java_t)


    def getElse(self):
        '''
        Gets the value of the property else
        :return: possible object is ConsequentClausesType
        '''
        return self.java_ct.getElse()

    def getThen(self):
        '''
        Gets the value of the property then
        :return: possible object is ConsequentClausesType
        '''
        return self.java_ct.getThen()

    def setElse(self, value):
        '''
        Sets the value of the property else
        :param value: allowed object is ConsequentClausesType
        '''
        assert type(value)==ConsequentClausesType
        self.java_ct.setElse(value.java_cct)

    def setThen(self, value):
        '''
        Sets the value of the property then
        :param value: allowed object is ConsequentClausesType
        '''
        assert type(value)==ConsequentClausesType
        self.java_ct.setThen(value.java_cct)