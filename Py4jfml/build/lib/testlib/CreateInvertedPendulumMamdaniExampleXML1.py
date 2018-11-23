'''
This class creates an XML file with the definition of a Mamdani-type FLS for the problem of Inverted Pendulum:
 *   1) Triangular and Trapezoidal membership functions
 *   2) 19 rules
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

invertedPendulum = FuzzyInferenceSystem(name="invertedPendulum - MAMDANI")

#KNOWLEDGE BASE
kb = KnowledgeBaseType()
invertedPendulum.setKnowledgeBase(value=kb)

#FUZZY VARIABLE Angle
ang = FuzzyVariableType(name="Angle", domainLeft=0.0, domainRight=255.0)

#FUZZY TERM VNEG
ang_vneg = FuzzyTermType(name="very negative", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[0.0, 0.0, 48.0, 88.0])
ang.addFuzzyTerm(ft=ang_vneg)

#FUZZY TERM NEG
ang_neg = FuzzyTermType(name="negative", type_java=FuzzyTermType.TYPE_triangularShape, param=[48.0, 88.0, 128.0])
ang.addFuzzyTerm(ft=ang_neg)

#FUZZY TERM NEU
ang_neu = FuzzyTermType(name="zero",  type_java=FuzzyTermType.TYPE_triangularShape, param=[88.0, 128.0, 168.0])
ang.addFuzzyTerm(ft=ang_neu)

#FUZZY TERM POS
ang_pos = FuzzyTermType(name="positive", type_java=FuzzyTermType.TYPE_triangularShape, param=[128.0, 168.0, 208.0])
ang.addFuzzyTerm(ft=ang_pos)

#FUZZY TERM VPOS
ang_vpos = FuzzyTermType(name="very positive", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[168.0, 208.0, 255.0, 255.0])
ang.addFuzzyTerm(ft=ang_vpos)

#FUZZY TERM VNEG OR NEG
ang_vneg_or_neg = FuzzyTermType(name="very negative or negative", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[0.0, 0.0, 88.0, 128.0])
ang.addFuzzyTerm(ft=ang_vneg_or_neg)

#FUZZY TERM POS OR VPOS
ang_pos_or_vpos = FuzzyTermType(name="positive or very positive", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[128.0, 168.0, 255.0, 255.0])
ang.addFuzzyTerm(ft=ang_pos_or_vpos)

kb.addVariable(var=ang)

#FUZZY VARIABLE ChangeAngle
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
ca.addFuzzyTerm(ft=ang_vpos)

#FUZZY TERM VNEG OR NEG
ca_vneg_or_neg = FuzzyTermType(name="very negative or negative", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[0.0, 0.0, 88.0, 128.0])
ca.addFuzzyTerm(ft=ca_vneg_or_neg)

#FUZZY TERM POS OR VPOS
ca_pos_or_vpos = FuzzyTermType(name="positive or very positive", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[128.0, 168.0, 255.0, 255.0])
ca.addFuzzyTerm(ft=ca_pos_or_vpos)

kb.addVariable(var=ca)

#FUZZY VARIABLE FORCE
force = FuzzyVariableType(name="Force", domainLeft=0.0, domainRight=255.0)
force.setDefaultValue(value=0.0)
force.setAccumulation(value="MAX")
force.setDefuzzifierName(value="COG")
force.setType(value="output")

#FUZZY TERM VNEG
force_vneg = FuzzyTermType(name="very negative", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[0.0, 0.0, 48.0, 88.0])
force.addFuzzyTerm(ft=force_vneg)

#FUZZY TERM NEG
force_neg = FuzzyTermType(name="negative", type_java=FuzzyTermType.TYPE_triangularShape, param=[48.0, 88.0, 128.0])
force.addFuzzyTerm(ft=force_neg)

#FUZZY TERM NEU
force_neu = FuzzyTermType(name="zero", type_java=FuzzyTermType.TYPE_triangularShape, param=[88.0, 128.0, 168.0])
force.addFuzzyTerm(ft=force_neu)

#FUZZY TERM POS
force_pos = FuzzyTermType(name="positive", type_java=FuzzyTermType.TYPE_triangularShape, param=[128.0, 168.0, 208.0])
force.addFuzzyTerm(ft=force_pos)

#FUZZY TERM VPOS
force_vpos = FuzzyTermType(name="very positive", type_java=FuzzyTermType.TYPE_trapezoidShape, param=[168.0, 208.0, 255.0, 255.0])
force.addFuzzyTerm(ft=force_vpos)

kb.addVariable(var=force)

#RULE BASE
rb = MamdaniRuleBaseType(name="rulebase1")

#RULE 1
r1 = FuzzyRuleType(name="rule1", connector="and", connectorMethod="MIN", weight=1.0)
ant1 = AntecedentType()
ant1.addClause(c=ClauseType(ang, ang_vneg_or_neg))
ant1.addClause(c=ClauseType(ca, ca_vneg_or_neg))
con1 = ConsequentType()
con1.addThenClause(variable=force, term=force_vneg)
r1.setAntecedent(value=ant1)
r1.setConsequent(value=con1)
rb.addRule(rule=r1)

#RULE 2
r2 = FuzzyRuleType(name="rule2", connector="and", connectorMethod="MIN", weight=1.0)
ant2 = AntecedentType()
ant2.addClause(c=ClauseType(ang, ang_vneg))
ant2.addClause(c=ClauseType(ca, ca_neu))
con2 = ConsequentType()
con2.addThenClause(variable=force, term=force_vneg)
r2.setAntecedent(value=ant2)
r2.setConsequent(value=con2)
rb.addRule(rule=r2)

#RULE 3
r3 = FuzzyRuleType(name="rule3", connector="and", connectorMethod="MIN", weight=1.0)
ant3 = AntecedentType()
ant3.addClause(c=ClauseType(ang, ang_vneg))
ant3.addClause(c=ClauseType(ca, ca_pos))
con3 = ConsequentType()
con3.addThenClause(variable=force, term=force_neg)
r3.setAntecedent(value=ant3)
r3.setConsequent(value=con3)
rb.addRule(rule=r3)

#RULE 4
r4 = FuzzyRuleType(name="rule4", connector="and", connectorMethod="MIN", weight=1.0)
ant4 = AntecedentType()
ant4.addClause(c=ClauseType(ang, ang_vneg))
ant4.addClause(c=ClauseType(ca, ca_vpos))
con4 = ConsequentType()
con4.addThenClause(variable=force, term=force_neu)
r4.setAntecedent(value=ant4)
r4.setConsequent(value=con4)
rb.addRule(rule=r4)

#RULE 5
r5 = FuzzyRuleType(name="rule5", connector="and", connectorMethod="MIN", weight=1.0)
ant5 = AntecedentType()
ant5.addClause(c=ClauseType(ang, ang_neg))
ant5.addClause(c=ClauseType(ca, ca_neu))
con5 = ConsequentType()
con5.addThenClause(variable=force, term=force_neg)
r5.setAntecedent(value=ant5)
r5.setConsequent(value=con5)
rb.addRule(rule=r5)

#RULE 6
r6 = FuzzyRuleType(name="rule6", connector="and", connectorMethod="MIN", weight=1.0)
ant6 = AntecedentType()
ant6.addClause(c=ClauseType(ang, ang_neg))
ant6.addClause(c=ClauseType(ca, ca_pos))
con6 = ConsequentType()
con6.addThenClause(variable=force, term=force_neu)
r6.setAntecedent(value=ant6)
r6.setConsequent(value=con6)
rb.addRule(rule=r6)

#RULE 7
r7 = FuzzyRuleType(name="rule7", connector="and", connectorMethod="MIN", weight=1.0)
ant7 = AntecedentType()
ant7.addClause(c=ClauseType(ang, ang_neg))
ant7.addClause(c=ClauseType(ca, ca_vpos))
con7 = ConsequentType()
con7.addThenClause(variable=force, term=force_pos)
r7.setAntecedent(value=ant7)
r7.setConsequent(value=con7)
rb.addRule(rule=r7)

#RULE 8
r8 = FuzzyRuleType(name="rule8", connector="and", connectorMethod="MIN", weight=1.0)
ant8 = AntecedentType()
ant8.addClause(c=ClauseType(ang, ang_neu))
ant8.addClause(c=ClauseType(ca, ca_vneg))
con8 = ConsequentType()
con8.addThenClause(variable=force, term=force_vneg)
r8.setAntecedent(value=ant8)
r8.setConsequent(value=con8)
rb.addRule(rule=r8)

#RULE 9
r9 = FuzzyRuleType(name="rule9", connector="and", connectorMethod="MIN", weight=1.0)
ant9 = AntecedentType()
ant9.addClause(c=ClauseType(ang, ang_neu))
ant9.addClause(c=ClauseType(ca, ca_neg))
con9 = ConsequentType()
con9.addThenClause(variable=force, term=force_neg)
r9.setAntecedent(value=ant9)
r9.setConsequent(value=con9)
rb.addRule(rule=r9)

#RULE 10
r10 = FuzzyRuleType(name="rule10", connector="and", connectorMethod="MIN", weight=1.0)
ant10 = AntecedentType()
ant10.addClause(c=ClauseType(ang, ang_neu))
ant10.addClause(c=ClauseType(ca, ca_neu))
con10 = ConsequentType()
con10.addThenClause(variable=force, term=force_neu)
r10.setAntecedent(value=ant10)
r10.setConsequent(value=con10)
rb.addRule(rule=r10)

#RULE 11
r11 = FuzzyRuleType(name="rule11", connector="and", connectorMethod="MIN", weight=1.0)
ant11 = AntecedentType()
ant11.addClause(c=ClauseType(ang, ang_neu))
ant11.addClause(c=ClauseType(ca, ca_pos))
con11 = ConsequentType()
con11.addThenClause(variable=force, term=force_pos)
r11.setAntecedent(value=ant11)
r11.setConsequent(value=con11)
rb.addRule(rule=r11)

#RULE 12
r12 = FuzzyRuleType(name="rule12", connector="and", connectorMethod="MIN", weight=1.0)
ant12 = AntecedentType()
ant12.addClause(c=ClauseType(ang, ang_neu))
ant12.addClause(c=ClauseType(ca, ca_vpos))
con12 = ConsequentType()
con12.addThenClause(variable=force, term=force_vpos)
r12.setAntecedent(value=ant12)
r12.setConsequent(value=con12)
rb.addRule(rule=r12)

#RULE 13
r13 = FuzzyRuleType(name="rule13", connector="and", connectorMethod="MIN", weight=1.0)
ant13 = AntecedentType()
ant13.addClause(c=ClauseType(ang, ang_pos))
ant13.addClause(c=ClauseType(ca, ca_vneg))
con13 = ConsequentType()
con13.addThenClause(variable=force, term=force_neg)
r13.setAntecedent(value=ant13)
r13.setConsequent(value=con13)
rb.addRule(rule=r13)

#RULE 14
r14 = FuzzyRuleType(name="rule14", connector="and", connectorMethod="MIN", weight=1.0)
ant14 = AntecedentType()
ant14.addClause(c=ClauseType(ang, ang_pos))
ant14.addClause(c=ClauseType(ca, ca_neg))
con14 = ConsequentType()
con14.addThenClause(variable=force, term=force_neu)
r14.setAntecedent(value=ant14)
r14.setConsequent(value=con14)
rb.addRule(rule=r14)

#RULE 15
r15 = FuzzyRuleType(name="rule15", connector="and", connectorMethod="MIN", weight=1.0)
ant15 = AntecedentType()
ant15.addClause(c=ClauseType(ang, ang_pos))
ant15.addClause(c=ClauseType(ca, ca_neu))
con15 = ConsequentType()
con15.addThenClause(variable=force, term=force_pos)
r15.setAntecedent(value=ant15)
r15.setConsequent(value=con15)
rb.addRule(rule=r15)

#RULE 16
r16 = FuzzyRuleType(name="rule16", connector="and", connectorMethod="MIN", weight=1.0)
ant16 = AntecedentType()
ant16.addClause(c=ClauseType(ang, ang_vpos))
ant16.addClause(c=ClauseType(ca, ca_vneg))
con16 = ConsequentType()
con16.addThenClause(variable=force, term=force_neu)
r16.setAntecedent(value=ant16)
r16.setConsequent(value=con16)
rb.addRule(rule=r16)

#RULE 17
r17 = FuzzyRuleType(name="rule17", connector="and", connectorMethod="MIN", weight=1.0)
ant17 = AntecedentType()
ant17.addClause(c=ClauseType(ang, ang_vpos))
ant17.addClause(c=ClauseType(ca, ca_neg))
con17 = ConsequentType()
con17.addThenClause(variable=force, term=force_pos)
r17.setAntecedent(value=ant17)
r17.setConsequent(value=con17)
rb.addRule(rule=r17)

#RULE 18
r18 = FuzzyRuleType(name="rule18", connector="and", connectorMethod="MIN", weight=1.0)
ant18 = AntecedentType()
ant18.addClause(c=ClauseType(ang, ang_vpos))
ant18.addClause(c=ClauseType(ca, ca_neu))
con18 = ConsequentType()
con18.addThenClause(variable=force, term=force_vpos)
r18.setAntecedent(value=ant18)
r18.setConsequent(value=con18)
rb.addRule(rule=r18)

#RULE 19
r19 = FuzzyRuleType(name="rule19", connector="and", connectorMethod="MIN", weight=1.0)
ant19 = AntecedentType()
ant19.addClause(c=ClauseType(ang, ang_pos_or_vpos))
ant19.addClause(c=ClauseType(ca, ca_pos_or_vpos))
con19 = ConsequentType()
con19.addThenClause(variable=force, term=force_vpos)
r19.setAntecedent(value=ant19)
r19.setConsequent(value=con19)
rb.addRule(r19)

invertedPendulum.addRuleBase(rb);

print(invertedPendulum)

#WRITTING INVERTED PENDULUM EXAMPLE INTO AN XML FILE
invertedPendulumXMLFile = "InvertedPendulumMamdani1.xml"
Py4jfml.writeFSTtoXML(invertedPendulum, invertedPendulumXMLFile)

Py4jfml.kill()