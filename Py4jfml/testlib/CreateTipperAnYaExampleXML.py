'''
This class creates an XML file with the definition of a AnYa-type FLS for the Tipper regression problem:
 *   1) Three input variables (food, service, and quality) defined as AnYaDataCloudType
 *   2) Three rules
'''
from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem
from py4jfml.Py4Jfml import Py4jfml
from py4jfml.knowledgebase.KnowledgeBaseType import KnowledgeBaseType
from py4jfml.knowledgebasevariable.AnYaDataCloudType import AnYaDataCloudType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.rule.AnYaAntecedentType import AnYaAntecedentType
from py4jfml.rule.AnYaRuleType import AnYaRuleType
from py4jfml.rule.ConsequentType import ConsequentType
from py4jfml.rulebase.AnYaRuleBaseType import AnYaRuleBaseType
from py4jfml.term.FuzzyTermType import FuzzyTermType

tipper = FuzzyInferenceSystem("tipper - AnYa")

#KNOWLEDGE BASE
kb = KnowledgeBaseType()
tipper.setKnowledgeBase(kb)

#CLOUD food
datumFood = [1.0,1.7,4.0,3.2]
cloudFood = AnYaDataCloudType(name="food", terms=datumFood)

kb.addVariable(var=cloudFood)

#CLOUD service
datumService = [6.0,5.7,7.0,4.6]
cloudService = AnYaDataCloudType(name="service", terms=datumService)

kb.addVariable(var=cloudService)

#CLOUD service
datumQuality = [8.0,7.7,10.0,8.6]
cloudQuality = AnYaDataCloudType(name="quality", terms=datumQuality)

kb.addVariable(var=cloudQuality)

#FUZZY VARIABLE tip
tip = FuzzyVariableType(name="tip", domainLeft=0.0, domainRight=20.0)
tip.setDefaultValue(0.0)
tip.setAccumulation("MAX")
tip.setDefuzzifierName("COG")
tip.setType("output")

#FUZZY TERM cheap
cheap = FuzzyTermType(name="cheap", type_java=FuzzyTermType.TYPE_triangularShape, param=[0.0, 5.0, 10.0])
tip.addFuzzyTerm(cheap)

#FUZZY TERM average
average = FuzzyTermType(name="average", type_java=FuzzyTermType.TYPE_triangularShape, param=[5.0, 10.0, 15.0])
tip.addFuzzyTerm(average)

#FUZZY TERM generous
generous = FuzzyTermType(name="generous", type_java=FuzzyTermType.TYPE_triangularShape, param=[10.0, 15.0, 20.0])
tip.addFuzzyTerm(generous)

kb.addVariable(tip)

#RULE BASE
rb = AnYaRuleBaseType("rulebase1")

#RULE 1
rule1 = AnYaRuleType(name="rule1")
ant1 = AnYaAntecedentType(dataCloud=cloudFood)
con1 = ConsequentType()
con1.addThenClause(variable=tip, term=cheap)
rule1.setAnYaAntecedent(ant1)
rule1.setConsequent(con1)
rb.addAnYaRule(rule1)

#RULE 2
rule2 = AnYaRuleType(name="rule2")
ant2 = AnYaAntecedentType(dataCloud=cloudService)
con2 = ConsequentType()
con2.addThenClause(variable=tip, term=average)
rule2.setAnYaAntecedent(ant2)
rule2.setConsequent(con2)
rb.addAnYaRule(rule2)

#RULE 3
rule3 = AnYaRuleType(name="rule3")
ant3 = AnYaAntecedentType(dataCloud=cloudQuality)
con3 = ConsequentType()
con3.addThenClause(variable=tip, term=generous)
rule3.setAnYaAntecedent(ant3)
rule3.setConsequent(con3)
rb.addAnYaRule(rule3)

tipper.addRuleBase(rb)

#WRITTING TIPPER EXAMPLE INTO AN XML FILE
str_xml = "XMLFiles/TipperAnYa.xml"
Py4jfml.writeFSTtoXML(tipper, str_xml)

print(tipper)
