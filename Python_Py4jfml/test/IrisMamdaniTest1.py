import py4jfml.Py4jfml as fml
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()


#FuzzyInference
iris = fml.FuzzyInferenceSystem("iris - MAMDANI")
#KnowledgeBase
kb = fml.KnowledgeBaseType()
iris.setKnowledgeBase(kb)

#FUZZY VARIABLE PetalWidth
pw = fml.FuzzyVariableType("PetalWidth", 0.1, 2.5)

#FUZZY TERM low
pw_low = fml.FuzzyTermType("low", fml.FuzzyTerm.TYPE_trapezoidShape, [0.1, 0.1, 0.244, 1.087])
pw.addFuzzyTerm(pw_low)

#FUZZY TERM medium
pw_medium = fml.FuzzyTermType("medium", fml.FuzzyTerm.TYPE_trapezoidShape, [0.244, 1.087, 1.419, 1.906])
pw.addFuzzyTerm(pw_medium)

#FUZZY TERM high
pw_high = fml.FuzzyTermType("high", fml.FuzzyTerm.TYPE_trapezoidShape, [1.419, 1.906, 2.5, 2.5])
pw.addFuzzyTerm(pw_high)

kb.addVariable(pw)

#OUTPUT CLASS irisClass
irisClass = fml.FuzzyVariableType("irisClass", 1., 3.)
irisClass.setDefaultValue(1.)
irisClass.setAccumulation("MAX")
irisClass.setDefuzzifierName("MOM")
irisClass.setType("output")

#FUZZY TERM setosa
irisClass_setosa = fml.FuzzyTermType("setosa", fml.FuzzyTerm.TYPE_triangularShape, [1., 1., 2.])
irisClass.addFuzzyTerm(irisClass_setosa)

#FUZZY TERM virginica
irisClass_virginica = fml.FuzzyTermType("virginica", fml.FuzzyTerm.TYPE_triangularShape, [1., 2., 3.])
irisClass.addFuzzyTerm(irisClass_virginica)

#FUZZY TERM versicolor
irisClass_versicolor = fml.FuzzyTermType("versicolor", fml.FuzzyTerm.TYPE_triangularShape, [2., 3., 3.])
irisClass.addFuzzyTerm(irisClass_versicolor)

kb.addVariable(irisClass)

#RULE BASE
rb = fml.MamdaniRuleBaseType("rulebase-iris")

#RULE 1
r1 = fml.FuzzyRuleType("rule1", "and", "MIN", 1.0)

#aggiunta regole antecedenti
ant1 = fml.AntecedentType()
ant1.addClause(fml.ClauseType(pw, pw_low))

#aggiunta regole conseguenti
con1 = fml.ConsequentType()
con1.addThenClause(fml.ClauseType(irisClass, irisClass_setosa))
r1.setAntecedent(ant1)
r1.setConsequent(con1)

rb.addRule(r1)

#RULE 2
r2 = fml.FuzzyRuleType("rule2", "and", "MIN", 1.0)
ant2 = fml.AntecedentType()
ant2.addClause(fml.ClauseType(pw, pw_medium))
con2 = fml.ConsequentType()
con2.addThenClause(fml.ClauseType(irisClass, irisClass_virginica))
r2.setAntecedent(ant2)
r2.setConsequent(con2)

rb.addRule(r2)

#RULE 3
r3 = fml.FuzzyRuleType("rule3", "and", "MIN", 1.0)
ant3 = fml.AntecedentType()
ant3.addClause(fml.ClauseType(pw, pw_high))
con3 = fml.ConsequentType()
con3.addThenClause(fml.ClauseType(irisClass, irisClass_versicolor))
r3.setAntecedent(ant3)
r3.setConsequent(con3)

rb.addRule(r3)

iris.addRuleBase(rb)

#WRITTING IRIS EXAMPLE INTO AN XML FILE
str_xml = "C:\\Users\\andrea\\PycharmProjects\\untitled\\Python_Py4jfml\\XMLFiles\\IrisMamdani1.xml"
fml.PY4JFML.writeFSTtoXML(iris,str_xml)


