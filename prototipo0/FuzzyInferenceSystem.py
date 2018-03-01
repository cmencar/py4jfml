from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4j.java_collections import ListConverter

class FuzzyTerm:
    TYPE_rightLinearShape = 0
    TYPE_leftLinearShape = 1
    TYPE_piShape = 2
    TYPE_triangularShape = 3
    TYPE_gaussianShape = 4
    TYPE_rightGaussianShape = 5
    TYPE_leftGaussianShape = 6
    TYPE_trapezoidShape = 7
    TYPE_singletonShape = 8
    TYPE_rectangularShape = 9
    TYPE_zShape = 10
    TYPE_sShape = 11
    TYPE_pointSetShape = 12
    TYPE_pointSetMonotonicShape = 13
    TYPE_circularDefinition = 14
    TYPE_customShape = 15
    TYPE_customMonotonicShape = 16


class FuzzyInferenceSystem:
    def __init__(self):
        self.fuzzyInferenceSystem = gateway.entry_point.createFuzzyInferenceSystem()

    def __init__(self,name):
        self.fuzzyInferenceSystem = gateway.entry_point.createFuzzyInferenceSystem(name)

    def setKnowledgeBase(self, kb):
        self.fuzzyInferenceSystem.setKnowledgeBase(kb.java_kb)

    def addRuleBase(self,variable):
        self.fuzzyInferenceSystem.addRuleBase(variable.java_mrbt) #forse modificare vedi test0



class KnowledgeBaseType:
    def __init__(self):
        self.java_kb = gateway.entry_point.createKnowledgeBaseType()

    def addVariable(self,variable):
        self.java_kb.addVariable(variable.java_fvt)


class FuzzyVariableType:
    def __init__(self):
        self.java_fvt = gateway.entry_point.createFuzzyVariableType()

    def __init__(self,name,domainLeft,domainRight):
        self.java_fvt = gateway.entry_point.createFuzzyVariableType(name,float(domainLeft) ,float(domainRight))

    def addFuzzyTerm(self, variable):
        self.java_fvt.addFuzzyTerm(variable.java_ftt)



class FuzzyTermType:
    #forse bisogna mettere costruttore vuoto
    def __init__(self, name, num, points):
        java_list = ListConverter().convert(points, gateway._gateway_client)
        self.java_ftt = gateway.entry_point.createFuzzyTermType(name, int(num), java_list)

class MamdaniRuleBaseType:
    def __init__(self,name):
        self.java_mrbt= gateway.entry_point.createMamdaniRuleBaseType(name)

    def addRule(self, rule):
        self.java_mrbt.addRule(rule.java_frt)

class FuzzyRuleType:

    #forse eliminare dopo aver chiesto
    def __init__(self):
        self.java_frt = gateway.entry_point.createFuzzyRuleType()

    def __init__(self, name, connector, connectorMethod, weight):
        self.java_frt= gateway.entry_point.createFuzzyRuleType(name, connector, connectorMethod, weight)

    def setAntecedent(self,value):
        self.java_frt.setAntecedent(value.java_at)

    def setConsequent(self,value):
        self.java_frt.setConsequent(value.java_ct)

class AntecedentType:
    def __init__(self):
        self.java_at= gateway.entry_point.createAntecedentType()
    #forse bisogna aggiungere nuovi oggetti vedere in java
    def addClause(self,variable,term):
        self.java_at.addClause(variable.java_kb,term.ftt)

class ConsequentType:
    def __init__(self):
        self.java_ct = gateway.entry_point.createConsequentType()

    def addThenClause(self,variable,term):
        self.java_ct.addThenClause(variable.java_kb,term.java_ftt)