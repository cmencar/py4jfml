from py4j.java_gateway import JavaGateway
from py4jfml.Py4Jfml import Py4jfml
from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem
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

#Creazione oggetto tipper
tipper = FuzzyInferenceSystem("tipper")

#creazione dell'oggetto kb e aggiunta all'insieme di conoscenza fuzzy
kb = KnowledgeBaseType()
tipper.setKnowledgeBase(kb)

# creazione variabile tip con nome service dominio sinistro 0 e dominion destro 10
tip = FuzzyVariableType("tip", 0., 10.)
kb.addVariable(tip)

# creazione leftLinear con coordinate 0 e 1 e aggiunta all'insieme di conoscenza
cheap = FuzzyTermType("cheap", FuzzyTerm.TYPE_leftLinearShape, [0., 1.])

# creazione triangolarShape con coordinate 1,2 e 3 e aggiunta all'insieme di conoscenza
poor = FuzzyTermType("cheap", FuzzyTerm.TYPE_triangularShape, [1., 2., 3.])

tip.addFuzzyTerm(poor)

#creazione variabile service con nome service dominio sinistro 0 e dominion destro 10
service = FuzzyVariableType("service", 0., 10.)
kb.addVariable(service)

# creazione leftLinear con coordinate 0 e 1 e aggiunta all'insieme di conoscenza
poor = FuzzyTermType("poor", FuzzyTerm.TYPE_leftLinearShape, [0., 1.])

#creazione triangolarShape con coordinate 1,2 e 3 e aggiunta all'insieme di conoscenza
poor = FuzzyTermType("poor", FuzzyTerm.TYPE_triangularShape, [1., 2., 3.])

service.addFuzzyTerm(poor)

# creazione variabile food con nome food dominio sinistro 0 e dominio destro 10 e aggiunta all'insieme di conoscenza
food = FuzzyVariableType("food", 0.0, 10.0)
kb.addVariable(food)

#creazione triangolarShape con coordinate 0,2 e 4 (float) e aggiunta all'insieme di conoscenza
rancid = FuzzyTermType("rancid", FuzzyTerm.TYPE_triangularShape, [0., 2., 4.])
food.addFuzzyTerm(rancid)

# creazione Left LinearShape con coordinate 0 e 4 (float) e aggiunta all'insieme di conoscenza
rancid = FuzzyTermType("rancid", FuzzyTerm.TYPE_leftLinearShape, [0., 4.])
food.addFuzzyTerm(rancid)

# creazione Right LinearShape con coordinate 4 e 10(float) e aggiunta all'insieme di conoscenza
delicious = FuzzyTermType("delicious", FuzzyTerm.TYPE_rightLinearShape, [4.,10.])
food.addFuzzyTerm(delicious)

# creazione TrapezoidalShape con coordinate 0,1,3 e 4(float) e aggiunta all'insieme di conoscenza
rancid = FuzzyTermType("rancid", FuzzyTerm.TYPE_trapezoidShape, [0.,1.,3.,4.])
food.addFuzzyTerm(rancid)

# creazione RectangularShape con coordinate 4 e 7 (float) e aggiunta all'insieme di conoscenza
good = FuzzyTermType("good", FuzzyTerm.TYPE_rectangularShape, [4.,7.])
food.addFuzzyTerm(good)

# creazione GaussianShape con coordinate 5 e 1 (float) e aggiunta all'insieme di conoscenza
good = FuzzyTermType("good", FuzzyTerm.TYPE_gaussianShape, [5., 1.])
food.addFuzzyTerm(good)

# creazione GaussianShape con coordinate 5 e 1 (float) e aggiunta all'insieme di conoscenza
good = FuzzyTermType("good", FuzzyTerm.TYPE_gaussianShape, [5., 1.])
food.addFuzzyTerm(good)

# creazione LeftGaussianShape con coordinate 2 e 1 (float) e aggiunta all'insieme di conoscenza
rancid = FuzzyTermType("rancid", FuzzyTerm.TYPE_leftGaussianShape, [2., 1.])
food.addFuzzyTerm(rancid)

# creazione RightGaussianShape con coordinate 8 e 1 (float) e aggiunta all'insieme di conoscenza
delicious = FuzzyTermType("delicious", FuzzyTerm.TYPE_rightGaussianShape, [8., 1.])
food.addFuzzyTerm(delicious)

# creazione Pi-Shaped con coordinate 2, 4, 6 e 8  (float) e aggiunta all'insieme di conoscenza
good = FuzzyTermType("good", FuzzyTerm.TYPE_piShape, [2., 4., 6., 8.])
food.addFuzzyTerm(good)

# creazione Z-shape con coordinate 2 e 4 (float) e aggiunta all'insieme di conoscenza
rancid = FuzzyTermType("rancid", FuzzyTerm.TYPE_zShape, [2., 4.])
food.addFuzzyTerm(rancid)

# creazione S-shape con coordinate 6 e 8 (float) e aggiunta all'insieme di conoscenza
delicious = FuzzyTermType("delicious", FuzzyTerm.TYPE_rightGaussianShape, [6., 8.])
food.addFuzzyTerm(delicious)

# creazione Singleton Shape con coordinate 5  (float) e aggiunta all'insieme di conoscenza
good = FuzzyTermType("good", FuzzyTerm.TYPE_singletonShape, [5.])
food.addFuzzyTerm(good)

#creazione oggetto MamdaniRB1 con aggiunta regole mandami
rbMam = MamdaniRuleBaseType("MamdaniRB1")
tipper.addRuleBase(rbMam)

#creazione regola 1 con nome regola connettore metodo operazione e peso
rule1 = FuzzyRuleType("rule1", None, None, "or", "MAX", None, None, 1.)

#creazione clausole antecedenti alle regole
ant1 = AntecedentType()
ant1.addClause(ClauseType(food, rancid))
ant1.addClause(ClauseType(service, poor, "very"))

rule1.setAntecedent(ant1)

# creazione clausole conseguenti alle regole
con1 = ConsequentType()
con1.addThenClause(ClauseType(tip, cheap))

rule1.setConsequent(con1)

#aggiunta alle regole Mamdani
rbMam.addRule(rule1)

# lettura file
str_xml = "XMLFiles/TipperMamdani1.xml"
tipper1 = Py4jfml.load(str_xml)

#scrittura file
str_xmlOutput = "XMLFiles/ourFS.xml"
Py4jfml.writeFSTtoXML(tipper, str_xmlOutput)