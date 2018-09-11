import py4jfml.FuzzyInferenceSystem as fis
import py4jfml.aggregated.AndAggregatedType as aat
import py4jfml.aggregated.OrAggregatedType as oat
import py4jfml.membershipfunction.CircularDefinitionType as cdt
import py4jfml.membershipfunction.CircularMembershipFunction as circularmf
import py4jfml.membershipfunction.CustomMembershipFunction as custommf
import py4jfml.membershipfunction.CustomShapeType as customst
import py4jfml.membershipfunction.LeftGaussianMembershipFunction as lgmf
import py4jfml.membershipfunction.LeftLinearMembershipFunction as llmf
import py4jfml.membershipfunction.PiShapedMembershipFunction as psmf
import py4jfml.membershipfunction.PointSetMonotonicShapeType as psmst
import py4jfml.membershipfunction.PointSetShapeType as psst
import py4jfml.membershipfunction.PointType as pt
import py4jfml.membershipfunction.RectangularMembershipFunction as rmf
import py4jfml.membershipfunction.RightGaussianMembershipFunction as rgmf
import py4jfml.membershipfunction.RightLinearMembershipFunction as rlmf
import py4jfml.membershipfunction.SingletonMembershipFunction as smf
import py4jfml.membershipfunction.SShapeMembershipFunction as ssmf
import py4jfml.membershipfunction.TrapezoidMembershipFunction as tramf
import py4jfml.membershipfunction.TriangularMembershipFunction as trimf
import py4jfml.membershipfunction.ZShapeMembershipFunction as zsmf
import py4jfml.operator.AndLogicalType as alt
import py4jfml.operator.OrLogicalType as olt
import py4jfml.parameter.ParameterType as pt
import py4jfml.parameter.OneParamType as opt
import py4jfml.parameter.TwoParamType as tpt
import py4jfml.parameter.ThreeParamType as trpt
import py4jfml.parameter.FourParamType as fpt
import py4jfml.term.AggregatedFuzzyTermType as aft
import py4jfml.term.CircularTermType as ctt
import py4jfml.term.FuzzyTermType as ftt
import py4jfml.term.TskTermType as tsktt
import py4jfml.term.TsukamotoTermType as ttt

import cProfile


#Valutazione dell'efficienza della libreria Py4JFML
pr = cProfile.Profile()
pr.enable()
fis.FuzzyInferenceSystem()
pr.disable()
pr.print_stats(sort="calls")