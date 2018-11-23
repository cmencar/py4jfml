'''
This class creates an XML file with the definition of a Mamdani-type FLS for the Tipper ruleression problem:
    1) Two input variables (food and service) with Triangular, rightLinear, leftGaussian, gaussian and rightGaussian membership functions
    2) Three rules:
        + Use of edge "very" in rule1
'''
from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem
from py4jfml.Py4Jfml import Py4jfml
from py4jfml.knowledgebase.KnowledgeBaseType import KnowledgeBaseType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.rule.AntecedentType import AntecedentType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.rule.ConsequentType import ConsequentType
from py4jfml.rule.FuzzyRuleType import FuzzyRuleType
from py4jfml.rulebase.MamdaniRuleBaseType import MamdaniRuleBaseType
from py4jfml.term.FuzzyTermType import FuzzyTermType

tipper = FuzzyInferenceSystem("tipper - MAMDANI")

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

# FUZZY VARIABLE tip
tip = FuzzyVariableType("tip", 0., 20.)
tip.setDefaultValue(0.)
tip.setAccumulation("MAX")
tip.setDefuzzifierName("COG")
tip.setType("output")

# FUZZY TERM cheap
cheap = FuzzyTermType("cheap", FuzzyTermType.TYPE_triangularShape,[0., 5., 10.])
tip.addFuzzyTerm(cheap)

# FUZZY TERM average
average = FuzzyTermType("average", FuzzyTermType.TYPE_triangularShape,[5., 10., 15.])
tip.addFuzzyTerm(average)

# FUZZY TERM generous
generous = FuzzyTermType("generous", FuzzyTermType.TYPE_triangularShape,[10., 15., 20.])
tip.addFuzzyTerm(generous)

kb.addVariable(tip)

# RULE BASE
rb = MamdaniRuleBaseType("rulebase1")

# RULE1
rule1 = FuzzyRuleType("rule1", connector="or", connectorMethod="MAX", weight=1.)
ant1 = AntecedentType()
ant1.addClause(ClauseType(food, rancid))
ant1.addClause(ClauseType(service, poor, "very"))
con1 = ConsequentType()
con1.addThenClause(variable=tip, term=cheap)
rule1.setAntecedent(ant1)
rule1.setConsequent(con1)
rb.addRule(rule1)

# RULE2
rule2 = FuzzyRuleType("rule2", connector="or", connectorMethod="MAX", weight=1.)
ant2 = AntecedentType()
ant2.addClause(ClauseType(service, good))
con2 = ConsequentType()
con2.addThenClause(variable=tip, term=average)
rule2.setAntecedent(ant2)
rule2.setConsequent(con2)
rb.addRule(rule2)

# RULE3
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

tipperXMLFile = "TipperMamdani1.xml"
Py4jfml.writeFSTtoXML(tipper, tipperXMLFile)

print(tipper)

Py4jfml.kill()