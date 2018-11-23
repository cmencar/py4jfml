'''
This class creates an XML file with the definition o.0a Mamdani-type FLS for the problem o.0Inverted Pendulum:
    1) Triangular and Trapezoidal membership functions
    2) Definition o.0composed linguistic terms such as "A or B" with OrLogicalType and CircularDefinitionType
    3) 19 rules
'''

from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem
from py4jfml.Py4Jfml import Py4jfml
import os

from py4jfml.knowledgebase.KnowledgeBaseType import KnowledgeBaseType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.membershipfunction.CircularDefinitionType import CircularDefinitionType
from py4jfml.operator.OrLogicalType import OrLogicalType
from py4jfml.rule.AntecedentType import AntecedentType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.rule.ConsequentType import ConsequentType
from py4jfml.rule.FuzzyRuleType import FuzzyRuleType
from py4jfml.rulebase.MamdaniRuleBaseType import MamdaniRuleBaseType
from py4jfml.term.FuzzyTermType import FuzzyTermType

invertedPendulum = FuzzyInferenceSystem("invertedPendulum - MAMDANI")

# KNOWLEDGE BASE
kb = KnowledgeBaseType()
invertedPendulum.setKnowledgeBase(kb)

# FUZZY VARIABLE
ang = FuzzyVariableType("Angle", 0.0, 255.0)

# FUZZY TERM VNEG
ang_vneg = FuzzyTermType("very negative", FuzzyTermType.TYPE_trapezoidShape, [0.0, 0.0, 48.0, 88.0])
ang.addFuzzyTerm(ang_vneg)

#FUZZY TERM NEG
ang_neg = FuzzyTermType("negative", FuzzyTermType.TYPE_triangularShape,[48.0, 88.0, 128.0])
ang.addFuzzyTerm(ang_neg)

# FUZZY TERM NEU
ang_neu = FuzzyTermType("zero", FuzzyTermType.TYPE_triangularShape,[88.0, 128.0, 168.0])
ang.addFuzzyTerm(ang_neu)

#FUZZY TERM POS
ang_pos = FuzzyTermType("positive", FuzzyTermType.TYPE_triangularShape,[128.0, 168.0, 208.0])
ang.addFuzzyTerm(ang_pos)

# FUZZY TERM VPOS
ang_vpos = FuzzyTermType("very positive", FuzzyTermType.TYPE_trapezoidShape,[168.0, 208.0, 255.0, 255.0])
ang.addFuzzyTerm(ang_vpos)

#FUZZY TERM VNEG OR NEG
ang_or1 = OrLogicalType("BSUM", "very negative", "negative")
ang_c1 = CircularDefinitionType(orLogical=ang_or1, var=ang)
ang_vneg_or_neg = FuzzyTermType("very negative or negative", circular=ang_c1)
ang.addFuzzyTerm(ang_vneg_or_neg)

#FUZZY TERM POS OR VPOS
ang_or2 = OrLogicalType("BSUM", "positive", "very positive")
ang_c2 = CircularDefinitionType(orLogical=ang_or2, var=ang)
ang_pos_or_vpos = FuzzyTermType("positive or very positive", circular=ang_c2)
ang.addFuzzyTerm(ang_pos_or_vpos)

#Adds the fuzzy variable ang to the knowledge base
kb.addVariable(ang)


#FUZZY VARIABLE ChangeAngle
ca = FuzzyVariableType("ChangeAngle", 0.0, 255.0)

#FUZZY TERM VNEG
ca_vneg = FuzzyTermType("very negative", FuzzyTermType.TYPE_trapezoidShape,[0.0, 0.0, 48.0, 88.0])
ca.addFuzzyTerm(ca_vneg)

#FUZZY TERM NEG
ca_neg = FuzzyTermType("negative", FuzzyTermType.TYPE_triangularShape,[48.0, 88.0, 128.0])
ca.addFuzzyTerm(ca_neg)

#FUZZY TERM NEU
ca_neu = FuzzyTermType("zero", FuzzyTermType.TYPE_triangularShape,[88.0, 128.0, 168.0])
ca.addFuzzyTerm(ca_neu)

#FUZZY TERM POS
ca_pos = FuzzyTermType("positive", FuzzyTermType.TYPE_triangularShape,[128.0, 168.0, 208.0])
ca.addFuzzyTerm(ca_pos)

#FUZZY TERM VPOS
ca_vpos = FuzzyTermType("very positive", FuzzyTermType.TYPE_trapezoidShape,[168.0, 208.0, 255.0, 255.0])
ca.addFuzzyTerm(ca_vpos)

#FUZZY TERM VNEG OR NEG
ca_or1 = OrLogicalType("BSUM", "very negative", "negative")
ca_c1 = CircularDefinitionType(orLogical=ca_or1, var=ca)
ca_vneg_or_neg = FuzzyTermType("very negative or negative", circular=ca_c1)
ca.addFuzzyTerm(ca_vneg_or_neg)

#FUZZY TERM POS OR VPOS
ca_or2 = OrLogicalType("BSUM", "positive", "very positive")
ca_c2 = CircularDefinitionType(orLogical=ca_or2, var=ang)
ca_pos_or_vpos = FuzzyTermType("positive or very positive", circular=ca_c2)
ca.addFuzzyTerm(ca_pos_or_vpos)

kb.addVariable(ca)


#FUZZY VARIABLE FORCE
force =  FuzzyVariableType("Force", 0.0, 255.0)
force.setDefaultValue(0.0)
force.setAccumulation("MAX")
force.setDefuzzifierName("COG")
force.setType("output")

# FUZZY TERM VNEG
force_vneg =  FuzzyTermType("very negative", FuzzyTermType.TYPE_trapezoidShape,[ 0.0, 0.0, 48.0, 88.0])
force.addFuzzyTerm(force_vneg)

# FUZZY TERM NEG
force_neg =  FuzzyTermType("negative", FuzzyTermType.TYPE_triangularShape,[ 48.0, 88.0, 128.0])
force.addFuzzyTerm(force_neg)

# FUZZY TERM NEU
force_neu =  FuzzyTermType("zero", FuzzyTermType.TYPE_triangularShape,[ 88.0, 128.0, 168.0])
force.addFuzzyTerm(force_neu)

# FUZZY TERM POS
force_pos =  FuzzyTermType("positive", FuzzyTermType.TYPE_triangularShape,[ 128.0, 168.0, 208.0])
force.addFuzzyTerm(force_pos)

# FUZZY TERM VPOS
force_vpos =  FuzzyTermType("very positive", FuzzyTermType.TYPE_trapezoidShape,[ 168.0, 208.0, 255.0, 255.0])
force.addFuzzyTerm(force_vpos)

kb.addVariable(force)


# RULE BASE
rb = MamdaniRuleBaseType("rulebase1")

# RULE1
r1 = FuzzyRuleType("rule1", connector="and", connectorMethod="MIN", weight=1.0)
ant1 = AntecedentType()
ant1.addClause(ClauseType(ang, ang_vneg_or_neg))
ant1.addClause(ClauseType(ca, ca_vneg_or_neg))
con1 = ConsequentType()
con1.addThenClause(variable=force, term=force_vneg)
r1.setAntecedent(ant1)
r1.setConsequent(con1)
rb.addRule(r1)

# RULE2
r2 = FuzzyRuleType("rule2", connector="and", connectorMethod="MIN", weight=1.0)
ant2 = AntecedentType()
ant2.addClause(ClauseType(ang, ang_vneg))
ant2.addClause(ClauseType(ca, ca_neu))
con2 = ConsequentType()
con2.addThenClause(variable=force, term=force_vneg)
r2.setAntecedent(ant2)
r2.setConsequent(con2)
rb.addRule(r2)

# RULE3
r3 = FuzzyRuleType("rule3", connector="and", connectorMethod="MIN", weight=1.0)
ant3 = AntecedentType()
ant3.addClause(ClauseType(ang, ang_vneg))
ant3.addClause(ClauseType(ca, ca_pos))
con3 = ConsequentType()
con3.addThenClause(variable=force, term=force_neg)
r3.setAntecedent(ant3)
r3.setConsequent(con3)
rb.addRule(r3)

# RULE4
r4 = FuzzyRuleType("rule4", connector="and", connectorMethod="MIN", weight=1.0)
ant4 = AntecedentType()
ant4.addClause(ClauseType(ang, ang_vneg))
ant4.addClause(ClauseType(ca, ca_vpos))
con4 = ConsequentType()
con4.addThenClause(variable=force, term=force_neu)
r4.setAntecedent(ant4)
r4.setConsequent(con4)
rb.addRule(r4)

# RULE5
r5 = FuzzyRuleType("rule5", connector="and", connectorMethod="MIN", weight=1.0)
ant5 = AntecedentType()
ant5.addClause(ClauseType(ang, ang_neg))
ant5.addClause(ClauseType(ca, ca_neu))
con5 = ConsequentType()
con5.addThenClause(variable=force, term=force_neg)
r5.setAntecedent(ant5)
r5.setConsequent(con5)
rb.addRule(r5)

# RULE6
r6 = FuzzyRuleType("rule6", connector="and", connectorMethod="MIN", weight=1.0)
ant6 = AntecedentType()
ant6.addClause(ClauseType(ang, ang_neg))
ant6.addClause(ClauseType(ca, ca_pos))
con6 = ConsequentType()
con6.addThenClause(variable=force, term=force_neu)
r6.setAntecedent(ant6)
r6.setConsequent(con6)
rb.addRule(r6)

# RULE7
r7 = FuzzyRuleType("rule7", connector="and", connectorMethod="MIN", weight=1.0)
ant7 = AntecedentType()
ant7.addClause(ClauseType(ang, ang_neg))
ant7.addClause(ClauseType(ca, ca_vpos))
con7 = ConsequentType()
con7.addThenClause(variable=force, term=force_pos)
r7.setAntecedent(ant7)
r7.setConsequent(con7)
rb.addRule(r7)

# RULE8
r8 = FuzzyRuleType("rule8", connector="and", connectorMethod="MIN", weight=1.0)
ant8 = AntecedentType()
ant8.addClause(ClauseType(ang, ang_neu))
ant8.addClause(ClauseType(ca, ca_vneg))
con8 = ConsequentType()
con8.addThenClause(variable=force, term=force_vneg)
r8.setAntecedent(ant8)
r8.setConsequent(con8)
rb.addRule(r8)

# RULE9
r9 = FuzzyRuleType("rule9", connector="and", connectorMethod="MIN", weight=1.0)
ant9 = AntecedentType()
ant9.addClause(ClauseType(ang, ang_neu))
ant9.addClause(ClauseType(ca, ca_neg))
con9 = ConsequentType()
con9.addThenClause(variable=force, term=force_neg)
r9.setAntecedent(ant9)
r9.setConsequent(con9)
rb.addRule(r9)

# RULE10
r10 = FuzzyRuleType("rule10", connector="and", connectorMethod="MIN", weight=1.0)
ant10 = AntecedentType()
ant10.addClause(
ClauseType(ang, ang_neu))
ant10.addClause(
ClauseType(ca, ca_neu))
con10 = ConsequentType()
con10.addThenClause(variable=force, term=force_neu)
r10.setAntecedent(ant10)
r10.setConsequent(con10)
rb.addRule(r10)

# RULE11
r11 = FuzzyRuleType("rule11", connector="and", connectorMethod="MIN", weight=1.0)
ant11 = AntecedentType()
ant11.addClause(ClauseType(ang, ang_neu))
ant11.addClause(ClauseType(ca, ca_pos))
con11 = ConsequentType()
con11.addThenClause(variable=force, term=force_pos)
r11.setAntecedent(ant11)
r11.setConsequent(con11)
rb.addRule(r11)

# RULE12
r12 = FuzzyRuleType("rule12", connector="and", connectorMethod="MIN", weight=1.0)
ant12 = AntecedentType()
ant12.addClause(ClauseType(ang, ang_neu))
ant12.addClause(ClauseType(ca, ca_vpos))
con12 = ConsequentType()
con12.addThenClause(variable=force, term=force_vpos)
r12.setAntecedent(ant12)
r12.setConsequent(con12)
rb.addRule(r12)

# RULE13
r13 = FuzzyRuleType("rule13", connector="and", connectorMethod="MIN", weight=1.0)
ant13 = AntecedentType()
ant13.addClause(ClauseType(ang, ang_pos))
ant13.addClause(ClauseType(ca, ca_vneg))
con13 = ConsequentType()
con13.addThenClause(variable=force, term=force_neg)
r13.setAntecedent(ant13)
r13.setConsequent(con13)
rb.addRule(r13)

# RULE14
r14 = FuzzyRuleType("rule14", connector="and", connectorMethod="MIN", weight=1.0)
ant14 = AntecedentType()
ant14.addClause(ClauseType(ang, ang_pos))
ant14.addClause(ClauseType(ca, ca_neg))
con14 = ConsequentType()
con14.addThenClause(variable=force, term=force_neu)
r14.setAntecedent(ant14)
r14.setConsequent(con14)
rb.addRule(r14)

# RULE15
r15 = FuzzyRuleType("rule15", connector="and", connectorMethod="MIN", weight=1.0)
ant15 = AntecedentType()
ant15.addClause(ClauseType(ang, ang_pos))
ant15.addClause(ClauseType(ca, ca_neu))
con15 = ConsequentType()
con15.addThenClause(variable=force, term=force_pos)
r15.setAntecedent(ant15)
r15.setConsequent(con15)
rb.addRule(r15)

# RULE16
r16 = FuzzyRuleType("rule16", connector="and", connectorMethod="MIN", weight=1.0)
ant16 = AntecedentType()
ant16.addClause(ClauseType(ang, ang_vpos))
ant16.addClause(ClauseType(ca, ca_vneg))
con16 = ConsequentType()
con16.addThenClause(variable=force, term=force_neu)
r16.setAntecedent(ant16)
r16.setConsequent(con16)
rb.addRule(r16)

# RULE17
r17 = FuzzyRuleType("rule17", connector="and", connectorMethod="MIN", weight=1.0)
ant17 = AntecedentType()
ant17.addClause(ClauseType(ang, ang_vpos))
ant17.addClause(ClauseType(ca, ca_neg))
con17 = ConsequentType()
con17.addThenClause(variable=force, term=force_pos)
r17.setAntecedent(ant17)
r17.setConsequent(con17)
rb.addRule(r17)

# RULE18
r18 = FuzzyRuleType("rule18", connector="and", connectorMethod="MIN", weight=1.0)
ant18 = AntecedentType()
ant18.addClause(ClauseType(ang, ang_vpos))
ant18.addClause(ClauseType(ca, ca_neu))
con18 = ConsequentType()
con18.addThenClause(variable=force, term=force_vpos)
r18.setAntecedent(ant18)
r18.setConsequent(con18)
rb.addRule(r18)

# RULE19
r19 = FuzzyRuleType("rule19", connector="and", connectorMethod="MIN", weight=1.0)
ant19 = AntecedentType()
ant19.addClause(ClauseType(ang, ang_pos_or_vpos))
ant19.addClause(ClauseType(ca, ca_pos_or_vpos))
con19 = ConsequentType()
con19.addThenClause(variable=force, term=force_vpos)
r19.setAntecedent(ant19)
r19.setConsequent(con19)
rb.addRule(r19)

invertedPendulum.addRuleBase(rb)

print(invertedPendulum)

invertedPendulumXMLFile = "InvertedPendulumMamdani2.xml"
Py4jfml.writeFSTtoXML(invertedPendulum, invertedPendulumXMLFile)

Py4jfml.kill()