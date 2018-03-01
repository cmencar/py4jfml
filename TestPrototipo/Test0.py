import prototipo0.FuzzyInferenceSystem
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class Test:
    #Creazione oggetto tipper
    tipper = prototipo0.FuzzyInferenceSystem.FuzzyInferenceSystem("tipper")

    #creazione dell'oggetto kb e aggiunta all'insieme di conoscenza fuzzy
    kb = prototipo0.FuzzyInferenceSystem.KnowledgeBaseType()
    tipper.setKnowledgeBase(kb)

    #creazione variabile food con nome food dominio sinistro 0 e dominio destro 10 e aggiunta all'insieme di conoscenza
    food = prototipo0.FuzzyInferenceSystem.FuzzyVariableType("food", 0.0, 10.0)
    kb.addVariable(food)

    #creazione triangolarShape con coordinate 0,2 e 4 (float) e aggiunta all'insieme di conoscenza
    rancid = prototipo0.FuzzyInferenceSystem.FuzzyTermType("rancid",
                                                           prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_triangularShape,
                                                           [0., 2., 4.])
    food.addFuzzyTerm(rancid)

    # creazione Left LinearShape con coordinate 0 e 4 (float) e aggiunta all'insieme di conoscenza
    rancid = prototipo0.FuzzyInferenceSystem.FuzzyTermType("rancid",
                                                           prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_leftLinearShape,
                                                           [0., 4.])
    food.addFuzzyTerm(rancid)

    # creazione Right LinearShape con coordinate 4 e 10(float) e aggiunta all'insieme di conoscenza
    delicious = prototipo0.FuzzyInferenceSystem.FuzzyTermType("delicious",
                                                           prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_rightLinearShape,
                                                           [4.,10.])
    food.addFuzzyTerm(delicious)

    # creazione TrapezoidalShape con coordinate 0,1,3 e 4(float) e aggiunta all'insieme di conoscenza
    rancid = prototipo0.FuzzyInferenceSystem.FuzzyTermType("rancid",
                                                           prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_trapezoidShape,
                                                           [0.,1.,3.,4.])
    food.addFuzzyTerm(rancid)

    # creazione RectangularShape con coordinate 4 e 7 (float) e aggiunta all'insieme di conoscenza
    good = prototipo0.FuzzyInferenceSystem.FuzzyTermType("good",
                                                           prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_rectangularShape,
                                                           [4.,7.])
    food.addFuzzyTerm(good)

    # creazione GaussianShape con coordinate 5 e 1 (float) e aggiunta all'insieme di conoscenza
    good = prototipo0.FuzzyInferenceSystem.FuzzyTermType("good",
                                                         prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_gaussianShape,
                                                         [5., 1.])
    food.addFuzzyTerm(good)

    # creazione GaussianShape con coordinate 5 e 1 (float) e aggiunta all'insieme di conoscenza
    good = prototipo0.FuzzyInferenceSystem.FuzzyTermType("good",
                                                         prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_gaussianShape,
                                                         [5., 1.])
    food.addFuzzyTerm(good)

    # creazione LeftGaussianShape con coordinate 2 e 1 (float) e aggiunta all'insieme di conoscenza
    rancid = prototipo0.FuzzyInferenceSystem.FuzzyTermType("rancid",
                                                         prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_leftGaussianShape,
                                                         [2., 1.])
    food.addFuzzyTerm(rancid)

    # creazione RightGaussianShape con coordinate 8 e 1 (float) e aggiunta all'insieme di conoscenza
    delicious = prototipo0.FuzzyInferenceSystem.FuzzyTermType("delicious",
                                                           prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_rightGaussianShape,
                                                           [8., 1.])
    food.addFuzzyTerm(delicious)

    # creazione Pi-Shaped con coordinate 2, 4, 6 e 8  (float) e aggiunta all'insieme di conoscenza
    good = prototipo0.FuzzyInferenceSystem.FuzzyTermType("good",
                                                         prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_piShape,
                                                         [2., 4., 6., 8.])
    food.addFuzzyTerm(good)

    # creazione Z-shape con coordinate 2 e 4 (float) e aggiunta all'insieme di conoscenza
    rancid = prototipo0.FuzzyInferenceSystem.FuzzyTermType("rancid",
                                                           prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_zShape,
                                                           [2., 4.])
    food.addFuzzyTerm(rancid)

    # creazione S-shape con coordinate 6 e 8 (float) e aggiunta all'insieme di conoscenza
    delicious = prototipo0.FuzzyInferenceSystem.FuzzyTermType("delicious",
                                                              prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_rightGaussianShape,
                                                              [6., 8.])
    food.addFuzzyTerm(delicious)


    # creazione Singleton Shape con coordinate 5  (float) e aggiunta all'insieme di conoscenza
    good = prototipo0.FuzzyInferenceSystem.FuzzyTermType("good",
                                                         prototipo0.FuzzyInferenceSystem.FuzzyTerm.TYPE_singletonShape,
                                                         [5.])
    food.addFuzzyTerm(good)

    #creazione oggetto MamdaniRB1 con aggiunta regole mandami
    rbMam = prototipo0.FuzzyInferenceSystem.MamdaniRuleBaseType("MamdaniRB1");
    tipper.addRuleBase(rbMam); #forse modificare metodo add chiedere professore

    #creazione regola 1 con nome regola connettore metodo che connette e peso
    rule1 = prototipo0.FuzzyInferenceSystem.FuzzyRuleType("rule1", "or", "MAX", 1.)

    ant1 = prototipo0.FuzzyInferenceSystem.AntecedentType()
    #ant1.addClause(kb,"rancid") #chiedere che valori bisogna inserire
    rule1.setAntecedent(ant1)
    con1 = prototipo0.FuzzyInferenceSystem.ConsequentType()
    #con1 = prototipo0.FuzzyInferenceSystem.ConsequentType.addThenClause(tip,cheap)
    rule1.setConsequent(con1)
    rbMam.addRule(rule1)
