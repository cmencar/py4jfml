'''
 This class creates an XML file with the definition of a Mamdani-type FLS for the Iris classification problem:
     1) Four input variables (SepalLength, SepalWith, PetalLength and PetalWidth) with Triangular and Trapezoidal membership functions
     2) Three rules (one per output class)
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
from py4jfml.term.FuzzyTerm import FuzzyTerm
from py4jfml.term.FuzzyTermType import FuzzyTermType

# FuzzyInference
iris = FuzzyInferenceSystem("iris - MAMDANI")

# KnowledgeBase
kb = KnowledgeBaseType()
iris.setKnowledgeBase(kb)

# FUZZY VARIABLE SepalLength
sl = FuzzyVariableType("SepalLength", 4.3, 7.9)

# FUZZY TERM low
sl_low = FuzzyTermType("low", FuzzyTerm.TYPE_trapezoidShape, [4.3, 4.3, 5.019, 6.048])
sl.addFuzzyTerm(sl_low)

# FUZZY TERM  medium
sl_medium = FuzzyTermType("medium", FuzzyTerm.TYPE_triangularShape, [5.019, 6.048, 7.05])
sl.addFuzzyTerm(sl_medium)

# FUZZY TERM high
sl_high = FuzzyTermType("high", FuzzyTerm.TYPE_trapezoidShape, [6.048, 7.05, 7.9, 7.9])
sl.addFuzzyTerm(sl_high)

# FUZZY TERM NOT(low)
sl_not_low = FuzzyTermType("NOT(low)", FuzzyTerm.TYPE_trapezoidShape, [4.3, 4.3, 5.019, 6.048])
sl_not_low.setComplement("true")
sl.addFuzzyTerm(sl_not_low)

kb.addVariable(sl)

# FUZZY VARIABLE SepalWidth
sw = FuzzyVariableType("SepalWidth", 2., 4.4)

# FUZZY TERM low
sw_low = FuzzyTermType("low", FuzzyTerm.TYPE_trapezoidShape, [2., 2., 2.585, 3.119])
sw.addFuzzyTerm(sw_low)

# FUZZY TERM medium
sw_medium = FuzzyTermType("medium", FuzzyTerm.TYPE_triangularShape, [2.585, 3.119, 3.758])
sw.addFuzzyTerm(sw_medium)

# FUZZY TERM high
sw_high = FuzzyTermType("high", FuzzyTerm.TYPE_trapezoidShape, [3.119, 3.758, 4.4, 4.4])
sw.addFuzzyTerm(sw_high)

# FUZZY TERM NOT(high)
sw_not_high = FuzzyTermType("NOT(high)", FuzzyTerm.TYPE_trapezoidShape, [3.119, 3.758, 4.4, 4.4])
sw_not_high.setComplement("true")
sw.addFuzzyTerm(sw_not_high)

kb.addVariable(sw)

# FUZZY VARIABLE PetalLength
pl = FuzzyVariableType("PetalLength", 1., 6.9)

# FUZZY TERM low
pl_low = FuzzyTermType("low", FuzzyTerm.TYPE_trapezoidShape, [1., 1., 1.464, 4.432])
pl.addFuzzyTerm(pl_low);
# FUZZY TERM medium
pl_medium = FuzzyTermType("medium", FuzzyTerm.TYPE_triangularShape, [1.464, 4.432, 5.826])
pl.addFuzzyTerm(pl_medium)
# FUZZY TERM high
pl_high = FuzzyTermType("high", FuzzyTerm.TYPE_trapezoidShape, [4.432, 5.826, 6.9, 6.9])
pl.addFuzzyTerm(pl_high)
# FUZZY TERM NOT(low)
pl_not_low = FuzzyTermType("NOT(low)", FuzzyTerm.TYPE_trapezoidShape, [1., 1., 1.464, 4.432])

pl_not_low.setComplement("true")
pl.addFuzzyTerm(pl_not_low)

kb.addVariable(pl)

# FUZZY VARIABLE PetalWidth
pw = FuzzyVariableType("PetalWidth", 0.1, 2.5)

# FUZZY TERM low
pw_low = FuzzyTermType("low", FuzzyTerm.TYPE_trapezoidShape, [0., 0.1, 0.244, 1.337])
pw.addFuzzyTerm(pw_low)

# FUZZY TERM medium
pw_medium = FuzzyTermType("medium", FuzzyTerm.TYPE_triangularShape, [0.244, 1.337, 2.074])
pw.addFuzzyTerm(pw_medium)

# FUZZY TERM high
pw_high = FuzzyTermType("high", FuzzyTerm.TYPE_trapezoidShape, [1.337, 2.074, 2.5, 2.5])
pw.addFuzzyTerm(pw_high)

kb.addVariable(pw)

# OUTPUT CLASS irisClass
irisClass = FuzzyVariableType("irisClass", 1.0, 3.0)
irisClass.setDefaultValue(1.)
irisClass.setAccumulation("MAX")
irisClass.setDefuzzifierName("LM")
irisClass.setType("output")

# FUZZY TERM setosa
irisClass_setosa = FuzzyTermType("setosa", FuzzyTerm.TYPE_singletonShape, [1.0])
irisClass.addFuzzyTerm(irisClass_setosa);

# FUZZY TERM virginica
irisClass_virginica = FuzzyTermType("virginica", FuzzyTerm.TYPE_singletonShape, [2.0])
irisClass.addFuzzyTerm(irisClass_virginica)

# FUZZY TERM versicolor
irisClass_versicolor = FuzzyTermType("versicolor", FuzzyTerm.TYPE_singletonShape, [3.0])
irisClass.addFuzzyTerm(irisClass_versicolor)

kb.addVariable(irisClass)

# RULE BASE
rb = MamdaniRuleBaseType("rulebase-iris")

# RULE 1
r1 = FuzzyRuleType("rule1", connector="and", connectorMethod="MIN", weight=1.0)
ant1 = AntecedentType()
ant1.addClause(ClauseType(pw, pw_low))
con1 = ConsequentType()
con1.addThenClause(ClauseType(irisClass, irisClass_setosa))
r1.setAntecedent(ant1)
r1.setConsequent(con1)

rb.addRule(r1)

# RULE 2
r2 = FuzzyRuleType("rule2", connector="and", connectorMethod="MIN", weight=1.0)
ant2 = AntecedentType()
ant2.addClause(ClauseType(sw, sw_not_high))
ant2.addClause(ClauseType(pl, pl_medium))
ant2.addClause(ClauseType(pw, pw_medium))
con2 = ConsequentType()
con2.addThenClause(ClauseType(irisClass, irisClass_virginica))
r2.setAntecedent(ant2)
r2.setConsequent(con2)

rb.addRule(r2);

# RULE 3
r3 = FuzzyRuleType("rule3", connector="and", connectorMethod="MIN", weight=1.0)
ant3 = AntecedentType()
ant3.addClause(ClauseType(sl, sl_not_low))
ant3.addClause(ClauseType(pl, pl_not_low))
ant3.addClause(ClauseType(pw, pw_high))
con3 = ConsequentType()
con3.addThenClause(ClauseType(irisClass, irisClass_versicolor))
r3.setAntecedent(ant3)
r3.setConsequent(con3)

rb.addRule(r3)

iris.addRuleBase(rb)

print(iris)

# WRITTING IRIS EXAMPLE INTO AN XML FILE
irisXMLFile = "XMLFiles/IrisMamdani2.xml"
Py4jfml.writeFSTtoXML(iris, irisXMLFile)

Py4jfml.kill()