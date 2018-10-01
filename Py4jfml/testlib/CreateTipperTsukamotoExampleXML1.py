'''
This class creates an XML file with the definition of a Tsukamoto-type FLS for the Tipper ruleression problem:
    1) Two input variables (food and service) with Triangular, rightLinear, leftGaussian, gaussian and rightGaussian membership functions
    2) One output with monotone (leftLinear, z and rightGaussian) membership functions
    3) Three rules
'''
from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem
from py4jfml.Py4Jfml import Py4jfml
from py4jfml.knowledgebase.KnowledgeBaseType import KnowledgeBaseType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.knowledgebasevariable.TsukamotoVariableType import TsukamotoVariableType
from py4jfml.rule.AntecedentType import AntecedentType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.rule.ConsequentType import ConsequentType
from py4jfml.rule.FuzzyRuleType import FuzzyRuleType
from py4jfml.rulebase.TsukamotoRuleBaseType import TsukamotoRuleBaseType
from py4jfml.term.FuzzyTermType import FuzzyTermType
from py4jfml.term.TsukamotoTermType import TsukamotoTermType

tipper = FuzzyInferenceSystem("tipper - TSUKAMOTO")

# KNOWLEDGE BASE
kb = KnowledgeBaseType()
tipper.setKnowledgeBase(kb)

# FUZZY VARIABLE food
food = FuzzyVariableType("food", 0., 10.)

# FUZZY TERM rancid
rancid = FuzzyTermType("rancid", FuzzyTermType.TYPE_triangularShape,[0., 2., 5.5])
food.addFuzzyTerm(rancid)

# FUZZY TERM delicious
delicious = FuzzyTermType("delicious", FuzzyTermType.TYPE_rightLinearShape,[5.5, 10.])
food.addFuzzyTerm(delicious)

kb.addVariable(food)

# FUZZY VARIABLE service
service = FuzzyVariableType("service", 0., 10.)

# FUZZY TERM poor
poor = FuzzyTermType("poor", FuzzyTermType.TYPE_leftGaussianShape, [0., 2.])
service.addFuzzyTerm(poor)

# FUZZY TERM good
good = FuzzyTermType("good", FuzzyTermType.TYPE_gaussianShape, [5., 4.])
service.addFuzzyTerm(good)

# FUZZY TERM excellent
excellent = FuzzyTermType("excellent", FuzzyTermType.TYPE_rightGaussianShape, [10., 2.])
service.addFuzzyTerm(excellent)

kb.addVariable(service)

# TSUKAMOTO VARIABLE tip
tip = TsukamotoVariableType("tip", 0., 20.)
tip.setDefaultValue(0.)
tip.setCombination("WA")
tip.setType("output")

# TSUKAMOTO TERM cheap
cheap = TsukamotoTermType("cheap", FuzzyTermType.TYPE_leftLinearShape,[0., 10.])
tip.addTsukamotoTerm(t=cheap)

# TSUKAMOTO TERM average
average = TsukamotoTermType("average", FuzzyTermType.TYPE_zShape,[5., 15.])
tip.addTsukamotoTerm(t=average)

# TSUKAMOTO TERM generous
generous = TsukamotoTermType("generous", FuzzyTermType.TYPE_rightGaussianShape,[20., 10.])
tip.addTsukamotoTerm(t=generous)

kb.addVariable(tip)

#RULEBASE
rb = TsukamotoRuleBaseType("rulebase1")

#RULE1
rule1 = FuzzyRuleType("rule1", connector="or", connectorMethod="MAX", weight=1.)
ant1 = AntecedentType()
ant1.addClause(ClauseType(food, rancid))
ant1.addClause(ClauseType(service, poor, "very"))
con1 = ConsequentType()
con1.addThenClause(variable=tip, term=cheap)
rule1.setAntecedent(ant1)
rule1.setConsequent(con1)
rb.addRule(rule1)

#RULE2
rule2 = FuzzyRuleType("rule2", connector="or", connectorMethod="MAX", weight=1.)
ant2 = AntecedentType()
ant2.addClause(ClauseType(service, good))
con2 = ConsequentType()
con2.addThenClause(variable=tip, term=average)
rule2.setAntecedent(ant2)
rule2.setConsequent(con2)
rb.addRule(rule2)

#RULE3
rule3 = FuzzyRuleType("rule3", connector="or", connectorMethod="MAX", weight=1.)
ant3 = AntecedentType()
ant3.addClause(ClauseType(service, excellent))
ant3.addClause(ClauseType(food, delicious))
con3 = ConsequentType()
con3.addThenClause(variable=tip, term=generous)
rule3.setAntecedent(ant3)
rule3.setConsequent(con3)
rb.addRule(rule3)

tipper.addRuleBase(rb)

# WRITTING TIPPER EXAMPLE INTO AN XML FILE
tipperXMLFile = "XMLFiles/TipperTsukamoto1.xml"
Py4jfml.writeFSTtoXML(tipper, tipperXMLFile)

print(tipper)

Py4jfml.kill()