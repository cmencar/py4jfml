'''
This class creates an XML file with the definition of a Mamdani-type FLS for the Tipper regression problem:
    1) Two input variables (food and service) with Triangular, rightLinear, leftGaussian, gaussian and rightGaussian membership functions
    2) Example of using AggregatedFuzzyVariableType and AggregatedFuzzyTermType in the definition of the variable "quality" as a combination of terms
    3) five rules:
        + Use of the variable quality in rule4 and rule5
'''

from py4j.java_gateway import JavaGateway
from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem
from py4jfml.aggregated.AndAggregatedType import AndAggregatedType
from py4jfml.aggregated.OrAggregatedType import OrAggregatedType
from py4jfml.enumeration.InterpolationMethodType import InterpolationMethodType
from py4jfml.knowledgebase.KnowledgeBaseType import KnowledgeBaseType
from py4jfml.knowledgebasevariable.AggregatedFuzzyVariableType import AggregatedFuzzyVariableType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.membershipfunction.PointSetShapeType import PointSetShapeType
from py4jfml.membershipfunction.PointType import PointType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.term.AggregatedFuzzyTermType import AggregatedFuzzyTermType
from py4jfml.term.FuzzyTermType import FuzzyTermType

tipper = FuzzyInferenceSystem("tipper - MAMDANI")

# KNOWLEDGE BASE
kb = KnowledgeBaseType()
tipper.setKnowledgeBase(kb)

# FUZZY VARIABLE food
food = FuzzyVariableType("food", 0., 10.)

# FUZZY TERM rancid
rancid = FuzzyTermType("rancid", FuzzyTermType.TYPE_triangularShape,[0., 2., 5.5])
food.addFuzzyTerm(rancid)

# FUZZY TERM delicious
delicious = FuzzyTermType("delicious", FuzzyTermType.TYPE_rightLinearShape,[5.5, 10.])
food.addFuzzyTerm(delicious)

kb.addVariable(food)

# FUZZY VARIABLE service
service = FuzzyVariableType("service", 0., 10.)

# FUZZY TERM poor
poor = FuzzyTermType("poor", FuzzyTermType.TYPE_leftGaussianShape, [0., 2.])
service.addFuzzyTerm(poor)

# FUZZY TERM good
good = FuzzyTermType("good", FuzzyTermType.TYPE_gaussianShape, [5., 4.])
service.addFuzzyTerm(good)

# FUZZY TERM excellent
excellent = FuzzyTermType("excellent", FuzzyTermType.TYPE_rightGaussianShape, [10., 2.])
service.addFuzzyTerm(excellent)

kb.addVariable(service)

# AGGREGATED FUZZY VARIABLE quality
quality = AggregatedFuzzyVariableType("quality")

# AGGREGATED FUZZY TERM acceptable
acceptable = AggregatedFuzzyTermType("acceptable")
acceptable_t1 = ClauseType(food, delicious)
acceptable_t2 = ClauseType(service, good)
acceptable_t3 = ClauseType(service, excellent)
acceptable_or = OrAggregatedType(c1=acceptable_t2, c2=acceptable_t3)
acceptable_and = AndAggregatedType(c1=acceptable_t1, term2=acceptable_or)
acceptable.setAnd(acceptable_and)

# AGGREGATED FUZZY TERM bad
bad = AggregatedFuzzyTermType("bad")
bad_t1 = ClauseType(food, rancid)
bad_t2 = ClauseType(service, poor)
bad_or = OrAggregatedType(c1=bad_t1, c2=bad_t2)
bad.setOr(bad_or)

quality.addAggregatedFuzzyTerm(acceptable)
quality.addAggregatedFuzzyTerm(bad)

kb.addVariable(quality)

# FUZZY VARIABLE tip
tip = FuzzyVariableType("tip", 0., 20.)
tip.setDefaultValue(0.)
tip.setAccumulation("MAX")
tip.setDefuzzifierName("COG")
tip.setType("output")

# FUZZY TERMcheap
gateway = JavaGateway()
points1 = []
points1.append(PointType(0., 1.))
points1.append(PointType(1., 1.))
points1.append(PointType(2., 0.6))
points1.append(PointType(3., 0.4))
points1.append(PointType(4., 0.))
ps = PointSetShapeType(points=points1)
ps.setInterpolationMethod(InterpolationMethodType.LINEAR)
cheap = FuzzyTermType("cheap", point=ps)
tip.addFuzzyTerm(cheap)

# FUZZY TERM average
average = FuzzyTermType("average", FuzzyTermType.TYPE_triangularShape,[5., 10., 15.])
tip.addFuzzyTerm(average)

# FUZZY TERM generous
generous = FuzzyTermType("generous", FuzzyTermType.TYPE_triangularShape,[10., 15., 20.])
tip.addFuzzyTerm(generous)

kb.addVariable(tip)

print(tipper)

# DA CONTINUARE