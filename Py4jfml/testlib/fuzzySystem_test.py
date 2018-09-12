from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem
from py4jfml.Py4Jfml import Py4jfml
from py4jfml.defuzzifier.DefuzzifierCenterOfArea import DefuzzifierCenterOfArea
from py4jfml.defuzzifier.DefuzzifierCenterOfGravity import DefuzzifierCenterOfGravity
from py4jfml.defuzzifier.DefuzzifierCenterOfGravitySingletons import DefuzzifierCenterOfGravitySingletons
from py4jfml.enumeration.MonotonicInterpolationMethodType import MonotonicInterpolationMethodType
from py4jfml.jaxb.FuzzySystemType import FuzzySystemType
from py4jfml.knowledgebase.KnowledgeBaseType import KnowledgeBaseType
from py4jfml.knowledgebasevariable.AggregatedFuzzyVariableType import AggregatedFuzzyVariableType
from py4jfml.knowledgebasevariable.AnYaDataCloudType import AnYaDataCloudType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.knowledgebasevariable.TskVariableType import TskVariableType
from py4jfml.knowledgebasevariable.TsukamotoVariableType import TsukamotoVariableType
from py4jfml.membershipfunction.CircularDefinitionType import CircularDefinitionType
from py4jfml.membershipfunction.PointSetMonotonicShapeType import PointSetMonotonicShapeType
from py4jfml.membershipfunction.PointType import PointType
from py4jfml.operator.OrLogicalType import OrLogicalType
from py4jfml.rule.AnYaAntecedentType import AnYaAntecedentType
from py4jfml.rule.AnYaRuleType import AnYaRuleType
from py4jfml.rule.AntecedentType import AntecedentType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.rule.ConsequentType import ConsequentType
from py4jfml.rule.FuzzyRuleType import FuzzyRuleType
from py4jfml.rule.TskConsequentType import TskConsequentType
from py4jfml.rule.TskFuzzyRuleType import TskFuzzyRuleType
from py4jfml.rulebase.AnYaRuleBaseType import AnYaRuleBaseType
from py4jfml.rulebase.FuzzySystemRuleBase import FuzzySystemRuleBase
from py4jfml.rulebase.MamdaniRuleBaseType import MamdaniRuleBaseType
from py4jfml.rulebase.TskRuleBaseType import TskRuleBaseType
from py4jfml.rulebase.TsukamotoRuleBaseType import TsukamotoRuleBaseType
from py4jfml.term.FuzzyTerm import FuzzyTerm
from py4jfml.term.FuzzyTermType import FuzzyTermType

#A FUZZY VARIABLE
from py4jfml.term.TskTerm import TskTerm
from py4jfml.term.TskTermType import TskTermType
from py4jfml.term.TsukamotoTermType import TsukamotoTermType

domainLeft = 0.0
domainRight = 255.
force =  FuzzyVariableType("Force", domainLeft, domainRight)
force.setDefaultValue(0.0)
force.setAccumulation("MAX")
force.setType("output")
# FUZZY TERM VNEG
termName = "very negative"
force_vneg =  FuzzyTermType(termName, FuzzyTermType.TYPE_trapezoidShape,[ 0.0, 0.0, 48.0, 88.0])
# FUZZY TERM NEG
force_neg =  FuzzyTermType("negative", FuzzyTermType.TYPE_triangularShape,[ 48.0, 88.0, 128.0])
# FUZZY TERM NEU
force_neu =  FuzzyTermType("zero", FuzzyTermType.TYPE_triangularShape,[ 88.0, 128.0, 168.0])


print()

defuzzCoA = DefuzzifierCenterOfArea(2., 4., [force_vneg])
defuzzCoA.setValue(5., 15.)
nameCoa = "CenterOfArea"
if defuzzCoA.getName()==nameCoa:
    print("DefuzzifierCenterOfArea test case 1 (name) passed.")
else:
    print("DefuzzifierCenterOfArea test case 1 (name) failed.")
if defuzzCoA.getValueY(5.)==15.:
    print("DefuzzifierCenterOfArea test case 2 (value y) passed.")
else:
    print("DefuzzifierCenterOfArea test case 2 (value y) failed.")

defuzzCoG = DefuzzifierCenterOfGravity(2., 4., [force_vneg])
force.setDefuzzifier(defuzzCoG)
COG = "COG"
if force.getDefuzzifierName()==COG:
    print("DefuzzifierCenterOfGravity and FuzzyVariableType test case 1 (defuzzifier, name) passed.")
else:
    print("DefuzzifierCenterOfGravity and FuzzyVariableType test case 1 (defuzzifier, name) failed.")

defuzzCoGS = DefuzzifierCenterOfGravitySingletons(2.,4.)
defuzzCoGS.setDiscrete(True)
defuzzCoGS.setPoint(5.,15.)
if defuzzCoGS.getDiscreteValue(5.)==15.:
    print("DefuzzifierCenterOfGravitySingletons test case 1 (discrete value) passed.")
else:
    print("DefuzzifierCenterOfGravitySingletons test case 1 (discrete value) failed.")

print()

name = "quality"
output = "output"
aggregatedFuzzyVar = AggregatedFuzzyVariableType(name)
aggregatedFuzzyVar.setType("output")
if aggregatedFuzzyVar.getName()==name:
    print("AggregatedFuzzyVariableType test case 1 (name) passed.")
else:
    print("AggregatedFuzzyVariableType test case 1 (name) failed.")
if(aggregatedFuzzyVar.getType()==output):
    print("AggregatedFuzzyVariableType test case 2 (type) passed.")
else:
    print("AggregatedFuzzyVariableType test case 2 (type) failed.")

force.setDefuzzifierName(COG)
if force.getDefuzzifierName()==COG:
    print("FuzzyVariableType test case 1 (defuzzifier name) passed.")
else:
    print("FuzzyVariableType test case 1 (defuzzifier name) failed.")
if force.getDomainleft()==domainLeft:
    print("FuzzyVariableType test case 2 (domain left) passed.")
else:
    print("FuzzyVariableType test case 2 (domain left) failed.")
domainRight=+1.
force.setDomainright(domainRight)
if force.getDomainright()==domainRight:
    print("FuzzyVariableType test case 3 (domain right) passed.")
else:
    print("FuzzyVariableType test case 3 (domain right) failed.")
terms = [force_vneg,force_neg]
for t in terms:
    force.addFuzzyTerm(t)
if force.getFuzzyTerm(0).getName() == termName:
    print("FuzzyVariableType test case (fuzzy term name) 4 passed.")
else:
    print("FuzzyVariableType test case (fuzzy term name) 4 failed.")

anyaName="food"
anyaVar = AnYaDataCloudType(name=anyaName, terms=[1.0, 1.7, 4.0, 3.2])
if anyaVar.getName()==anyaName:
    print("AnYaDataCloudType test case 1 (anya name) passed.")
else:
    print("AnYaDataCloudType test case 1 (anya name) failed.")
thirdTerm=4.2
anyaVar.setTerms([2.0, 2.7, 5.0, thirdTerm])
if anyaVar.getTerms()[3]==thirdTerm:
    print("AnYaDataCloudType test case (term) 2 passed.")
else:
    print("AnYaDataCloudType test case (term) 2 failed.")

#TSUKAMOTO VARIABLE
domainRight=20.0
tsukamotoVar = TsukamotoVariableType(name="tip", domainLeft=0.0, domainRight=domainRight)
tsukamotoVar.setDefaultValue(0.0)
comb = "WA"
tsukamotoVar.setCombination(comb)
if tsukamotoVar.isInput()==False:
    print("TsukamotoVariableType test case 1 (input) passed.")
else:
    print("TsukamotoVariableType test case 1 (input) failed.")
if tsukamotoVar.getCombination()==comb:
    print("TsukamotoVariableType test case 2 (combination) passed.")
else:
    print("TsukamotoVariableType test case 2 (combination) failed.")
domainRight=+1.
tsukamotoVar.setDomainright(domainRight)
if tsukamotoVar.getDomainright()==domainRight:
    print("TsukamotoVariableType test case 3 (domain right) passed.")
else:
    print("TsukamotoVariableType test case 3 (domain right) failed.")
tsukamotoVar.setType(output)
if tsukamotoVar.getType()==output:
    print("TsukamotoVariableType test case 4 (type) passed.")
else:
    print("TsukamotoVariableType test case 4 (type) failed.")
#TSUKAMOTO TERM cheap
points1 = [PointType(0.0, 1.0),PointType(1.0, 1.0),PointType(2.0, 0.6),PointType(3.0, 0.4),PointType(4.0, 0.0)]
psm = PointSetMonotonicShapeType(points=points1)
psm.setInterpolationMethod(MonotonicInterpolationMethodType.CUBIC)
name="cheap"
cheap = TsukamotoTermType(name=name, psm=psm)
tsukamotoVar.addTsukamotoTerm(t=cheap)
if tsukamotoVar.getTerm(name).getName()==name:
    print("TsukamotoVariableType test case 5 (term name) passed.")
else:
    print("TsukamotoVariableType test case 5 (term name) failed.")

#TSK VARIABLE tip
tskVar = TskVariableType("tip")
tskVar.setDefaultValue(0.0)
tskVar.setCombination(comb)
#TSK TERM average
average = TskTermType(name="average", order=TskTerm._ORDER_0, coeff=[1.6])
tskVar.addTskTerm(average)
if tskVar.getTerms()[0].getName()==average.getName():
    print("TskVariableType test case 1 (term name) passed.")
else:
    print("TskVariableType test case 1 (term name) failed.")
tskVar.setType(output)
if tskVar.getType()==output:
    print("TskVariableType test case 2 (type) passed.")
else:
    print("TskVariableType test case 2 (type) failed.")
if tskVar.getCombination()==comb:
    print("TskVariableType test case 3 (combination) passed.")
else:
    print("TskVariableType test case 3 (combination) failed.")
kb = KnowledgeBaseType()
kb.addVariable(aggregatedFuzzyVar)
kb.addVariable(anyaVar)
kb.addVariable(tsukamotoVar)
kb.addVariable(tskVar)
kb.addVariable(force)
if kb.getVariable("tip").getCombination()=="WA":
    print("KnowledgeBaseType test case passed.")
else:
    print("KnowledgeBaseType test case failed.")

print()

# FUZZY VARIABLE
ang = FuzzyVariableType("Angle", 0.0, 255.0)
ang_vneg = FuzzyTermType("very negative", FuzzyTermType.TYPE_trapezoidShape, [0.0, 0.0, 48.0, 88.0])
ang.addFuzzyTerm(ang_vneg)
ang_or1 = OrLogicalType("BSUM", "very negative", "negative")
ang_c1 = CircularDefinitionType(orLogical=ang_or1, var=ang)
nameTerm="very negative or negative"
ang_vneg_or_neg = FuzzyTermType(nameTerm, circular=ang_c1)
ang.addFuzzyTerm(ang_vneg_or_neg)
name1="ChangeAngle"
ca = FuzzyVariableType(name1, 0.0, 255.0)
ca_vneg = FuzzyTermType(nameTerm, FuzzyTermType.TYPE_trapezoidShape,[0.0, 0.0, 48.0, 88.0])
ca.addFuzzyTerm(ca_vneg)
ca_or1 = OrLogicalType("BSUM", "very negative", "negative")
ca_c1 = CircularDefinitionType(orLogical=ca_or1, var=ca)
ca_vneg_or_neg = FuzzyTermType(nameTerm, circular=ca_c1)
ca.addFuzzyTerm(ca_vneg_or_neg)
ant1 = AntecedentType()
ant1.addClause(ClauseType(ang, ang_vneg_or_neg))
ant1.addClause(ClauseType(ca, ca_vneg_or_neg))
if ant1.getClauses()[1].getVariable().getName()==name1:
    print("AntecedentType, ClauseType, FuzzyVariableType test case passed.")
else:
    print("AntecedentType, ClauseType, FuzzyVariableType test case failed.")
if ant1.getClauses()[1].getTerm().getName()==nameTerm:
    print("AntecedentType, ClauseType, FuzzyTermType test case passed.")
else:
    print("AntecedentType, ClauseType, FuzzyTermType test case failed.")
ant1 = AnYaAntecedentType(dataCloud=anyaVar)
name=str(anyaVar.getName())+"modified"
anyaVar.setName(name)
ant1.setDataCloudName(anyaVar.getName())
if ant1.getDataCloudName()==name:
    print("AnYaAntecedentType, AnYaDataCloudType test case passed.")
else:
    print("AntecedentType, AnYaDataCloudType test case failed.")
anyarule = AnYaRuleType()
anyarule.aggregation([9.,1.])
anyarule.setAnYaAntecedent(AnYaAntecedentType(AnYaDataCloudType(name,[8.,9.])))
if anyarule.getAnYaAntecedent().getDataCloudName().getName()==name:
    print("AnYaAntecedentType, AnYaRuleType, AnYaDataCloudType test case passed.")
else:
    print("AntecedentType, AnYaRuleType, AnYaDataCloudType test case failed.")
fuzzyrule = FuzzyRuleType("rule1", connector="and", connectorMethod="MIN", weight=1.0)
ant1 = AntecedentType()
ant1.addClause(ClauseType(ang, ang_vneg_or_neg))
con1 = ConsequentType()
irisClass = FuzzyVariableType("irisClass", 1.0, 3.0)
irisClass.setDefaultValue(1.)
irisClass.setAccumulation("MAX")
defuzz="LM"
irisClass.setDefuzzifierName(defuzz)
irisClass.setType("output")
irisClass_setosa = FuzzyTermType("setosa", FuzzyTerm.TYPE_singletonShape, [1.0])
irisClass.addFuzzyTerm(irisClass_setosa)
con1.addThenClause(ClauseType(irisClass, irisClass_setosa))
fuzzyrule.setAntecedent(ant1)
fuzzyrule.setConsequent(con1)
if fuzzyrule.getConsequent().getThen().getClause()[0].getVariable().getDefuzzifier().getName()=="LeftMostMax":
    print("ConsequentType, ConsequentClausesType FuzzyRuleType, FuzzyVariableType, Defuzzifier test case passed.")
else:
    print("ConsequentType, ConsequentClausesType, FuzzyRuleType, FuzzyVariableType, Defuzzifier test case failed.")
name="tsk example"
a = TskFuzzyRuleType(name)
a.orFunction([5.,6.])
a.andFunction([4.,6.])
if a.getName()==name:
    print("TskFuzzyRuleType test case 1 (names) passed.")
else:
    print("TskFuzzyRuleType test case 1 (names) passed.")
if a.getOrMethod()=="MAX":
    print("TskFuzzyRuleType test case 2 (orMethod) passed.")
else:
    print("TskFuzzyRuleType test case 2 (orMethod) passed.")
r1 = TskFuzzyRuleType("rule1", connector="and", connectorMethod="MIN", weight=1.0)
ant1 = AntecedentType()
ant1.addClause(ClauseType(ang, ang_vneg_or_neg))
ant1.addClause(ClauseType(ca, ca_vneg_or_neg))
con1 = TskConsequentType()
force = TskVariableType("Force")
force.setDefaultValue(0.0)
force.setCombination("WA")
force.setType("output")
name="very negative"
force_vneg = TskTermType(name, TskTerm._ORDER_1, [48.0, 0.01, 0.02])
force.addTskTerm(force_vneg)
con1.addTskThenClause(variable=force, term=force_vneg)
r1.setAntecedent(ant1)
r1.setTskConsequent(con1)
if r1.getAntecedent().getClauses()[1].getVariable().getType()=="input":
    print("TskFuzzyRuleType, AntecedentType, ClauseType, TskVariableType test case passed.")
else:
    print("TskFuzzyRuleType, AntecedentType, ClauseType, TskVariableType test case passed.")
if r1.getTskConsequent().getTskThen().getTskClause()[0].getTerm().getName()==name:
    print("TskFuzzyRuleType, TskConsequentType, TskConsequentClausesType, TskClauseType test case passed.")
else:
    print("TskFuzzyRuleType, TskConsequentType, TskConsequentClausesType, TskClauseType test case failed.")

print()

rb = AnYaRuleBaseType("rulebase1")
rb.addAnYaRule(anyarule)
if rb.getRuleBaseSystemTypeName()=="anYa":
    print("AnYaRuleBaseType test case passed.")
else:
    print("AnYaRuleBaseType test case failed.")
if rb.getAnYaRules()[0].getAnYaAntecedent().getDataCloudName().getName()=="foodmodified":
    print("AnYaRuleBaseType, AnYaAntecedentType, AnYaRuleType, AnYaDataCloudType test case passed.")
else:
    print("AnYaRuleBaseType, AnYaAntecedentType, AnYaRuleType, AnYaDataCloudType test case failed.")
rb = MamdaniRuleBaseType("rulebase1")
rb.addRule(fuzzyrule)
if rb.getRuleBaseSystemTypeName()=="mamdani":
    print("MamdaniRuleBaseType test case passed.")
else:
    print("MamdaniRuleBaseType test case failed.")
if rb.getRules()[0].getConsequent().getThen().getClause()[0].getVariable().getDefuzzifier().getName()=="LeftMostMax":
    print("MamdaniRuleBaseType, ConsequentType, ConsequentClausesType FuzzyRuleType, FuzzyVariableType, Defuzzifier test case passed.")
else:
    print("MamdaniRuleBaseType, ConsequentType, ConsequentClausesType, FuzzyRuleType, FuzzyVariableType, Defuzzifier test case failed.")

rb1 = TskRuleBaseType("rulebase1", FuzzySystemRuleBase.TYPE_TSK)
rb1.setActivationMethod("PROD")
rb1.addTskRule(r1)
if rb1.getTskRules()[0].getAntecedent().getClauses()[1].getVariable().getType()=="input":
    print("TskRuleBaseType, TskFuzzyRuleType, AntecedentType, ClauseType, TskVariableType test case passed.")
else:
    print("TskRuleBaseType, TskFuzzyRuleType, AntecedentType, ClauseType, TskVariableType test case passed.")
if rb1.getTskRules()[0].getTskConsequent().getTskThen().getTskClause()[0].getTerm().getName()==name:
    print("TskRuleBaseType, TskFuzzyRuleType, TskConsequentType, TskConsequentClausesType, TskClauseType test case passed.")
else:
    print("TskRuleBaseType, TskFuzzyRuleType, TskConsequentType, TskConsequentClausesType, TskClauseType test case failed.")

rb = TsukamotoRuleBaseType("rulebase1")
rb.addRule(fuzzyrule)
if rb.getRuleBaseSystemTypeName()=="tsukamoto":
    print("TsukamotoRuleBaseType test case passed.")
else:
    print("TsukamotoRuleBaseType test case failed.")
if rb.getRules()[0].getConsequent().getThen().getClause()[0].getVariable().getDefuzzifier().getName()=="LeftMostMax":
    print("TsukamotoRuleBaseType, ConsequentType, ConsequentClausesType FuzzyRuleType, FuzzyVariableType, Defuzzifier test case passed.")
else:
    print("TsukamotoRuleBaseType, ConsequentType, ConsequentClausesType, FuzzyRuleType, FuzzyVariableType, Defuzzifier test case failed.")

print()

fis = FuzzySystemType()
fis.addRuleBase(rb)
fis.addRuleBase(rb1)
fis.setName("fis")
if fis.getAllRuleBase()[1].getRuleBaseSystemTypeName()=="tsk":
    print("FuzzySystemType test case passed.")
else:
    print("FuzzySystemType test case failed.")


Py4jfml.kill()

