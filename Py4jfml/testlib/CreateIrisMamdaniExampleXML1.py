'''
This class creates an XML file with the definition of a Mamdani-type FLS for the Iris classification problem:
 *   1) One input variable (PetalWidth) with Trapezoidal membership functions
 *   2) Three rules (one per output class)
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

iris = FuzzyInferenceSystem("iris - MAMDANI")

#KNOWLEDGE BASE
kb = KnowledgeBaseType()
iris.setKnowledgeBase(kb)

#FUZZY VARIABLE PetalWidth
pw = FuzzyVariableType(name="PetalWidth", domainLeft=0.1, domainRight=2.5)

#FUZZY TERM low
pw_low = FuzzyTermType(name="low", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[0.1, 0.1, 0.244, 1.087])
pw.addFuzzyTerm(pw_low)

#FUZZY TERM medium
pw_medium = FuzzyTermType(name="medium", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[0.244, 1.087, 1.419, 1.906])
pw.addFuzzyTerm(pw_medium)

#FUZZY TERM high
pw_high = FuzzyTermType(name="high", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[1.419, 1.906, 2.5, 2.5])
pw.addFuzzyTerm(pw_high)

kb.addVariable(pw)

#OUTPUT CLASS irisClass
irisClass = FuzzyVariableType(name="irisClass", domainLeft=1.0, domainRight=3.0)
irisClass.setDefaultValue(value=1.0)
irisClass.setAccumulation(value="MAX")
irisClass.setDefuzzifierName(value="MOM")
irisClass.setType(value="output")

#FUZZY TERM setosa
irisClass_setosa = FuzzyTermType(name="setosa", type_java=FuzzyTermType.TYPE_triangularShape, param=[1.0, 1.0, 2.0])
irisClass.addFuzzyTerm(ft=irisClass_setosa)

#FUZZY TERM virginica
irisClass_virginica = FuzzyTermType(name="virginica", type_java=FuzzyTermType.TYPE_triangularShape, param=[1.0, 2.0, 3.0])
irisClass.addFuzzyTerm(irisClass_virginica)

#FUZZY TERM versicolor
irisClass_versicolor = FuzzyTermType(name="versicolor", type_java=FuzzyTermType.TYPE_triangularShape, param=[2.0, 3.0, 3.0])
irisClass.addFuzzyTerm(irisClass_versicolor)

kb.addVariable(irisClass)

#RULE BASE
rb =MamdaniRuleBaseType("rulebase-iris")

#RULE 1
r1 =FuzzyRuleType(name="rule1", connector="and", connectorMethod="MIN", weight=1.0)

ant1 = AntecedentType()
ant1.addClause(c=ClauseType(pw, pw_low))
con1 = ConsequentType()
con1.addThenClause(variable=irisClass, term=irisClass_setosa)
r1.setAntecedent(value=ant1)
r1.setConsequent(value=con1)

rb.addRule(r1)

#RULE 2
r2 = FuzzyRuleType(name="rule2", connector="and", connectorMethod="MIN", weight=1.0)

ant2 = AntecedentType()
ant2.addClause(c=ClauseType(pw, pw_medium))
con2 = ConsequentType()
con2.addThenClause(variable=irisClass, term=irisClass_virginica)
r2.setAntecedent(value=ant2)
r2.setConsequent(value=con2)

rb.addRule(r2)

#RULE 3
r3 = FuzzyRuleType(name="rule3", connector="and", connectorMethod="MIN", weight=1.0)

ant3 = AntecedentType()
ant3.addClause(c=ClauseType(pw, pw_high))
con3 = ConsequentType()
con3.addThenClause(variable=irisClass, term=irisClass_versicolor)
r3.setAntecedent(value=ant3)
r3.setConsequent(value=con3)

rb.addRule(r3)

iris.addRuleBase(rb)

#WRITTING IRIS EXAMPLE INTO AN XML FILE
irisXMLFile = "XMLFiles/IrisMamdani1.xml"
Py4jfml.writeFSTtoXML(iris, irisXMLFile)

print(iris)