'''
This class creates an XML file with the definition of a TSK-type FLS for the problem of Inverted Pendulum:
    1) Triangular and Trapezoidal membership functions
    2) Definition of composed linguistic terms such as "A or B" with OrLogicalType and CircularDefinitionType
    3) 19 rules (some rules of order-0 and some rules of order-1)
'''
from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem
from py4jfml.Py4Jfml import Py4jfml
from py4jfml.knowledgebase.KnowledgeBaseType import KnowledgeBaseType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.knowledgebasevariable.TskVariableType import TskVariableType
from py4jfml.membershipfunction.CircularDefinitionType import CircularDefinitionType
from py4jfml.operator.OrLogicalType import OrLogicalType
from py4jfml.rule.AntecedentType import AntecedentType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.rule.TskConsequentType import TskConsequentType
from py4jfml.rule.TskFuzzyRuleType import TskFuzzyRuleType
from py4jfml.rulebase.FuzzySystemRuleBase import FuzzySystemRuleBase
from py4jfml.rulebase.TskRuleBaseType import TskRuleBaseType
from py4jfml.term.FuzzyTermType import FuzzyTermType
from py4jfml.term.TskTerm import TskTerm
from py4jfml.term.TskTermType import TskTermType

invertedPendulum = FuzzyInferenceSystem("invertedPendulum - TSK")

# KNOWLEDGE BASE
kb = KnowledgeBaseType()
invertedPendulum.setKnowledgeBase(kb)

# FUZZY VARIABLE Angle
ang = FuzzyVariableType("Angle", 0.0, 255.0)

# FUZZY TERM VNEG
ang_vneg = FuzzyTermType("very negative", FuzzyTermType.TYPE_trapezoidShape,[0.0, 0.0, 48.0, 88.0])
ang.addFuzzyTerm(ang_vneg)

# FUZZY TERM NEG
ang_neg = FuzzyTermType("negative", FuzzyTermType.TYPE_triangularShape,[48.0, 88.0, 128.0])
ang.addFuzzyTerm(ang_neg)

# FUZZY TERM NEU
ang_neu = FuzzyTermType("zero", FuzzyTermType.TYPE_triangularShape,[88.0, 128.0, 168.0])
ang.addFuzzyTerm(ang_neu)

# FUZZY TERM POS
ang_pos = FuzzyTermType("positive", FuzzyTermType.TYPE_triangularShape,[128.0, 168.0, 208.0])
ang.addFuzzyTerm(ang_pos)

# FUZZY TERM VPOS
ang_vpos = FuzzyTermType("very positive", FuzzyTermType.TYPE_trapezoidShape,[168.0, 208.0, 255.0, 255.0])
ang.addFuzzyTerm(ang_vpos)

# FUZZY TERM VNEG OR NEG
ang_or1 = OrLogicalType("BSUM", "very negative", "negative")
ang_c1 = CircularDefinitionType(orLogical=ang_or1, var=ang)
ang_vneg_or_neg = FuzzyTermType("very negative or negative", circular=ang_c1)
ang.addFuzzyTerm(ang_vneg_or_neg)

# FUZZY TERM POS OR VPOS
ang_or2 = OrLogicalType("BSUM", "positive", "very positive")
ang_c2 = CircularDefinitionType(orLogical=ang_or2, var=ang)
ang_pos_or_vpos = FuzzyTermType("positive or very positive", circular=ang_c2)
ang.addFuzzyTerm(ang_pos_or_vpos)

kb.addVariable(ang)

# FUZZY VARIABLE ChangeAngle(Angular Velocity)
ca = FuzzyVariableType("ChangeAngle", 0.0, 255.0)

# FUZZY TERM VNEG
ca_vneg = FuzzyTermType("very negative", FuzzyTermType.TYPE_trapezoidShape,[0.0, 0.0, 48.0, 88.0])
ca.addFuzzyTerm(ca_vneg)

# FUZZY TERM NEG
ca_neg = FuzzyTermType("negative", FuzzyTermType.TYPE_triangularShape,[48.0, 88.0, 128.0])
ca.addFuzzyTerm(ca_neg)

# FUZZY TERM NEU
ca_neu = FuzzyTermType("zero", FuzzyTermType.TYPE_triangularShape,[88.0, 128.0, 168.0])
ca.addFuzzyTerm(ca_neu)

# FUZZY TERM POS
ca_pos = FuzzyTermType("positive", FuzzyTermType.TYPE_triangularShape,[128.0, 168.0, 208.0])
ca.addFuzzyTerm(ca_pos)

# FUZZY TERM VPOS
ca_vpos = FuzzyTermType("very positive", FuzzyTermType.TYPE_trapezoidShape,[168.0, 208.0, 255.0, 255.0])
ca.addFuzzyTerm(ca_vpos)

# FUZZY TERM VNEG OR NEG
ca_or1 = OrLogicalType("BSUM", "very negative", "negative")
ca_c1 = CircularDefinitionType(orLogical=ca_or1, var=ca)
ca_vneg_or_neg = FuzzyTermType("very negative or negative", circular=ca_c1)
ca.addFuzzyTerm(ca_vneg_or_neg)

# FUZZY TERM POS OR VPOS
ca_or2 = OrLogicalType("BSUM", "positive", "very positive")
ca_c2 = CircularDefinitionType(orLogical=ca_or2, var=ang)
ca_pos_or_vpos = FuzzyTermType("positive or very positive", circular=ca_c2)
ca.addFuzzyTerm(ca_pos_or_vpos)

kb.addVariable(ca)

# TSK VARIABLE FORCE
force = TskVariableType("Force")
force.setDefaultValue(0.0)
force.setCombination("WA")
force.setType("output")

# FUZZY TERM VNEG TskTermType
force_vneg = TskTermType("very negative", TskTerm._ORDER_1, [48.0, 0.01, 0.02])
force.addTskTerm(force_vneg)

# FUZZY TERM NEG
force_neg = TskTermType("negative", TskTerm._ORDER_0, [88.0])
force.addTskTerm(force_neg)

# FUZZY TERM NEU
force_neu = TskTermType("zero", TskTerm._ORDER_1, [128.0, 0.05, 0.05])
force.addTskTerm(force_neu)

# FUZZY TERM POS
force_pos = TskTermType("positive", TskTerm._ORDER_0, [168.0])
force.addTskTerm(force_pos)

# FUZZY TERM VPOS
force_vpos = TskTermType("very positive", TskTerm._ORDER_1, [208.0, 0.05, 0.03])
force.addTskTerm(force_vpos)

kb.addVariable(force)

# RULE BASE
rb = TskRuleBaseType("rulebase1", FuzzySystemRuleBase.TYPE_TSK)
rb.setActivationMethod("PROD")

# RULE 1
r1 = TskFuzzyRuleType("rule1", connector="and", connectorMethod="MIN", weight=1.0)
ant1 = AntecedentType()
ant1.addClause(ClauseType(ang, ang_vneg_or_neg))
ant1.addClause(ClauseType(ca, ca_vneg_or_neg))
con1 = TskConsequentType()
con1.addTskThenClause(variable=force, term=force_vneg)
r1.setAntecedent(ant1)
r1.setTskConsequent(con1)
rb.addTskRule(r1)

# RULE2
r2 = TskFuzzyRuleType("rule2", connector="and", connectorMethod="MIN", weight=1.0)
ant2 = AntecedentType()
ant2.addClause(ClauseType(ang, ang_vneg))
ant2.addClause(ClauseType(ca, ca_neu))
con2 = TskConsequentType()
con2.addTskThenClause(variable=force, term=force_vneg)
r2.setAntecedent(ant2)
r2.setTskConsequent(con2)
rb.addTskRule(r2)


# RULE3
r3 = TskFuzzyRuleType("rule3", connector="and", connectorMethod="MIN", weight=1.0)
ant3 = AntecedentType()
ant3.addClause(ClauseType(ang, ang_vneg))
ant3.addClause(ClauseType(ca, ca_pos))
con3 = TskConsequentType()
con3.addTskThenClause(variable=force, term=force_neg)
r3.setAntecedent(ant3)
r3.setTskConsequent(con3)
rb.addTskRule(r3)

# RULE4
r4 = TskFuzzyRuleType("rule4", connector="and", connectorMethod="MIN", weight=1.0)
ant4 = AntecedentType()
ant4.addClause(ClauseType(ang, ang_vneg))
ant4.addClause(ClauseType(ca, ca_vpos))
con4 = TskConsequentType()
con4.addTskThenClause(variable=force, term=force_neu)
r4.setAntecedent(ant4)
r4.setTskConsequent(con4)
rb.addTskRule(r4)

# RULE5
r5 = TskFuzzyRuleType("rule5", connector="and", connectorMethod="MIN", weight=1.0)
ant5 = AntecedentType()
ant5.addClause(ClauseType(ang, ang_neg))
ant5.addClause(ClauseType(ca, ca_neu))
con5 = TskConsequentType()
con5.addTskThenClause(variable=force, term=force_neg)
r5.setAntecedent(ant5)
r5.setTskConsequent(con5)
rb.addTskRule(r5)

# RULE6
r6 = TskFuzzyRuleType("rule6", connector="and", connectorMethod="MIN", weight=1.0)
ant6 = AntecedentType()
ant6.addClause(ClauseType(ang, ang_neg))
ant6.addClause(ClauseType(ca, ca_pos))
con6 = TskConsequentType()
con6.addTskThenClause(variable=force, term=force_neu)
r6.setAntecedent(ant6)
r6.setTskConsequent(con6)
rb.addTskRule(r6)

# RULE7
r7 = TskFuzzyRuleType("rule7", connector="and", connectorMethod="MIN", weight=1.0)
ant7 = AntecedentType()
ant7.addClause(ClauseType(ang, ang_neg))
ant7.addClause(ClauseType(ca, ca_vpos))
con7 = TskConsequentType()
con7.addTskThenClause(variable=force, term=force_pos)
r7.setAntecedent(ant7)
r7.setTskConsequent(con7)
rb.addTskRule(r7)

# RULE8
r8 = TskFuzzyRuleType("rule8", connector="and", connectorMethod="MIN", weight=1.0)
ant8 = AntecedentType()
ant8.addClause(ClauseType(ang, ang_neu))
ant8.addClause(ClauseType(ca, ca_vneg))
con8 = TskConsequentType()
con8.addTskThenClause(variable=force, term=force_vneg)
r8.setAntecedent(ant8)
r8.setTskConsequent(con8)
rb.addTskRule(r8)

# RULE9
r9 = TskFuzzyRuleType("rule9", connector="and", connectorMethod="MIN", weight=1.0)
ant9 = AntecedentType()
ant9.addClause(ClauseType(ang, ang_neu))
ant9.addClause(ClauseType(ca, ca_neg))
con9 = TskConsequentType()
con9.addTskThenClause(variable=force, term=force_neg)
r9.setAntecedent(ant9)
r9.setTskConsequent(con9)
rb.addTskRule(r9)

# RULE10
r10 = TskFuzzyRuleType("rule10", connector="and", connectorMethod="MIN", weight=1.0)
ant10 = AntecedentType()
ant10.addClause(ClauseType(ang, ang_neu))
ant10.addClause(ClauseType(ca, ca_neu))
con10 = TskConsequentType()
con10.addTskThenClause(variable=force, term=force_neu)
r10.setAntecedent(ant10)
r10.setTskConsequent(con10)
rb.addTskRule(r10)

# RULE11
r11 = TskFuzzyRuleType("rule11", connector="and", connectorMethod="MIN", weight=1.0)
ant11 = AntecedentType()
ant11.addClause(ClauseType(ang, ang_neu))
ant11.addClause(ClauseType(ca, ca_pos))
con11 = TskConsequentType()
con11.addTskThenClause(variable=force, term=force_pos)
r11.setAntecedent(ant11)
r11.setTskConsequent(con11)
rb.addTskRule(r11)

# RULE12
r12 = TskFuzzyRuleType("rule12", connector="and", connectorMethod="MIN", weight=1.0)
ant12 = AntecedentType()
ant12.addClause(ClauseType(ang, ang_neu))
ant12.addClause(ClauseType(ca, ca_vpos))
con12 = TskConsequentType()
con12.addTskThenClause(variable=force, term=force_vpos)
r12.setAntecedent(ant12)
r12.setTskConsequent(con12)
rb.addTskRule(r12)

# RULE13
r13 = TskFuzzyRuleType("rule13", connector="and", connectorMethod="MIN", weight=1.0)
ant13 = AntecedentType()
ant13.addClause(ClauseType(ang, ang_pos))
ant13.addClause(ClauseType(ca, ca_vneg))
con13 = TskConsequentType()
con13.addTskThenClause(variable=force, term=force_neg)
r13.setAntecedent(ant13)
r13.setTskConsequent(con13)
rb.addTskRule(r13)

# RULE14
r14 = TskFuzzyRuleType("rule14", connector="and", connectorMethod="MIN", weight=1.0)
ant14 = AntecedentType()
ant14.addClause(ClauseType(ang, ang_pos))
ant14.addClause(ClauseType(ca, ca_neg))
con14 = TskConsequentType()
con14.addTskThenClause(variable=force, term=force_neu)
r14.setAntecedent(ant14)
r14.setTskConsequent(con14)
rb.addTskRule(r14)

# RULE15
r15 = TskFuzzyRuleType("rule15", connector="and", connectorMethod="MIN", weight=1.0)
ant15 = AntecedentType()
ant15.addClause(ClauseType(ang, ang_pos))
ant15.addClause(ClauseType(ca, ca_neu))
con15 = TskConsequentType()
con15.addTskThenClause(variable=force, term=force_pos)
r15.setAntecedent(ant15)
r15.setTskConsequent(con15)
rb.addTskRule(r15)

# RULE16
r16 = TskFuzzyRuleType("rule16", connector="and", connectorMethod="MIN", weight=1.0)
ant16 = AntecedentType()
ant16.addClause(ClauseType(ang, ang_vpos))
ant16.addClause(ClauseType(ca, ca_vneg))
con16 = TskConsequentType()
con16.addTskThenClause(variable=force, term=force_neu)
r16.setAntecedent(ant16)
r16.setTskConsequent(con16)
rb.addTskRule(r16)

# RULE17
r17 = TskFuzzyRuleType("rule17", connector="and", connectorMethod="MIN", weight=1.0)
ant17 = AntecedentType()
ant17.addClause(ClauseType(ang, ang_vpos))
ant17.addClause(ClauseType(ca, ca_neg))
con17 = TskConsequentType()
con17.addTskThenClause(variable=force, term=force_pos)
r17.setAntecedent(ant17)
r17.setTskConsequent(con17)
rb.addTskRule(r17)

# RULE18
r18 = TskFuzzyRuleType("rule18", connector="and", connectorMethod="MIN", weight=1.0)
ant18 = AntecedentType()
ant18.addClause(ClauseType(ang, ang_vpos))
ant18.addClause(ClauseType(ca, ca_neu))
con18 = TskConsequentType()
con18.addTskThenClause(variable=force, term=force_vpos)
r18.setAntecedent(ant18)
r18.setTskConsequent(con18)
rb.addTskRule(r18)

# RULE19
r19 = TskFuzzyRuleType("rule19", connector="and", connectorMethod="MIN", weight=1.0)
ant19 = AntecedentType()
ant19.addClause(ClauseType(ang, ang_pos_or_vpos))
ant19.addClause(ClauseType(ca, ca_pos_or_vpos))
con19 = TskConsequentType()
con19.addTskThenClause(variable=force, term=force_vpos)
r19.setAntecedent(ant19)
r19.setTskConsequent(con19)
rb.addTskRule(r19)

invertedPendulum.addRuleBase(rb)

print(invertedPendulum)

#WRITTING INVERTED PENDULUM EXAMPLE INTO AN XML FILE
invertedPendulumXMLFile = "XMLFiles/InvertedPendulumTSK2.xml"
Py4jfml.writeFSTtoXML(invertedPendulum, invertedPendulumXMLFile)