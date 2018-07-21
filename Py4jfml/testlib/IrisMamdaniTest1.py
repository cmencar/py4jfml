from py4jfml.FuzzyInferenceSystem import *
from py4jfml.knowledgebase.KnowledgeBaseType import *
from py4jfml.term.FuzzyTerm import *
from py4jfml.rulebase.MamdaniRuleBaseType import *
from py4jfml.rule.ConsequentType import *
import py4jfml.Py4Jfml as fml

gateway = JavaGateway()

#FuzzyInference
iris = FuzzyInferenceSystem("iris - MAMDANI")
#KnowledgeBase
kb = KnowledgeBaseType()
iris.setKnowledgeBase(kb)

#FUZZY VARIABLE PetalWidth
pw = FuzzyVariableType("PetalWidth", 0.1, 2.5)

#FUZZY TERM low
pw_low = FuzzyTermType("low", FuzzyTerm.TYPE_trapezoidShape, [0.1, 0.1, 0.244, 1.087])
pw.addFuzzyTerm(pw_low)

#FUZZY TERM medium
pw_medium = FuzzyTermType("medium", FuzzyTerm.TYPE_trapezoidShape, [0.244, 1.087, 1.419, 1.906])
pw.addFuzzyTerm(pw_medium)

#FUZZY TERM high
pw_high = FuzzyTermType("high", FuzzyTerm.TYPE_trapezoidShape, [1.419, 1.906, 2.5, 2.5])
pw.addFuzzyTerm(pw_high)

kb.addVariable(pw)

#OUTPUT CLASS irisClass
irisClass = FuzzyVariableType("irisClass", 1., 3.)
irisClass.setDefaultValue(1.)
irisClass.setAccumulation("MAX")
irisClass.setDefuzzifierName("MOM")
irisClass.setType("output")

#FUZZY TERM setosa
irisClass_setosa = FuzzyTermType("setosa", FuzzyTerm.TYPE_triangularShape, [1., 1., 2.])
irisClass.addFuzzyTerm(irisClass_setosa)

#FUZZY TERM virginica
irisClass_virginica = FuzzyTermType("virginica", FuzzyTerm.TYPE_triangularShape, [1., 2., 3.])
irisClass.addFuzzyTerm(irisClass_virginica)

#FUZZY TERM versicolor
irisClass_versicolor = FuzzyTermType("versicolor", FuzzyTerm.TYPE_triangularShape, [2., 3., 3.])
irisClass.addFuzzyTerm(irisClass_versicolor)

kb.addVariable(irisClass)

#RULE BASE
rb = MamdaniRuleBaseType("rulebase-iris")

#RULE 1
r1 = FuzzyRuleType("rule1", None, None, "and", "MIN", None, None, 1.0)

#aggiunta regole antecedenti
ant1 = AntecedentType()
ant1.addClause(ClauseType(pw, pw_low))

#aggiunta regole conseguenti
con1 = ConsequentType()
con1.addThenClause(ClauseType(irisClass, irisClass_setosa))
r1.setAntecedent(ant1)
r1.setConsequent(con1)

rb.addRule(r1)

#RULE 2
r2 = FuzzyRuleType("rule2", None, None, "and", "MIN", None, None, 1.0)
ant2 = AntecedentType()
ant2.addClause(ClauseType(pw, pw_medium))
con2 = ConsequentType()
con2.addThenClause(ClauseType(irisClass, irisClass_virginica))
r2.setAntecedent(ant2)
r2.setConsequent(con2)

rb.addRule(r2)

#RULE 3
r3 = FuzzyRuleType("rule3", None, None, "and", "MIN", None, None, 1.0)
ant3 = AntecedentType()
ant3.addClause(ClauseType(pw, pw_high))
con3 = ConsequentType()
con3.addThenClause(ClauseType(irisClass, irisClass_versicolor))
r3.setAntecedent(ant3)
r3.setConsequent(con3)

rb.addRule(r3)

iris.addRuleBase(rb)

#WRITTING IRIS EXAMPLE INTO AN XML FILE
str_xml = "XMLFiles/IrisMamdani1.xml"
fml.Py4jfml.writeFSTtoXML(iris, str_xml)


