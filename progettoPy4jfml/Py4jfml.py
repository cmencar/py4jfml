from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4j.java_collections import ListConverter

class PY4JFML:

    @staticmethod
    def load(xml_fileName):
        assert type(xml_fileName) == str
        JFML = gateway.entry_point.createJFML()
        xml = gateway.jvm.java.io.File(str(xml_fileName))
        java_fis = JFML.load(xml)
        fuzzyInferenceSystem = FuzzyInferenceSystem(java_fis)
        return fuzzyInferenceSystem


    @staticmethod
    def writeFSTtoXML(fst, str_output):
        assert type(fst) == FuzzyInferenceSystem and type(str_output) == str
        JFML = gateway.entry_point.createJFML()
        xmlOutput = gateway.jvm.java.io.File(str(str_output))
        return JFML.writeFSTtoXML(fst.java_fis, xmlOutput)


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
    def __init__(self,name=None):
        if name==None:
            self.java_fis = gateway.entry_point.createFuzzyInferenceSystem()
        elif type(name) == str:
            assert type(name) == str
            self.java_fis = gateway.entry_point.createFuzzyInferenceSystem(str(name))
        elif(type(name)== FuzzyInferenceSystem):
            self.java_fis = name.fuzzyInferenceSystem
        else:
            self.java_fis = name


    def setKnowledgeBase(self, value):
        assert type(value) == KnowledgeBaseType
        self.java_fis.setKnowledgeBase(value.java_kb)

    def addRuleBase(self,r):
        assert type(r) == MamdaniRuleBaseType
        self.java_fis.addRuleBase(r.java_mrbt)

    #aggiunta
    def getVariable(self,name):
        assert type(name) == str
        return FuzzyVariableType(self.java_fis.getVariable(str(name)))

    #aggiunta
    def evaluate(self):
        self.java_fis.evaluate()

    def __str__(self):
        return self.java_fis.toString()


class KnowledgeBaseType:
    def __init__(self):
        self.java_kb = gateway.entry_point.createKnowledgeBaseType()

    def addVariable(self,var):
        assert type(var) == FuzzyVariableType
        self.java_kb.addVariable(var.java_fvt)




class FuzzyVariableType:
    def __init__(self,name=None,domainLeft=None,domainRight=None):
        if(name==None):
            self.java_fvt = gateway.entry_point.createFuzzyVariableType()
        elif(type(name) == str and type(domainRight)== float and type(domainLeft)==float):
            assert type(name) == str and type(domainRight)== float and type(domainLeft)==float
            self.java_fvt = gateway.entry_point.createFuzzyVariableType(str(name),float(domainLeft) ,float(domainRight))
        else:
            self.java_fvt = name

    def addFuzzyTerm(self, ft):
        assert  type(ft) == FuzzyTermType
        self.java_fvt.addFuzzyTerm(ft.java_ftt)


    def setValue(self, x):
        assert type(x) == float
        self.java_fvt.setValue(float(x))


    def getValue(self):
        return self.java_fvt.getValue()


    def getName(self):
        return self.java_fvt.getName()

    #aggiunta
    def setDefaultValue(self, value):
        assert type(value) == float
        self.java_fvt.setDefaultValue(float(value))

    #aggiunta
    def setAccumulation(self, value):
        assert type(value) == str
        self.java_fvt.setAccumulation(str(value))

    #aggiunta
    def setDefuzzifierName(self, value):
        assert type(value) == str
        self.java_fvt.setDefuzzifierName(str(value))

    #aggiunta
    def setType(self, value):
        assert  type(value) == str
        self.java_fvt.setType(str(value))

class FuzzyTermType:
    def __init__(self, name, type_java, param):
        assert type(name) == str and type(type_java) == int and type(param) == list
        java_list = ListConverter().convert(param, gateway._gateway_client)
        self.java_ftt = gateway.entry_point.createFuzzyTermType(str(name), int(type_java), java_list)

    def setComplement(self, value):
        assert type(value) == str
        self.java_ftt.setComplement(str(value))

class MamdaniRuleBaseType:
    def __init__(self,name):
        assert type(name) == str
        self.java_mrbt= gateway.entry_point.createMamdaniRuleBaseType(str(name))

    def addRule(self, rule):
        assert type(rule == FuzzyRuleType)
        self.java_mrbt.addRule(rule.java_frt)

class FuzzyRuleType:
    def __init__(self, name=None, connector=None, connectorMethod=None, weight=0.):
        if name==None:
            self.java_frt = gateway.entry_point.createFuzzyRuleType()
        else:
            assert type(name) == str and type(connector) == str and type(connectorMethod) == str and type(weight) == float
            self.java_frt= gateway.entry_point.createFuzzyRuleType(str(name), str(connector), str(connectorMethod), float(weight))

    def setAntecedent(self, value):
        assert  type(value) == AntecedentType
        self.java_frt.setAntecedent(value.java_at)

    def setConsequent(self, value):
        assert type(value) == ConsequentType
        self.java_frt.setConsequent(value.java_ct)

class AntecedentType:
    def __init__(self):
        self.java_at = gateway.entry_point.createAntecedentType()

    def addClause(self, c):
        assert type(c) == ClauseType
        self.java_at.addClause(c.java_clauseT)

class ConsequentType:
    def __init__(self):
        self.java_ct = gateway.entry_point.createConsequentType()

    def addThenClause(self, c):
        assert type(c) == ClauseType
        self.java_ct.addThenClause(c.java_clauseT)

class ClauseType:
    def __init__(self, variable, term, modifier=None):
        if modifier == None:
            assert type(variable) == FuzzyVariableType and type(term) == FuzzyTermType
            self.java_clauseT = gateway.entry_point.createClauseType(variable.java_fvt, term.java_ftt)
        else:
            assert type(variable) == FuzzyVariableType and type(term) == FuzzyTermType and type(modifier) == str
            self.java_clauseT = gateway.entry_point.createClauseType(variable.java_fvt, term.java_ftt, modifier)