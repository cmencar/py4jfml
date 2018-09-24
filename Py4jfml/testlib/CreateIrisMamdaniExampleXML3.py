'''
This class creates an XML file with the definition of a Mamdani-type FLS for the Iris classification problem:
 *   1) 1 input variable (PetalWidth) with 12 different membership functions
 *   2) 12 rules (4 per output class, 1 per membership function in the input variable)
'''

from py4j.java_gateway import JavaGateway
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

gateway = JavaGateway()


iris = FuzzyInferenceSystem("iris - MAMDANI")

#KNOWLEDGEBASE
kb = KnowledgeBaseType()
iris.setKnowledgeBase(kb)

#FUZZY VARIABLE PetalWidth
pw = FuzzyVariableType(name="PetalWidth", domainLeft=0.1, domainRight=2.5)

#FUZZY TERM low
pw_lowLIN = FuzzyTermType(name="lowLIN", type_java=FuzzyTerm.TYPE_leftLinearShape, param=[0., 0.8])
pw.addFuzzyTerm(pw_lowLIN)

#lowGAU
pw_lowGAU = FuzzyTermType(name="lowGAU", type_java=FuzzyTerm.TYPE_leftGaussianShape, param=[0.5, 0.2])
pw.addFuzzyTerm(pw_lowGAU)
#lowPI
pw_lowPi = FuzzyTermType(name="lowPi", type_java=FuzzyTerm.TYPE_piShape, param=[1., 1.2])
pw.addFuzzyTerm(pw_lowPi)
#lowZ
pw_lowZ = FuzzyTermType(name="lowZ", type_java=FuzzyTerm.TYPE_zShape, param=[1., 0.2])
pw.addFuzzyTerm(pw_lowZ)

#FUZZY TERM medium TRI
pw_mediumTRI = FuzzyTermType(name="mediumTRI", type_java=FuzzyTerm.TYPE_triangularShape, param=[0.5, 1., 1.5])
pw.addFuzzyTerm(pw_mediumTRI)
#TRA
pw_mediumTRA = FuzzyTermType(name="mediumTRA", type_java=FuzzyTerm.TYPE_trapezoidShape, param=[0.25, 1., 2., 2.25])
pw.addFuzzyTerm(pw_mediumTRA)
#GAU
pw_mediumGAU = FuzzyTermType(name="mediumGAU", type_java=FuzzyTerm.TYPE_gaussianShape, param=[1., 0.2])
pw.addFuzzyTerm(pw_mediumGAU)
#REC
pw_mediumREC = FuzzyTermType(name="mediumREC", type_java=FuzzyTerm.TYPE_rectangularShape, param=[1., 2.])
pw.addFuzzyTerm(pw_mediumREC)

#FUZZY TERM high LIN
pw_highLIN = FuzzyTermType(name="highLIN", type_java=FuzzyTerm.TYPE_rightLinearShape, param=[1.5, 2.5])
pw.addFuzzyTerm(pw_highLIN)
#GAU
pw_highGAU = FuzzyTermType(name="highGAU", type_java=FuzzyTerm.TYPE_rightGaussianShape, param=[2., 0.2])
pw.addFuzzyTerm(pw_highGAU)
#SIN
pw_highSIN = FuzzyTermType(name="highSIN", type_java=FuzzyTerm.TYPE_singletonShape, param=[2.0])
pw.addFuzzyTerm(pw_highSIN)
pw_highS = FuzzyTermType(name="highS", type_java=FuzzyTerm.TYPE_sShape, param=[2., 0.2])
pw.addFuzzyTerm(pw_highS)

kb.addVariable(pw)

#OUTPUT CLASS irisClass
irisClass = FuzzyVariableType(name="irisClass", domainLeft=1., domainRight=3.)
irisClass.setDefaultValue(1.)
irisClass.setAccumulation("MAX")
irisClass.setDefuzzifierName("LM")
irisClass.setType("output")

#FUZZY TERM setosa
irisClass_setosa = FuzzyTermType(name="setosa", type_java=FuzzyTerm.TYPE_singletonShape, param=[1.])
irisClass.addFuzzyTerm(irisClass_setosa)

#FUZZY TERM  virginica
irisClass_virginica = FuzzyTermType(name="virginica",type_java= FuzzyTerm.TYPE_singletonShape, param=[2.])
irisClass.addFuzzyTerm(irisClass_virginica)

#FUZZY TERM versicolor
irisClass_versicolor = FuzzyTermType(name="versicolor", type_java=FuzzyTerm.TYPE_singletonShape, param=[3.])
irisClass.addFuzzyTerm(irisClass_versicolor)

kb.addVariable(irisClass)

#RULE BASE
rb = MamdaniRuleBaseType("rulebase-iris")

#RULE 1
r1 = FuzzyRuleType(name="rule1",connector="and", connectorMethod="MIN",weight=1.0)

ant1 = AntecedentType()
ant1.addClause(c=ClauseType(pw, pw_lowLIN))
con1 = ConsequentType()
con1.addThenClause(c=ClauseType(variable=irisClass, term=irisClass_setosa))
r1.setAntecedent(value=ant1)
r1.setConsequent(value=con1)
rb.addRule(r1)

#RULE 2
r2 = FuzzyRuleType("rule2",connector="and", connectorMethod="MIN", weight=1.0)
ant2 = AntecedentType()
ant2.addClause(c=ClauseType(pw, pw_lowGAU))
con2 = ConsequentType()
con2.addThenClause(c=ClauseType(irisClass, irisClass_setosa))
r2.setAntecedent(value=ant2)
r2.setConsequent(value=con2)
rb.addRule(r2)

#RULE 3
r3 = FuzzyRuleType(name="rule3",connector="and", connectorMethod="MIN", weight=1.0)
ant3 = AntecedentType()
ant3.addClause(c=ClauseType(pw, pw_lowPi))
con3 = ConsequentType()
con3.addThenClause(c=ClauseType(irisClass, irisClass_setosa))
r3.setAntecedent(value=ant3)
r3.setConsequent(value=con3)
rb.addRule(r3)

#RULE 4
r4 = FuzzyRuleType(name="rule4", connector="and", connectorMethod="MIN", weight=1.0)
ant4 = AntecedentType()
ant4.addClause(c=ClauseType(pw, pw_lowZ))
con4 = ConsequentType()
con4.addThenClause(c=ClauseType(irisClass, irisClass_setosa))
r4.setAntecedent(value=ant4)
r4.setConsequent(value=con4)
rb.addRule(r4)

#RULE 5
r5 = FuzzyRuleType(name="rule5", connector="and", connectorMethod="MIN", weight=1.0)
ant5 = AntecedentType()
ant5.addClause(c=ClauseType(pw, pw_mediumTRI))
con5 = ConsequentType()
con5.addThenClause(c=ClauseType(irisClass, irisClass_virginica))
r5.setAntecedent(value=ant5)
r5.setConsequent(value=con5)
rb.addRule(r5)

#RULE 6
r6 = FuzzyRuleType(name="rule6",connector="and", connectorMethod="MIN",weight=1.0)
ant6 = AntecedentType()
ant6.addClause(c=ClauseType(pw, pw_mediumTRA))
con6 = ConsequentType()
con6.addThenClause(c=ClauseType(irisClass, irisClass_virginica))
r6.setAntecedent(value=ant6)
r6.setConsequent(value=con6)
rb.addRule(r6)

#RULE 7
r7 = FuzzyRuleType(name="rule7",connector="and", connectorMethod="MIN", weight=1.0)
ant7 = AntecedentType()
ant7.addClause(c=ClauseType(pw, pw_mediumGAU))
con7 = ConsequentType()
con7.addThenClause(c=ClauseType(irisClass, irisClass_virginica))
r7.setAntecedent(value=ant7)
r7.setConsequent(value=con7)
rb.addRule(r7)

#RULE 8
r8 = FuzzyRuleType(name="rule8", connector="and", connectorMethod="MIN", weight=1.0)
ant8 = AntecedentType()
ant8.addClause(c=ClauseType(pw, pw_mediumREC))
con8 = ConsequentType()
con8.addThenClause(c=ClauseType(irisClass, irisClass_virginica))
r8.setAntecedent(value=ant8)
r8.setConsequent(value=con8)
rb.addRule(r8)

#RULE 9
r9 = FuzzyRuleType(name="rule9", connector="and", connectorMethod="MIN", weight=1.0)
ant9 = AntecedentType()
ant9.addClause(c=ClauseType(pw, pw_highLIN))
con9 = ConsequentType()
con9.addThenClause(c=ClauseType(irisClass, irisClass_versicolor))
r9.setAntecedent(value=ant9)
r9.setConsequent(value=con9)
rb.addRule(r9)

#RULE 10
r10 = FuzzyRuleType(name="rule10", connector="and", connectorMethod="MIN", weight=1.0)
ant10 = AntecedentType()
ant10.addClause(c=ClauseType(pw, pw_highGAU))
con10 = ConsequentType()
con10.addThenClause(c=ClauseType(irisClass, irisClass_versicolor))
r10.setAntecedent(value=ant10)
r10.setConsequent(value=con10)
rb.addRule(r10)

#RULE 11
r11 = FuzzyRuleType(name="rule11", connector="and", connectorMethod="MIN", weight=1.0)
ant11 = AntecedentType()
ant11.addClause(c=ClauseType(pw, pw_highSIN))
con11 = ConsequentType()
con11.addThenClause(c=ClauseType(irisClass, irisClass_versicolor))
r11.setAntecedent(value=ant11)
r11.setConsequent(value=con11)
rb.addRule(r11)

# RULE 12
r12 = FuzzyRuleType(name="rule12",connector="and", connectorMethod="MIN", weight=1.0)
ant12 = AntecedentType()
ant12.addClause(c=ClauseType(pw, pw_highS))
con12 = ConsequentType()
con12.addThenClause(c=ClauseType(irisClass, irisClass_versicolor))
r12.setAntecedent(value=ant12)
r12.setConsequent(value=con12)
rb.addRule(r12)

iris.addRuleBase(rb)

# WRITTING IRIS EXAMPLE INTO AN XML FILE
str_xml = "XMLFiles/IrisMamdani3.xml"
Py4jfml.writeFSTtoXML(iris, str_xml)

print(iris)