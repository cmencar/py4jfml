'''
This class creates an XML file with the definition of a TSK-type order-0 FLS for the problem of Inverted Pendulum:
 *   1) Triangular and Trapezoidal membership functions
 *   2) Definition of composed linguistic terms such as "A or B" with OrLogicalType and CircularDefinitionType
 *   3) 19 rules
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
from py4jfml.rulebase.TskRuleBaseType import TskRuleBaseType
from py4jfml.term.FuzzyTermType import FuzzyTermType
from py4jfml.term.TskTermType import TskTermType
from py4jfml.term.TskTerm import TskTerm
from py4jfml.rulebase.FuzzySystemRuleBase import FuzzySystemRuleBase

invertedPendulum = FuzzyInferenceSystem("invertedPendulum - TSK")

#KNOWLEDGE BASE
kb = KnowledgeBaseType()
invertedPendulum.setKnowledgeBase(kb)

#FUZZY VARIABLE Angle
ang = FuzzyVariableType(name="Angle", domainLeft=0.0, domainRight=255.0)

#FUZZY TERM VNEG
ang_vneg = FuzzyTermType(name="very negative", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[0.0, 0.0, 48.0, 88.0])
ang.addFuzzyTerm(ft=ang_vneg)

#FUZZY TERM NEG
ang_neg = FuzzyTermType(name="negative", type_java=FuzzyTermType.TYPE_triangularShape, param=[48.0, 88.0, 128.0])
ang.addFuzzyTerm(ft=ang_neg)

#FUZZY TERM NEU
ang_neu = FuzzyTermType(name="zero", type_java=FuzzyTermType.TYPE_triangularShape, param=[88.0, 128.0, 168.0])
ang.addFuzzyTerm(ft=ang_neu)

#FUZZY TERM POS
ang_pos = FuzzyTermType(name="positive", type_java=FuzzyTermType.TYPE_triangularShape, param=[128.0, 168.0, 208.0])
ang.addFuzzyTerm(ft=ang_pos)

#FUZZY TERM VPOS
ang_vpos = FuzzyTermType(name="very positive", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[168.0, 208.0, 255.0, 255.0])
ang.addFuzzyTerm(ft=ang_vpos)

#FUZZY TERM VNEG OR NEG
ang_or1 = OrLogicalType("BSUM", "very negative", "negative")
ang_c1 = CircularDefinitionType(orLogical=ang_or1, var=ang)
ang_vneg_or_neg = FuzzyTermType(name="very negative or negative", circular=ang_c1)
ang.addFuzzyTerm(ft=ang_vneg_or_neg)

#FUZZY TERM POS OR VPOS
ang_or2 = OrLogicalType("BSUM", "positive", "very positive")
ang_c2 = CircularDefinitionType(orLogical=ang_or2, var=ang)
ang_pos_or_vpos = FuzzyTermType(name="positive or very positive", circular=ang_c2)
ang.addFuzzyTerm(ft=ang_pos_or_vpos)

kb.addVariable(ang)

#FUZZY VARIABLE ChangeAngle (Angular Velocity)
ca = FuzzyVariableType(name="ChangeAngle", domainLeft=0.0, domainRight=255.0)

#FUZZY TERM VNEG
ca_vneg = FuzzyTermType(name="very negative", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[0.0, 0.0, 48.0, 88.0])
ca.addFuzzyTerm(ft=ca_vneg)

#FUZZY TERM NEG
ca_neg = FuzzyTermType(name="negative", type_java=FuzzyTermType.TYPE_triangularShape, param=[48.0, 88.0, 128.0])
ca.addFuzzyTerm(ft=ca_neg)

#FUZZY TERM NEU
ca_neu = FuzzyTermType(name="zero", type_java=FuzzyTermType.TYPE_triangularShape, param=[88.0, 128.0, 168.0])
ca.addFuzzyTerm(ft=ca_neu)

#FUZZY TERM POS
ca_pos = FuzzyTermType(name="positive", type_java=FuzzyTermType.TYPE_triangularShape, param=[128.0, 168.0, 208.0])
ca.addFuzzyTerm(ft=ca_pos)

#FUZZY TERM VPOS
ca_vpos = FuzzyTermType(name="very positive", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[168.0, 208.0, 255.0, 255.0])
ca.addFuzzyTerm(ft=ca_vpos)

#FUZZY TERM VNEG OR NEG
ca_or1 = OrLogicalType("BSUM", "very negative", "negative")
ca_c1 = CircularDefinitionType(orLogical=ca_or1, var=ca)
ca_vneg_or_neg = FuzzyTermType(name="very negative or negative", circular=ca_c1)
ca.addFuzzyTerm(ft=ca_vneg_or_neg)

#FUZZY TERM POS OR VPOS
ca_or2 = OrLogicalType("BSUM", "positive", "very positive")
ca_c2 = CircularDefinitionType(orLogical=ca_or2, var=ang)
ca_pos_or_vpos = FuzzyTermType(name="positive or very positive", circular=ca_c2)
ca.addFuzzyTerm(ft=ca_pos_or_vpos)

kb.addVariable(ca)

#TSK VARIABLE FORCE
force = TskVariableType(name="Force")
force.setDefaultValue(value=0.0)
force.setCombination(value="WA")
force.setType(value="output")

#FUZZY TERM VNEG
force_vneg = TskTermType(name="very negative", order=TskTerm._ORDER_0, coeff=[48.0])
force.addTskTerm(force_vneg)

#FUZZY TERM NEG
force_neg = TskTermType(name="negative", order=TskTerm._ORDER_0, coeff=[88.0])
force.addTskTerm(force_neg)

#FUZZY TERM NEU
force_neu = TskTermType(name="zero", order=TskTerm._ORDER_0, coeff=[128.0])
force.addTskTerm(force_neu)

#FUZZY TERM POS
force_pos = TskTermType(name="positive", order=TskTerm._ORDER_0, coeff=[128.0])
force.addTskTerm(force_pos)

#FUZZY TERM VPOS
force_vpos = TskTermType(name="very positive", order=TskTerm._ORDER_0, coeff=[208.0])
force.addTskTerm(force_vpos)

kb.addVariable(force)

#RULE BASE
rb = TskRuleBaseType(name="rulebase1", tskRuleBaseType=FuzzySystemRuleBase.TYPE_TSK)
rb.setActivationMethod(value="PROD")

#RULE 1
r1 = TskFuzzyRuleType(name="rule1", connector="and", connectorMethod="MIN", weight=1.0)
ant1 = AntecedentType()
ant1.addClause(c=ClauseType(ang, ang_vneg_or_neg))
ant1.addClause(c=ClauseType(ca, ca_vneg_or_neg))
con1 = TskConsequentType()
con1.addTskThenClause(variable=force, term=force_vneg)
r1.setAntecedent(value=ant1)
r1.setTskConsequent(value=con1)
rb.addTskRule(rule=r1)

#RULE 2
r2 = TskFuzzyRuleType(name="rule2", connector="and", connectorMethod="MIN", weight=1.0)
ant2 = AntecedentType()
ant2.addClause(c=ClauseType(ang, ang_vneg))
ant2.addClause(c=ClauseType(ca, ca_neu))
con2 = TskConsequentType()
con2.addTskThenClause(variable=force, term=force_vneg)
r2.setAntecedent(value=ant2)
r2.setTskConsequent(value=con2)
rb.addTskRule(rule=r2)

#RULE 3
r3 = TskFuzzyRuleType(name="rule3", connector="and", connectorMethod="MIN", weight=1.0)
ant3 = AntecedentType()
ant3.addClause(c=ClauseType(ang, ang_vneg))
ant3.addClause(c=ClauseType(ca, ca_pos))
con3 = TskConsequentType()
con3.addTskThenClause(variable=force, term=force_neg)
r3.setAntecedent(value=ant3)
r3.setTskConsequent(value=con3)
rb.addTskRule(rule=r3)

#RULE 4
r4 = TskFuzzyRuleType(name="rule4", connector="and", connectorMethod="MIN", weight=1.0)
ant4 = AntecedentType()
ant4.addClause(c=ClauseType(ang, ang_vneg))
ant4.addClause(c=ClauseType(ca, ca_vpos))
con4 = TskConsequentType()
con4.addTskThenClause(variable=force, term=force_neu)
r4.setAntecedent(value=ant4)
r4.setTskConsequent(value=con4)
rb.addTskRule(rule=r4)

#RULE 5
r5 = TskFuzzyRuleType(name="rule5", connector="and", connectorMethod="MIN", weight=1.0)
ant5 = AntecedentType()
ant5.addClause(c=ClauseType(ang, ang_neg))
ant5.addClause(c=ClauseType(ca, ca_neu))
con5 = TskConsequentType()
con5.addTskThenClause(variable=force, term=force_neg)
r5.setAntecedent(value=ant5)
r5.setTskConsequent(value=con5)
rb.addTskRule(rule=r5)

#RULE 6
r6 = TskFuzzyRuleType(name="rule6", connector="and", connectorMethod="MIN", weight=1.0)
ant6 = AntecedentType()
ant6.addClause(c=ClauseType(ang, ang_neg))
ant6.addClause(c=ClauseType(ca, ca_pos))
con6 = TskConsequentType()
con6.addTskThenClause(variable=force, term=force_neu)
r6.setAntecedent(value=ant6)
r6.setTskConsequent(value=con6)
rb.addTskRule(rule=r6)

#RULE 7
r7 = TskFuzzyRuleType(name="rule7", connector="and", connectorMethod="MIN", weight=1.0)
ant7 = AntecedentType()
ant7.addClause(c=ClauseType(ang, ang_neg))
ant7.addClause(c=ClauseType(ca, ca_vpos))
con7 = TskConsequentType()
con7.addTskThenClause(variable=force, term=force_pos)
r7.setAntecedent(value=ant7)
r7.setTskConsequent(value=con7)
rb.addTskRule(rule=r7)

#RULE 8
r8 = TskFuzzyRuleType(name="rule8", connector="and", connectorMethod="MIN", weight=1.0)
ant8 = AntecedentType()
ant8.addClause(c=ClauseType(ang, ang_neu))
ant8.addClause(c=ClauseType(ca, ca_vneg))
con8 = TskConsequentType()
con8.addTskThenClause(variable=force, term=force_vneg)
r8.setAntecedent(value=ant8)
r8.setTskConsequent(value=con8)
rb.addTskRule(rule=r8)

#RULE 9
r9 = TskFuzzyRuleType(name="rule9", connector="and", connectorMethod="MIN", weight=1.0)
ant9 = AntecedentType()
ant9.addClause(c=ClauseType(ang, ang_neu))
ant9.addClause(c=ClauseType(ca, ca_neg))
con9 = TskConsequentType()
con9.addTskThenClause(variable=force, term=force_neg)
r9.setAntecedent(value=ant9)
r9.setTskConsequent(value=con9)
rb.addTskRule(rule=r9)

#RULE 10
r10 = TskFuzzyRuleType(name="rule10", connector="and", connectorMethod="MIN", weight=1.0)
ant10 = AntecedentType()
ant10.addClause(c=ClauseType(ang, ang_neu))
ant10.addClause(c=ClauseType(ca, ca_neu))
con10 = TskConsequentType()
con10.addTskThenClause(variable=force, term=force_neu)
r10.setAntecedent(value=ant10)
r10.setTskConsequent(value=con10)
rb.addTskRule(rule=r10)

#RULE 11
r11 = TskFuzzyRuleType(name="rule11", connector="and", connectorMethod="MIN", weight=1.0)
ant11 = AntecedentType()
ant11.addClause(c=ClauseType(ang, ang_neu))
ant11.addClause(c=ClauseType(ca, ca_pos))
con11 = TskConsequentType()
con11.addTskThenClause(variable=force, term=force_pos)
r11.setAntecedent(value=ant11)
r11.setTskConsequent(value=con11)
rb.addTskRule(rule=r11)

#RULE 12
r12 = TskFuzzyRuleType(name="rule12", connector="and", connectorMethod="MIN", weight=1.0)
ant12 = AntecedentType()
ant12.addClause(c=ClauseType(ang, ang_neu))
ant12.addClause(c=ClauseType(ca, ca_vpos))
con12 = TskConsequentType()
con12.addTskThenClause(variable=force, term=force_vpos)
r12.setAntecedent(value=ant12)
r12.setTskConsequent(value=con12)
rb.addTskRule(rule=r12)

#RULE 13
r13 = TskFuzzyRuleType(name="rule13", connector="and", connectorMethod="MIN", weight=1.0)
ant13 = AntecedentType()
ant13.addClause(c=ClauseType(ang, ang_pos))
ant13.addClause(c=ClauseType(ca, ca_vneg))
con13 = TskConsequentType()
con13.addTskThenClause(variable=force, term=force_neg)
r13.setAntecedent(value=ant13)
r13.setTskConsequent(value=con13)
rb.addTskRule(rule=r13)

#RULE 14
r14 = TskFuzzyRuleType(name="rule14", connector="and", connectorMethod="MIN", weight=1.0)
ant14 = AntecedentType()
ant14.addClause(c=ClauseType(ang, ang_pos))
ant14.addClause(c=ClauseType(ca, ca_neg))
con14 = TskConsequentType()
con14.addTskThenClause(variable=force, term=force_neu)
r14.setAntecedent(value=ant14)
r14.setTskConsequent(value=con14)
rb.addTskRule(rule=r14)

#RULE 15
r15 = TskFuzzyRuleType(name="rule15", connector="and", connectorMethod="MIN", weight=1.0)
ant15 = AntecedentType()
ant15.addClause(c=ClauseType(ang, ang_pos))
ant15.addClause(c=ClauseType(ca, ca_neu))
con15 = TskConsequentType()
con15.addTskThenClause(variable=force, term=force_pos)
r15.setAntecedent(value=ant15)
r15.setTskConsequent(value=con15)
rb.addTskRule(rule=r15)

#RULE 16
r16 = TskFuzzyRuleType(name="rule16", connector="and", connectorMethod="MIN", weight=1.0)
ant16 = AntecedentType()
ant16.addClause(c=ClauseType(ang, ang_vpos))
ant16.addClause(c=ClauseType(ca, ca_vneg))
con16 = TskConsequentType()
con16.addTskThenClause(variable=force, term=force_neu)
r16.setAntecedent(value=ant16)
r16.setTskConsequent(value=con16)
rb.addTskRule(rule=r16)

#RULE 17
r17 = TskFuzzyRuleType(name="rule17", connector="and", connectorMethod="MIN", weight=1.0)
ant17 = AntecedentType()
ant17.addClause(c=ClauseType(ang, ang_vpos))
ant17.addClause(c=ClauseType(ca, ca_neg))
con17 = TskConsequentType()
con17.addTskThenClause(variable=force, term=force_pos)
r17.setAntecedent(value=ant17)
r17.setTskConsequent(value=con17)
rb.addTskRule(rule=r17)

#RULE 18
r18 = TskFuzzyRuleType(name="rule18", connector="and", connectorMethod="MIN", weight=1.0)
ant18 = AntecedentType()
ant18.addClause(c=ClauseType(ang, ang_vpos))
ant18.addClause(c=ClauseType(ca, ca_neu))
con18 = TskConsequentType()
con18.addTskThenClause(variable=force, term=force_vpos)
r18.setAntecedent(value=ant18)
r18.setTskConsequent(value=con18)
rb.addTskRule(rule=r18)

#RULE 19
r19 = TskFuzzyRuleType(name="rule19", connector="and", connectorMethod="MIN", weight=1.0)
ant19 = AntecedentType()
ant19.addClause(c=ClauseType(ang, ang_pos_or_vpos))
ant19.addClause(c=ClauseType(ca, ca_pos_or_vpos))
con19 = TskConsequentType()
con19.addTskThenClause(variable=force, term=force_vpos)
r19.setAntecedent(value=ant19)
r19.setTskConsequent(value=con19)
rb.addTskRule(rule=r19)

invertedPendulum.addRuleBase(rb);

print(invertedPendulum)

#WRITTING INVERTED PENDULUM EXAMPLE INTO AN XML FILE
invertedPendulumXMLFile = "XMLFiles/InvertedPendulumTSK1.xml"
Py4jfml.writeFSTtoXML(invertedPendulum, invertedPendulumXMLFile)

Py4jfml.kill()