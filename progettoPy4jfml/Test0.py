import progettoPy4jfml.Py4jfml
import shutil
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()


class Test:
    #Creazione oggetto tipper
    tipper = progettoPy4jfml.Py4jfml.FuzzyInferenceSystem("tipper")

    #creazione dell'oggetto kb e aggiunta all'insieme di conoscenza fuzzy
    kb = progettoPy4jfml.Py4jfml.KnowledgeBaseType()
    tipper.setKnowledgeBase(kb)

    # creazione variabile tip con nome service dominio sinistro 0 e dominion destro 10
    tip = progettoPy4jfml.Py4jfml.FuzzyVariableType("tip", 0., 10.)
    kb.addVariable(tip)

    # creazione leftLinear con coordinate 0 e 1 e aggiunta all'insieme di conoscenza
    cheap = progettoPy4jfml.Py4jfml.FuzzyTermType("cheap",
                                                  progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_leftLinearShape,
                                                  [0., 1.])

    # creazione triangolarShape con coordinate 1,2 e 3 e aggiunta all'insieme di conoscenza
    poor = progettoPy4jfml.Py4jfml.FuzzyTermType("cheap",
                                                 progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_triangularShape,
                                                 [1., 2., 3.])

    tip.addFuzzyTerm(poor)

    #creazione variabile service con nome service dominio sinistro 0 e dominion destro 10
    service = progettoPy4jfml.Py4jfml.FuzzyVariableType("service", 0.0, 10.0)
    kb.addVariable(service)

    # creazione leftLinear con coordinate 0 e 1 e aggiunta all'insieme di conoscenza
    poor = progettoPy4jfml.Py4jfml.FuzzyTermType("poor",
                                                 progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_leftLinearShape,
                                                 [0., 1.])

    #creazione triangolarShape con coordinate 1,2 e 3 e aggiunta all'insieme di conoscenza
    poor = progettoPy4jfml.Py4jfml.FuzzyTermType("poor",
                                                 progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_triangularShape,
                                                 [1., 2., 3.])

    service.addFuzzyTerm(poor)

    # creazione variabile food con nome food dominio sinistro 0 e dominio destro 10 e aggiunta all'insieme di conoscenza
    food = progettoPy4jfml.Py4jfml.FuzzyVariableType("food", 0.0, 10.0)
    kb.addVariable(food)

    #creazione triangolarShape con coordinate 0,2 e 4 (float) e aggiunta all'insieme di conoscenza
    rancid = progettoPy4jfml.Py4jfml.FuzzyTermType("rancid",
                                                   progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_triangularShape,
                                                   [0., 2., 4.])
    food.addFuzzyTerm(rancid)

    # creazione Left LinearShape con coordinate 0 e 4 (float) e aggiunta all'insieme di conoscenza
    rancid = progettoPy4jfml.Py4jfml.FuzzyTermType("rancid",
                                                   progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_leftLinearShape,
                                                   [0., 4.])
    food.addFuzzyTerm(rancid)

    # creazione Right LinearShape con coordinate 4 e 10(float) e aggiunta all'insieme di conoscenza
    delicious = progettoPy4jfml.Py4jfml.FuzzyTermType("delicious",
                                                      progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_rightLinearShape,
                                                      [4.,10.])
    food.addFuzzyTerm(delicious)

    # creazione TrapezoidalShape con coordinate 0,1,3 e 4(float) e aggiunta all'insieme di conoscenza
    rancid = progettoPy4jfml.Py4jfml.FuzzyTermType("rancid",
                                                   progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_trapezoidShape,
                                                   [0.,1.,3.,4.])
    food.addFuzzyTerm(rancid)

    # creazione RectangularShape con coordinate 4 e 7 (float) e aggiunta all'insieme di conoscenza
    good = progettoPy4jfml.Py4jfml.FuzzyTermType("good",
                                                 progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_rectangularShape,
                                                 [4.,7.])
    food.addFuzzyTerm(good)

    # creazione GaussianShape con coordinate 5 e 1 (float) e aggiunta all'insieme di conoscenza
    good = progettoPy4jfml.Py4jfml.FuzzyTermType("good",
                                                 progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_gaussianShape,
                                                 [5., 1.])
    food.addFuzzyTerm(good)

    # creazione GaussianShape con coordinate 5 e 1 (float) e aggiunta all'insieme di conoscenza
    good = progettoPy4jfml.Py4jfml.FuzzyTermType("good",
                                                 progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_gaussianShape,
                                                 [5., 1.])
    food.addFuzzyTerm(good)

    # creazione LeftGaussianShape con coordinate 2 e 1 (float) e aggiunta all'insieme di conoscenza
    rancid = progettoPy4jfml.Py4jfml.FuzzyTermType("rancid",
                                                   progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_leftGaussianShape,
                                                   [2., 1.])
    food.addFuzzyTerm(rancid)

    # creazione RightGaussianShape con coordinate 8 e 1 (float) e aggiunta all'insieme di conoscenza
    delicious = progettoPy4jfml.Py4jfml.FuzzyTermType("delicious",
                                                      progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_rightGaussianShape,
                                                      [8., 1.])
    food.addFuzzyTerm(delicious)

    # creazione Pi-Shaped con coordinate 2, 4, 6 e 8  (float) e aggiunta all'insieme di conoscenza
    good = progettoPy4jfml.Py4jfml.FuzzyTermType("good",
                                                 progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_piShape,
                                                 [2., 4., 6., 8.])
    food.addFuzzyTerm(good)

    # creazione Z-shape con coordinate 2 e 4 (float) e aggiunta all'insieme di conoscenza
    rancid = progettoPy4jfml.Py4jfml.FuzzyTermType("rancid",
                                                   progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_zShape,
                                                   [2., 4.])
    food.addFuzzyTerm(rancid)

    # creazione S-shape con coordinate 6 e 8 (float) e aggiunta all'insieme di conoscenza
    delicious = progettoPy4jfml.Py4jfml.FuzzyTermType("delicious",
                                                      progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_rightGaussianShape,
                                                      [6., 8.])
    food.addFuzzyTerm(delicious)


    # creazione Singleton Shape con coordinate 5  (float) e aggiunta all'insieme di conoscenza
    good = progettoPy4jfml.Py4jfml.FuzzyTermType("good",
                                                 progettoPy4jfml.Py4jfml.FuzzyTerm.TYPE_singletonShape,
                                                 [5.])
    food.addFuzzyTerm(good)



    #creazione oggetto MamdaniRB1 con aggiunta regole mandami
    rbMam = progettoPy4jfml.Py4jfml.MamdaniRuleBaseType("MamdaniRB1");
    tipper.addRuleBase(rbMam); #forse modificare metodo add chiedere professore

    #creazione regola 1 con nome regola connettore metodo che connette e peso
    rule1 = progettoPy4jfml.Py4jfml.FuzzyRuleType("rule1", "or", "MAX", 1.)

    ant1 = progettoPy4jfml.Py4jfml.AntecedentType()
    ant1.addClause(progettoPy4jfml.Py4jfml.ClauseType(food, rancid, ""))#chiedere se python non sceglie in automatico il costruttor
    ant1.addClause(progettoPy4jfml.Py4jfml.ClauseType(service, poor, "very"))

    rule1.setAntecedent(ant1)
    con1 = progettoPy4jfml.Py4jfml.ConsequentType()

    con1.addThenClause(progettoPy4jfml.Py4jfml.ClauseType(tip, cheap, ""))#chiedere se python non sceglie in automatico il costruttore da usare
    rule1.setConsequent(con1)
    rbMam.addRule(rule1)
    
    # lettura file
    xml = open(tipper.xml, "r").read()
    tipper = progettoPy4jfml.Py4jfml.PY4JFML.load(xml)

    #scrittura
    xmlOutput = open("./XMLFiles/ourFS.xml", "w")
    fst = progettoPy4jfml.Py4jfml.FuzzySystemType
    progettoPy4jfml.Py4jfml.PY4JFML.writeFSTtoXML(fst,xmlOutput)




