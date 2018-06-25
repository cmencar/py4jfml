import py4jfml.Py4jfml as fml
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class IrisMamdaniTest1:
    #FuzzyInference
    iris = fml.FuzzyInferenceSystem("iris - MAMDANI")
    #KnowledgeBase
    kb = fml.KnowledgeBaseType()
    iris.setKnowledgeBase(kb)

    #FUZZY VARIABLE PetalWidth
    pw = fml.FuzzyVariableType("PetalWidth", 0.1, 2.5)

    #FUZZY TERM low
    pw_low = fml.FuzzyTermType("low", fml.FuzzyTerm.TYPE_trapezoidShape, [0.1, 0.1, 0.244, 1.087])
    pw.addFuzzyTerm(pw_low)

    #FUZZY TERM medium
    pw_medium = fml.FuzzyTermType("medium", fml.FuzzyTerm.TYPE_trapezoidShape, [0.244, 1.087, 1.419, 1.906])
    pw.addFuzzyTerm(pw_medium)

    #FUZZY TERM high
    pw_high = fml.FuzzyTermType("high", fml.FuzzyTerm.TYPE_trapezoidShape, [1.419, 1.906, 2.5, 2.5])
    pw.addFuzzyTerm(pw_high)

    #Aggiunta
    kb.addVariable(pw)

    #OUTPUT CLASS irisClass
    irisClass = fml.FuzzyVariableType("irisClass", 1., 3.)
    irisClass.setDefaultValue(1.)
    irisClass.setAccumulation("MAX")
    irisClass.setDefuzzifierName("MOM")
    irisClass.setType("output")

    #FUZZY TERM setosa
    irisClass_setosa = fml.FuzzyTermType("setosa", fml.FuzzyTerm.TYPE_triangularShape, [1., 1., 2.])
    irisClass.addFuzzyTerm(irisClass_setosa)

    #FUZZY TERM virginica
    irisClass_virginica = fml.FuzzyTermType("virginica", fml.FuzzyTerm.TYPE_triangularShape, [1., 2., 3.])
    irisClass.addFuzzyTerm(irisClass_virginica)

    #FUZZY TERM versicolor
    irisClass_versicolor = fml.FuzzyTermType("versicolor", fml.FuzzyTerm.TYPE_triangularShape, [2., 3., 3.])
    irisClass.addFuzzyTerm(irisClass_versicolor)

    kb.addVariable(irisClass)

    #RULE BASE
    rb = fml.MamdaniRuleBaseType("rulebase-iris")

    #RULE 1
    r1 = fml.FuzzyRuleType("rule1", "and", "MIN", 1.0)

    #aggiunta regole antecedenti
    ant1 = fml.AntecedentType()
    ant1.addClause(fml.ClauseType(pw, pw_low))

    #aggiunta regole conseguenti
    con1 = fml.ConsequentType()
    con1.addThenClause(fml.ClauseType(irisClass, irisClass_setosa))
    r1.setAntecedent(ant1)
    r1.setConsequent(con1)

    rb.addRule(r1)

    #RULE 2
    r2 = fml.FuzzyRuleType("rule2", "and", "MIN", 1.0)
    ant2 = fml.AntecedentType()
    ant2.addClause(fml.ClauseType(pw, pw_medium))
    con2 = fml.ConsequentType()
    con2.addThenClause(fml.ClauseType(irisClass, irisClass_virginica))
    r2.setAntecedent(ant2)
    r2.setConsequent(con2)

    rb.addRule(r2)

    #RULE 3
    r3 = fml.FuzzyRuleType("rule3", "and", "MIN", 1.0)
    ant3 = fml.AntecedentType()
    ant3.addClause(fml.ClauseType(pw, pw_high))
    con3 = fml.ConsequentType()
    con3.addThenClause(fml.ClauseType(irisClass, irisClass_versicolor))
    r3.setAntecedent(ant3)
    r3.setConsequent(con3)

    rb.addRule(r3)

    iris.addRuleBase(rb)

    #WRITTING IRIS EXAMPLE INTO AN XML FILE
    str_xml = "C:\\Users\\andrea\\PycharmProjects\\untitled\\progettoPy4jfml\\XMLFiles\\IrisMamdani1.xml"
    fml.PY4JFML.writeFSTtoXML(iris,str_xml)

class IrisMamdaniTest2:
    # FuzzyInference
    iris = fml.FuzzyInferenceSystem("iris - MAMDANI")
    # KnowledgeBase
    kb = fml.KnowledgeBaseType()
    iris.setKnowledgeBase(kb)

    #FUZZY VARIABLE SepalLength
    sl = fml.FuzzyVariableType("SepalLength", 4.3, 7.9)

    #FUZZY TERM low
    sl_low = fml.FuzzyTermType("low", fml.FuzzyTerm.TYPE_trapezoidShape, [4.3, 4.3, 5.019, 6.048])
    sl.addFuzzyTerm(sl_low)
    # FUZZY TERM  medium
    sl_medium = fml.FuzzyTermType("medium", fml.FuzzyTerm.TYPE_triangularShape,[5.019, 6.048, 7.05])
    sl.addFuzzyTerm(sl_medium)
    # FUZZY TERM high
    sl_high = fml.FuzzyTermType("high", fml.FuzzyTerm.TYPE_trapezoidShape,[6.048, 7.05, 7.9, 7.9])
    sl.addFuzzyTerm(sl_high)
    # FUZZY TERM NOT(low)
    sl_not_low = fml.FuzzyTermType("NOT(low)", fml.FuzzyTerm.TYPE_trapezoidShape, [4.3, 4.3, 5.019, 6.048])
    sl_not_low.setComplement("true");
    sl.addFuzzyTerm(sl_not_low);

    kb.addVariable(sl);

    # FUZZY VARIABLE SepalWidth
    sw = fml.FuzzyVariableType("SepalWidth", 2., 4.4)

    # FUZZY TERM low
    sw_low = fml.FuzzyTermType("low", fml.FuzzyTerm.TYPE_trapezoidShape,[2., 2., 2.585, 3.119])
    sw.addFuzzyTerm(sw_low)
    # FUZZY TERM medium
    sw_medium = fml.FuzzyTermType("medium", fml.FuzzyTerm.TYPE_triangularShape,[2.585, 3.119, 3.758])
    sw.addFuzzyTerm(sw_medium)
    # FUZZY TERM high
    sw_high = fml.FuzzyTermType("high", fml.FuzzyTerm.TYPE_trapezoidShape, [3.119, 3.758, 4.4, 4.4])
    sw.addFuzzyTerm(sw_high)
    # FUZZY TERM NOT(high)
    sw_not_high = fml.FuzzyTermType("NOT(high)", fml.FuzzyTerm.TYPE_trapezoidShape,[3.119, 3.758, 4.4, 4.4])
    sw_not_high.setComplement("true")
    sw.addFuzzyTerm(sw_not_high)

    kb.addVariable(sw)

    #FUZZY VARIABLE PetalLength
    pl = fml.FuzzyVariableType("PetalLength", 1., 6.9)

    #FUZZY TERM low
    pl_low = fml.FuzzyTermType("low", fml.FuzzyTerm.TYPE_trapezoidShape, [1., 1., 1.464, 4.432])
    pl.addFuzzyTerm(pl_low);
    # FUZZY TERM medium
    pl_medium = fml.FuzzyTermType("medium", fml.FuzzyTerm.TYPE_triangularShape,[1.464, 4.432, 5.826])
    pl.addFuzzyTerm(pl_medium)
    # FUZZY TERM high
    pl_high = fml.FuzzyTermType("high", fml.FuzzyTerm.TYPE_trapezoidShape, [4.432, 5.826, 6.9, 6.9])
    pl.addFuzzyTerm(pl_high)
    # FUZZY TERM NOT(low)
    pl_not_low = fml.FuzzyTermType("NOT(low)", fml.FuzzyTerm.TYPE_trapezoidShape, [1., 1., 1.464, 4.432])

    pl_not_low.setComplement("true")
    pl.addFuzzyTerm(pl_not_low)

    kb.addVariable(pl)

    # FUZZY VARIABLE PetalWidth
    pw = fml.FuzzyVariableType("PetalWidth", 0.1, 2.5)

    # FUZZY TERM low
    pw_low = fml.FuzzyTermType("low", fml.FuzzyTerm.TYPE_trapezoidShape,[0., 0.1, 0.244, 1.337])
    pw.addFuzzyTerm(pw_low)
    # FUZZY TERM medium
    pw_medium = fml.FuzzyTermType("medium", fml.FuzzyTerm.TYPE_triangularShape, [0.244, 1.337, 2.074])
    pw.addFuzzyTerm(pw_medium)
    # FUZZY TERM high
    pw_high = fml.FuzzyTermType("high", fml.FuzzyTerm.TYPE_trapezoidShape,[1.337, 2.074, 2.5, 2.5])
    pw.addFuzzyTerm(pw_high)

    kb.addVariable(pw)

    # OUTPUT CLASS irisClass
    irisClass = fml.FuzzyVariableType("irisClass", 1., 3.)
    irisClass.setDefaultValue(1.)
    irisClass.setAccumulation("MAX")
    irisClass.setDefuzzifierName("LM")
    irisClass.setType("output")

    # FUZZY TERM setosa
    irisClass_setosa = fml.FuzzyTermType("setosa", fml.FuzzyTerm.TYPE_singletonShape, [1.])
    irisClass.addFuzzyTerm(irisClass_setosa);

    # FUZZY TERM virginica
    irisClass_virginica = fml.FuzzyTermType("virginica", fml.FuzzyTerm.TYPE_singletonShape, [2.])
    irisClass.addFuzzyTerm(irisClass_virginica)

    # FUZZY TERM versicolor
    irisClass_versicolor = fml.FuzzyTermType("versicolor", fml.FuzzyTerm.TYPE_singletonShape, [3.])
    irisClass.addFuzzyTerm(irisClass_versicolor)

    kb.addVariable(irisClass)

    # RULE BASE
    rb = fml.MamdaniRuleBaseType("rulebase-iris")
    # RULE 1
    r1 = fml.FuzzyRuleType("rule1", "and", "MIN", 1.0)

    ant1 = fml.AntecedentType()
    ant1.addClause(fml.ClauseType(pw, pw_low))
    con1 = fml.ConsequentType()
    con1.addThenClause(fml.ClauseType(irisClass, irisClass_setosa))
    r1.setAntecedent(ant1)
    r1.setConsequent(con1)

    rb.addRule(r1)

    # RULE 2
    r2 = fml.FuzzyRuleType("rule2", "and", "MIN", 1.0)

    ant2 = fml.AntecedentType()
    ant2.addClause(fml.ClauseType(sw, sw_not_high))
    ant2.addClause(fml.ClauseType(pl, pl_medium))
    ant2.addClause(fml.ClauseType(pw, pw_medium))
    con2 = fml.ConsequentType()
    con2.addThenClause(fml.ClauseType(irisClass, irisClass_virginica))
    r2.setAntecedent(ant2)
    r2.setConsequent(con2)

    rb.addRule(r2);

    # RULE 3
    r3 = fml.FuzzyRuleType("rule3", "and", "MIN", 1.0)

    ant3 = fml.AntecedentType()
    ant3.addClause(fml.ClauseType(sl, sl_not_low))
    ant3.addClause(fml.ClauseType(pl, pl_not_low))
    ant3.addClause(fml.ClauseType(pw, pw_high))

    con3 = fml.ConsequentType()
    con3.addThenClause(fml.ClauseType(irisClass, irisClass_versicolor))
    r3.setAntecedent(ant3)
    r3.setConsequent(con3)

    rb.addRule(r3)

    iris.addRuleBase(rb)

    # WRITTING IRIS EXAMPLE INTO AN XML FILE
    str_xml = "C:\\Users\\andrea\\PycharmProjects\\untitled\\progettoPy4jfml\\XMLFiles\\IrisMamdani2.xml"
    fml.PY4JFML.writeFSTtoXML(iris, str_xml)


class IrisMamdaniTest3:
    iris = fml.FuzzyInferenceSystem("iris - MAMDANI")

    # KNOWLEDGEBASE
    kb = fml.KnowledgeBaseType()
    iris.setKnowledgeBase(kb)

    # FUZZY VARIABLE PetalWidth
    pw = fml.FuzzyVariableType("PetalWidth", 0.1, 2.5)

    # FUZZY TERM low
    pw_lowLIN = fml.FuzzyTermType("lowLIN", fml.FuzzyTerm.TYPE_leftLinearShape, [0., 0.8])
    pw.addFuzzyTerm(pw_lowLIN)

    # lowGAU
    pw_lowGAU = fml.FuzzyTermType("lowGAU", fml.FuzzyTerm.TYPE_leftGaussianShape,[0.5, 0.2])
    pw.addFuzzyTerm(pw_lowGAU)
    # lowPI
    pw_lowPi = fml.FuzzyTermType("lowPi", fml.FuzzyTerm.TYPE_piShape, [1., 1.2])
    pw.addFuzzyTerm(pw_lowPi)
    # lowZ
    pw_lowZ = fml.FuzzyTermType("lowZ", fml.FuzzyTerm.TYPE_zShape, [1., 0.2])
    pw.addFuzzyTerm(pw_lowZ)

    # FUZZY TERM medium TRI
    pw_mediumTRI = fml.FuzzyTermType("mediumTRI", fml.FuzzyTerm.TYPE_triangularShape,[0.5, 1., 1.5])
    pw.addFuzzyTerm(pw_mediumTRI)
    # TRA
    pw_mediumTRA = fml.FuzzyTermType("mediumTRA", fml.FuzzyTerm.TYPE_trapezoidShape, [0.25, 1., 2., 2.25])
    pw.addFuzzyTerm(pw_mediumTRA)
    # GAU
    pw_mediumGAU = fml.FuzzyTermType("mediumGAU", fml.FuzzyTerm.TYPE_gaussianShape, [1., 0.2])
    pw.addFuzzyTerm(pw_mediumGAU)
    # REC
    pw_mediumREC = fml.FuzzyTermType("mediumREC", fml.FuzzyTerm.TYPE_rectangularShape, [1., 2.])
    pw.addFuzzyTerm(pw_mediumREC)

    # FUZZY TERM high LIN
    pw_highLIN = fml.FuzzyTermType("highLIN", fml.FuzzyTerm.TYPE_rightLinearShape, [1.5, 2.5])
    pw.addFuzzyTerm(pw_highLIN)
    # GAU
    pw_highGAU = fml.FuzzyTermType("highGAU", fml.FuzzyTerm.TYPE_rightGaussianShape, [2., 0.2])
    pw.addFuzzyTerm(pw_highGAU)
    # SIN
    pw_highSIN = fml.FuzzyTermType("highSIN", fml.FuzzyTerm.TYPE_singletonShape, [2.])
    pw.addFuzzyTerm(pw_highSIN)
    pw_highS = fml.FuzzyTermType("highS", fml.FuzzyTerm.TYPE_sShape, [2., 0.2])
    pw.addFuzzyTerm(pw_highS)

    kb.addVariable(pw)

    # OUTPUT CLASS irisClass
    irisClass = fml.FuzzyVariableType("irisClass", 1., 3.)
    irisClass.setDefaultValue(1.)
    irisClass.setAccumulation("MAX")
    irisClass.setDefuzzifierName("LM")
    irisClass.setType("output")

    # FUZZY TERM setosa
    irisClass_setosa = fml.FuzzyTermType("setosa", fml.FuzzyTerm.TYPE_singletonShape, [1.])
    irisClass.addFuzzyTerm(irisClass_setosa)

    # FUZZY TERM  virginica
    irisClass_virginica = fml.FuzzyTermType("virginica", fml.FuzzyTerm.TYPE_singletonShape, [2.])
    irisClass.addFuzzyTerm(irisClass_virginica)

    # FUZZY TERM versicolor
    irisClass_versicolor = fml.FuzzyTermType("versicolor", fml.FuzzyTerm.TYPE_singletonShape, [3.])
    irisClass.addFuzzyTerm(irisClass_versicolor)

    kb.addVariable(irisClass)

    # RULE BASE
    rb = fml.MamdaniRuleBaseType("rulebase-iris")

    # RULE 1
    r1 = fml.FuzzyRuleType("rule1", "and", "MIN", 1.0)

    #regole antecendenti
    ant1 = fml.AntecedentType()
    ant1.addClause(fml.ClauseType(pw, pw_lowLIN))
    #regole conseguenti
    con1 = fml.ConsequentType()
    con1.addThenClause(fml.ClauseType(irisClass, irisClass_setosa))

    r1.setAntecedent(ant1)
    r1.setConsequent(con1)

    rb.addRule(r1)

    # RULE 2
    r2 = fml.FuzzyRuleType("rule2", "and", "MIN", 1.0)

    ant2 = fml.AntecedentType()
    ant2.addClause(fml.ClauseType(pw, pw_lowGAU))

    con2 = fml.ConsequentType()
    con2.addThenClause(fml.ClauseType(irisClass, irisClass_setosa))
    r2.setAntecedent(ant2)
    r2.setConsequent(con2)
    rb.addRule(r2)

    # RULE 3
    r3 = fml.FuzzyRuleType("rule3", "and", "MIN", 1.0)

    ant3 = fml.AntecedentType()
    ant3.addClause(fml.ClauseType(pw, pw_lowPi))

    con3 = fml.ConsequentType()
    con3.addThenClause(fml.ClauseType(irisClass, irisClass_setosa))

    r3.setAntecedent(ant3)
    r3.setConsequent(con3)
    rb.addRule(r3)

    # RULE 4
    r4 = fml.FuzzyRuleType("rule4", "and", "MIN", 1.0)

    ant4 = fml.AntecedentType()
    ant4.addClause(fml.ClauseType(pw, pw_lowZ))

    con4 = fml.ConsequentType()
    con4.addThenClause(fml.ClauseType(irisClass, irisClass_setosa))

    r4.setAntecedent(ant4)
    r4.setConsequent(con4)

    rb.addRule(r4)

    # RULE 5
    r5 = fml.FuzzyRuleType("rule5", "and", "MIN", 1.0)

    ant5 = fml.AntecedentType()
    ant5.addClause(fml.ClauseType(pw, pw_mediumTRI))

    con5 = fml.ConsequentType()
    con5.addThenClause(fml.ClauseType(irisClass, irisClass_virginica))

    r5.setAntecedent(ant5)
    r5.setConsequent(con5)

    rb.addRule(r5)

    # RULE 6
    r6 = fml.FuzzyRuleType("rule6", "and", "MIN", 1.0)

    ant6 = fml.AntecedentType()
    ant6.addClause(fml.ClauseType(pw, pw_mediumTRA))

    con6 = fml.ConsequentType()
    con6.addThenClause(fml.ClauseType(irisClass, irisClass_virginica))

    r6.setAntecedent(ant6)
    r6.setConsequent(con6)

    rb.addRule(r6)

    # RULE 7
    r7 = fml.FuzzyRuleType("rule7", "and", "MIN", 1.0)

    ant7 = fml.AntecedentType()
    ant7.addClause(fml.ClauseType(pw, pw_mediumGAU))

    con7 = fml.ConsequentType()
    con7.addThenClause(fml.ClauseType(irisClass, irisClass_virginica))

    r7.setAntecedent(ant7)
    r7.setConsequent(con7)

    rb.addRule(r7)

    # RULE 8
    r8 = fml.FuzzyRuleType("rule8", "and", "MIN", 1.0)

    ant8 = fml.AntecedentType()
    ant8.addClause(fml.ClauseType(pw, pw_mediumREC))

    con8 = fml.ConsequentType()
    con8.addThenClause(fml.ClauseType(irisClass, irisClass_virginica))
    r8.setAntecedent(ant8)
    r8.setConsequent(con8)
    rb.addRule(r8)

    # RULE 9
    r9 = fml.FuzzyRuleType("rule9", "and", "MIN", 1.0)

    ant9 = fml.AntecedentType()
    ant9.addClause(fml.ClauseType(pw, pw_highLIN))

    con9 = fml.ConsequentType()
    con9.addThenClause(fml.ClauseType(irisClass, irisClass_versicolor))

    r9.setAntecedent(ant9)
    r9.setConsequent(con9)

    rb.addRule(r9)

    # RULE 10
    r10 = fml.FuzzyRuleType("rule10", "and", "MIN", 1.0)
    ant10 = fml.AntecedentType()
    ant10.addClause(fml.ClauseType(pw, pw_highGAU))

    con10 = fml.ConsequentType()
    con10.addThenClause(fml.ClauseType(irisClass, irisClass_versicolor))

    r10.setAntecedent(ant10)
    r10.setConsequent(con10)

    rb.addRule(r10)

    # RULE 11
    r11 = fml.FuzzyRuleType("rule11", "and", "MIN", 1.0)

    ant11 = fml.AntecedentType()
    ant11.addClause(fml.ClauseType(pw, pw_highSIN))

    con11 = fml.ConsequentType()
    con11.addThenClause(fml.ClauseType(irisClass, irisClass_versicolor))

    r11.setAntecedent(ant11)
    r11.setConsequent(con11)
    rb.addRule(r11)

    # RULE 12

    r12 = fml.FuzzyRuleType("rule12", "and", "MIN", 1.0)

    ant12 = fml.AntecedentType()
    ant12.addClause(fml.ClauseType(pw, pw_highS))

    con12 = fml.ConsequentType()
    con12.addThenClause(fml.ClauseType(irisClass, irisClass_versicolor))

    r12.setAntecedent(ant12)
    r12.setConsequent(con12)

    rb.addRule(r12)

    iris.addRuleBase(rb)

    # WRITTING IRIS EXAMPLE INTO AN XML FILE
    str_xml = "C:\\Users\\andrea\\PycharmProjects\\untitled\\progettoPy4jfml\\XMLFiles\\IrisMamdani3.xml"
    fml.PY4JFML.writeFSTtoXML(iris, str_xml)