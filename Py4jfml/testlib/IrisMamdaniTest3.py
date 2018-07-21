from py4jfml.FuzzyInferenceSystem import *
from py4jfml.knowledgebase.KnowledgeBaseType import *
from py4jfml.term.FuzzyTerm import *
from py4jfml.rulebase.MamdaniRuleBaseType import *
from py4jfml.rule.ConsequentType import *
import py4jfml.Py4Jfml as fml

from py4j.java_gateway import JavaGateway

gateway = JavaGateway()


iris = FuzzyInferenceSystem("iris - MAMDANI")

# KNOWLEDGEBASE
kb = KnowledgeBaseType()
iris.setKnowledgeBase(kb)

# FUZZY VARIABLE PetalWidth
pw = FuzzyVariableType("PetalWidth", 0.1, 2.5)

# FUZZY TERM low
pw_lowLIN = FuzzyTermType("lowLIN", FuzzyTerm.TYPE_leftLinearShape, [0., 0.8])
pw.addFuzzyTerm(pw_lowLIN)

# lowGAU
pw_lowGAU = FuzzyTermType("lowGAU", FuzzyTerm.TYPE_leftGaussianShape,[0.5, 0.2])
pw.addFuzzyTerm(pw_lowGAU)
# lowPI
pw_lowPi = FuzzyTermType("lowPi", FuzzyTerm.TYPE_piShape, [1., 1.2])
pw.addFuzzyTerm(pw_lowPi)
# lowZ
pw_lowZ = FuzzyTermType("lowZ", FuzzyTerm.TYPE_zShape, [1., 0.2])
pw.addFuzzyTerm(pw_lowZ)

# FUZZY TERM medium TRI
pw_mediumTRI = FuzzyTermType("mediumTRI", FuzzyTerm.TYPE_triangularShape,[0.5, 1., 1.5])
pw.addFuzzyTerm(pw_mediumTRI)
# TRA
pw_mediumTRA = FuzzyTermType("mediumTRA", FuzzyTerm.TYPE_trapezoidShape, [0.25, 1., 2., 2.25])
pw.addFuzzyTerm(pw_mediumTRA)
# GAU
pw_mediumGAU = FuzzyTermType("mediumGAU", FuzzyTerm.TYPE_gaussianShape, [1., 0.2])
pw.addFuzzyTerm(pw_mediumGAU)
# REC
pw_mediumREC = FuzzyTermType("mediumREC", FuzzyTerm.TYPE_rectangularShape, [1., 2.])
pw.addFuzzyTerm(pw_mediumREC)

# FUZZY TERM high LIN
pw_highLIN = FuzzyTermType("highLIN", FuzzyTerm.TYPE_rightLinearShape, [1.5, 2.5])
pw.addFuzzyTerm(pw_highLIN)
# GAU
pw_highGAU = FuzzyTermType("highGAU", FuzzyTerm.TYPE_rightGaussianShape, [2., 0.2])
pw.addFuzzyTerm(pw_highGAU)
# SIN
pw_highSIN = FuzzyTermType("highSIN", FuzzyTerm.TYPE_singletonShape, [2.])
pw.addFuzzyTerm(pw_highSIN)
pw_highS = FuzzyTermType("highS", FuzzyTerm.TYPE_sShape, [2., 0.2])
pw.addFuzzyTerm(pw_highS)

kb.addVariable(pw)

# OUTPUT CLASS irisClass
irisClass = FuzzyVariableType("irisClass", 1., 3.)
irisClass.setDefaultValue(1.)
irisClass.setAccumulation("MAX")
irisClass.setDefuzzifierName("LM")
irisClass.setType("output")

# FUZZY TERM setosa
irisClass_setosa = FuzzyTermType("setosa", FuzzyTerm.TYPE_singletonShape, [1.])
irisClass.addFuzzyTerm(irisClass_setosa)

# FUZZY TERM  virginica
irisClass_virginica = FuzzyTermType("virginica", FuzzyTerm.TYPE_singletonShape, [2.])
irisClass.addFuzzyTerm(irisClass_virginica)

# FUZZY TERM versicolor
irisClass_versicolor = FuzzyTermType("versicolor", FuzzyTerm.TYPE_singletonShape, [3.])
irisClass.addFuzzyTerm(irisClass_versicolor)

kb.addVariable(irisClass)

# RULE BASE
rb = MamdaniRuleBaseType("rulebase-iris")

# RULE 1
r1 = FuzzyRuleType("rule1", None, None, "and", "MIN", None, None, 1.0)

#regole antecendenti
ant1 = AntecedentType()
ant1.addClause(ClauseType(pw, pw_lowLIN))
#regole conseguenti
con1 = ConsequentType()
con1.addThenClause(ClauseType(irisClass, irisClass_setosa))

r1.setAntecedent(ant1)
r1.setConsequent(con1)

rb.addRule(r1)

# RULE 2
r2 = FuzzyRuleType("rule2", None, None, "and", "MIN", None, None, 1.0)

ant2 = AntecedentType()
ant2.addClause(ClauseType(pw, pw_lowGAU))

con2 = ConsequentType()
con2.addThenClause(ClauseType(irisClass, irisClass_setosa))
r2.setAntecedent(ant2)
r2.setConsequent(con2)
rb.addRule(r2)

# RULE 3
r3 = FuzzyRuleType("rule3", None, None, "and", "MIN", None, None, 1.0)

ant3 = AntecedentType()
ant3.addClause(ClauseType(pw, pw_lowPi))

con3 = ConsequentType()
con3.addThenClause(ClauseType(irisClass, irisClass_setosa))

r3.setAntecedent(ant3)
r3.setConsequent(con3)
rb.addRule(r3)

# RULE 4
r4 = FuzzyRuleType("rule4", None, None, "and", "MIN", None, None, 1.0)

ant4 = AntecedentType()
ant4.addClause(ClauseType(pw, pw_lowZ))

con4 = ConsequentType()
con4.addThenClause(ClauseType(irisClass, irisClass_setosa))

r4.setAntecedent(ant4)
r4.setConsequent(con4)

rb.addRule(r4)

# RULE 5
r5 = FuzzyRuleType("rule5", None, None, "and", "MIN", None, None, 1.0)

ant5 = AntecedentType()
ant5.addClause(ClauseType(pw, pw_mediumTRI))

con5 = ConsequentType()
con5.addThenClause(ClauseType(irisClass, irisClass_virginica))

r5.setAntecedent(ant5)
r5.setConsequent(con5)

rb.addRule(r5)

# RULE 6
r6 = FuzzyRuleType("rule6", None, None, "and", "MIN", None, None, 1.0)

ant6 = AntecedentType()
ant6.addClause(ClauseType(pw, pw_mediumTRA))

con6 = ConsequentType()
con6.addThenClause(ClauseType(irisClass, irisClass_virginica))

r6.setAntecedent(ant6)
r6.setConsequent(con6)

rb.addRule(r6)

# RULE 7
r7 = FuzzyRuleType("rule7", None, None, "and", "MIN", None, None, 1.0)

ant7 = AntecedentType()
ant7.addClause(ClauseType(pw, pw_mediumGAU))

con7 = ConsequentType()
con7.addThenClause(ClauseType(irisClass, irisClass_virginica))

r7.setAntecedent(ant7)
r7.setConsequent(con7)

rb.addRule(r7)

# RULE 8
r8 = FuzzyRuleType("rule8", None, None, "and", "MIN", None, None, 1.0)

ant8 = AntecedentType()
ant8.addClause(ClauseType(pw, pw_mediumREC))

con8 = ConsequentType()
con8.addThenClause(ClauseType(irisClass, irisClass_virginica))
r8.setAntecedent(ant8)
r8.setConsequent(con8)
rb.addRule(r8)

# RULE 9
r9 = FuzzyRuleType("rule9", None, None, "and", "MIN", None, None, 1.0)

ant9 = AntecedentType()
ant9.addClause(ClauseType(pw, pw_highLIN))

con9 = ConsequentType()
con9.addThenClause(ClauseType(irisClass, irisClass_versicolor))

r9.setAntecedent(ant9)
r9.setConsequent(con9)

rb.addRule(r9)

# RULE 10
r10 = FuzzyRuleType("rule10", None, None, "and", "MIN", None, None, 1.0)
ant10 = AntecedentType()
ant10.addClause(ClauseType(pw, pw_highGAU))

con10 = ConsequentType()
con10.addThenClause(ClauseType(irisClass, irisClass_versicolor))

r10.setAntecedent(ant10)
r10.setConsequent(con10)

rb.addRule(r10)

# RULE 11
r11 = FuzzyRuleType("rule11", None, None, "and", "MIN", None, None, 1.0)

ant11 = AntecedentType()
ant11.addClause(ClauseType(pw, pw_highSIN))

con11 = ConsequentType()
con11.addThenClause(ClauseType(irisClass, irisClass_versicolor))

r11.setAntecedent(ant11)
r11.setConsequent(con11)
rb.addRule(r11)

# RULE 12

r12 = FuzzyRuleType("rule12", None, None, "and", "MIN", None, None, 1.0)

ant12 = AntecedentType()
ant12.addClause(ClauseType(pw, pw_highS))

con12 = ConsequentType()
con12.addThenClause(ClauseType(irisClass, irisClass_versicolor))

r12.setAntecedent(ant12)
r12.setConsequent(con12)

rb.addRule(r12)

iris.addRuleBase(rb)

# WRITTING IRIS EXAMPLE INTO AN XML FILE
str_xml = "XMLFiles/IrisMamdani3.xml"
fml.Py4jfml.writeFSTtoXML(iris, str_xml)