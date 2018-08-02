'''
This class creates an XML file with the definition of a TSK-type FLS for the Tipper ruleression problem:
 *   1) Two input variables (food and service) with Triangular, rightLinear, leftGaussian, gaussian and rightGaussian membership functions
 *   2) Three rules with order-0 and order-1 in the rule consequents
'''
from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem
from py4jfml.Py4Jfml import Py4jfml
from py4jfml.knowledgebase.KnowledgeBaseType import KnowledgeBaseType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.knowledgebasevariable.TskVariableType import TskVariableType
from py4jfml.rule.AntecedentType import AntecedentType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.rule.TskConsequentType import TskConsequentType
from py4jfml.rule.TskFuzzyRuleType import TskFuzzyRuleType
from py4jfml.rulebase.FuzzySystemRuleBase import FuzzySystemRuleBase
from py4jfml.rulebase.TskRuleBaseType import TskRuleBaseType
from py4jfml.term.FuzzyTermType import FuzzyTermType
from py4jfml.term.TskTermType import TskTermType
from py4jfml.term.TskTerm import TskTerm

tipper = FuzzyInferenceSystem("tipper - TSK")

#KNOWLEDGE BASE
kb = KnowledgeBaseType()
tipper.setKnowledgeBase(kb)

#FUZZY VARIABLE food
food = FuzzyVariableType(name="food", domainLeft=0.0, domainRight=10.0)

#FUZZY TERM delicious
delicious = FuzzyTermType(name="delicious", type_java=FuzzyTermType.TYPE_rightLinearShape, param=[5.5, 10.0])
food.addFuzzyTerm(delicious)

#FUZZY TERM rancid
rancid = FuzzyTermType(name="rancid", type_java=FuzzyTermType.TYPE_triangularShape, param=[0.0, 2.0, 5.5])
food.addFuzzyTerm(rancid)

kb.addVariable(food)

#FUZZY VARIABLE service
service = FuzzyVariableType(name="service", domainLeft=0.0, domainRight=10.0)

#FUZZY TERM excellent
excellent = FuzzyTermType(name="excellent", type_java=FuzzyTermType.TYPE_rightGaussianShape, param=[10.0, 2.0])
service.addFuzzyTerm(excellent)

#FUZZY TERM good
good = FuzzyTermType(name="good", type_java=FuzzyTermType.TYPE_gaussianShape, param=[5.0, 2.0])
service.addFuzzyTerm(good)
#FUZZY TERM poor
poor = FuzzyTermType(name="poor", type_java=FuzzyTermType.TYPE_leftGaussianShape, param=[0.0, 2.0])
service.addFuzzyTerm(poor)

kb.addVariable(service)

#TSK VARIABLE tip
tip = TskVariableType("tip")
tip.setDefaultValue(0.0)
tip.setCombination("WA")
tip.setType("output")

#TSK TERM average
average = TskTermType(name="average", order=TskTerm._ORDER_0, coeff=[1.6])
tip.addTskTerm(average)

#TSK TERM cheap
cheap = TskTermType(name="cheap", order=TskTerm._ORDER_1, coeff=[1.9, 5.6, 6.0])
tip.addTskTerm(cheap)
		
#TSK TERM generous
generous = TskTermType(name="generous", order=TskTerm._ORDER_1, coeff=[0.6, 1.3, 1.0])
tip.addTskTerm(generous)

kb.addVariable(tip)

#RULE BASE
fr = TskRuleBaseType(name="rulebase1", tskRuleBaseType=FuzzySystemRuleBase.TYPE_TSK)
fr.setActivationMethod("PROD")

#RULE 1
rule1 = TskFuzzyRuleType(name="rule1", connector="or", connectorMethod="MAX", weight=1.0)
ant1 = AntecedentType()
ant1.addClause(c=ClauseType(food, rancid))
ant1.addClause(c=ClauseType(service, poor))
con1 = TskConsequentType()
con1.addTskThenClause(variable=tip, term=cheap)
rule1.setAntecedent(ant1)
rule1.setTskConsequent(con1)

fr.addTskRule(rule1)

#RULE 2
rule2 = TskFuzzyRuleType(name="rule2", connector="or", connectorMethod="MAX", weight=1.0)
ant2 = AntecedentType()
ant2.addClause(c=ClauseType(service, good))
con2 = TskConsequentType()
con2.addTskThenClause(variable=tip, term=average)
rule2.setAntecedent(ant2)
rule2.setTskConsequent(con2)

fr.addTskRule(rule2)

#RULE 3
rule3 = TskFuzzyRuleType(name="rule3", connector="or", connectorMethod="MAX", weight=1.0)
ant3 = AntecedentType()
ant3.addClause(c=ClauseType(service, excellent))
ant3.addClause(c=ClauseType(food, delicious))
con3 = TskConsequentType()
con3.addTskThenClause(variable=tip, term=generous)
rule3.setAntecedent(ant3)
rule3.setTskConsequent(con3)

fr.addTskRule(rule3)

tipper.addRuleBase(fr)

#WRITTING TIPPER EXAMPLE INTO AN XML FILE
str_xml = "XMLFiles/TipperTSK.xml"
Py4jfml.writeFSTtoXML(tipper, str_xml)

print(tipper)