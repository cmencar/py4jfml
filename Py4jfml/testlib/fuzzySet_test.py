from py4jfml.Py4Jfml import Py4jfml
from py4jfml.aggregated.AndAggregatedType import AndAggregatedType
from py4jfml.aggregated.OrAggregatedType import OrAggregatedType
from py4jfml.enumeration.MonotonicInterpolationMethodType import MonotonicInterpolationMethodType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.membershipfunction.LeftGaussianMembershipFunction import LeftGaussianMembershipFunction
from py4jfml.membershipfunction.LeftLinearMembershipFunction import LeftLinearMembershipFunction
from py4jfml.membershipfunction.PiShapedMembershipFunction import PiShapedMembershipFunction
from py4jfml.membershipfunction.PointSetMonotonicShapeType import PointSetMonotonicShapeType
from py4jfml.membershipfunction.PointSetShapeType import PointSetShapeType
from py4jfml.membershipfunction.PointType import PointType
from py4jfml.membershipfunction.RectangularMembershipFunction import RectangularMembershipFunction
from py4jfml.membershipfunction.RightGaussianMembershipFunction import RightGaussianMembershipFunction
from py4jfml.membershipfunction.RightLinearMembershipFunction import RightLinearMembershipFunction
from py4jfml.membershipfunction.SShapeMembershipFunction import SShapeMembershipFunction
from py4jfml.membershipfunction.SingletonMembershipFunction import SingletonMembershipFunction
from py4jfml.membershipfunction.TrapezoidMembershipFunction import TrapezoidMembershipFunction
from py4jfml.membershipfunction.TriangularMembershipFunction import TriangularMembershipFunction
from py4jfml.membershipfunction.ZShapeMembershipFunction import ZShapeMembershipFunction
from py4jfml.operator.AndLogicalType import AndLogicalType
from py4jfml.operator.OrLogicalType import OrLogicalType
from py4jfml.parameter.FourParamType import FourParamType
from py4jfml.parameter.OneParamType import OneParamType
from py4jfml.parameter.ParameterType import ParameterType
from py4jfml.parameter.ThreeParamType import ThreeParamType
from py4jfml.parameter.TwoParamType import TwoParamType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.term.AggregatedFuzzyTermType import AggregatedFuzzyTermType
from py4jfml.term.CircularTermType import CircularTermType
from py4jfml.term.FuzzyTermType import FuzzyTermType


# methods test of package aggregated
# FUZZY VARIABLE food
from py4jfml.term.TskTerm import TskTerm
from py4jfml.term.TskTermType import TskTermType
from py4jfml.term.TsukamotoTermType import TsukamotoTermType

food = FuzzyVariableType("food", 0., 10.)

# FUZZY TERM rancid
rancid = FuzzyTermType("rancid", FuzzyTermType.TYPE_triangularShape,[0., 2., 5.5])
food.addFuzzyTerm(rancid)

# FUZZY TERM delicious
delicious = FuzzyTermType("delicious", FuzzyTermType.TYPE_rightLinearShape,[5.5, 10.])
food.addFuzzyTerm(delicious)

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

acceptable_t1 = ClauseType(food, delicious)
acceptable_t2 = ClauseType(service, good)
acceptable_t3 = ClauseType(service, excellent)
acceptable_or = OrAggregatedType(c1=acceptable_t2, c2=acceptable_t3)
acceptable_and = AndAggregatedType(c1=acceptable_t1, term2=acceptable_or)

try:
    property_tnorm = "property tNorm"
    acceptable_and.setTNorm(property_tnorm)
    assert property_tnorm == acceptable_and.getTNorm()

    property_tConorm = "property tConorm"
    acceptable_or.setTConorm(property_tConorm)
    assert  property_tConorm == acceptable_or.getTConorm()

    print("Testing of package aggregated: SUCCESSFUL")
except AssertionError:
    print("Testing of package aggregated: FAILED")



# methods test of package operator
ca_or1 = OrLogicalType("BSUM", "very negative", "negative")
ca_and1 = AndLogicalType("BSUM", "very negative", "negative")

try:
    ca_or1.setTConorm(property_tConorm)
    assert property_tConorm == ca_or1.getTConorm()

    ca_and1.setTNorm(property_tnorm)
    assert property_tnorm == ca_and1.getTNorm()

    print("Testing of package operator: SUCCESSFUL")
except AssertionError:
    print("Testing of package operator: FAILED")



#Methods test of package parameter
p = ParameterType()
p1 = OneParamType()
p2 = TwoParamType()
p3 = ThreeParamType()
p4 = FourParamType()

try:
    prop = "property"
    p.setValue(prop)
    assert p.getValue() == prop

    value1 = 0.5
    p1.setParam1(value1)
    assert p1.getParam1() == value1
    assert p1.getParameter(1) == value1
    assert p1.getParameterLength() == 1

    value2 = 1.1
    p2.setParam1(value1)
    p2.setParam2(value2)
    assert p2.getParam1() == value1
    assert p2.getParam2() == value2
    assert p2.getParameter(1) == value1
    assert p2.getParameter(2) == value2
    assert p2.getParameterLength() == 2

    value3 = 1.5
    p3.setParam1(value1)
    p3.setParam2(value2)
    p3.setParam3(value3)
    assert p3.getParam1() == value1
    assert p3.getParam2() == value2
    assert p3.getParam3() == value3
    assert p3.getParameter(1) == value1
    assert p3.getParameter(2) == value2
    assert p3.getParameter(3) == value3
    assert p3.getParameterLength() == 3

    value4 = 2.4
    p4.setParam1(value1)
    p4.setParam2(value2)
    p4.setParam3(value3)
    p4.setParam4(value4)
    assert p4.getParam1() == value1
    assert p4.getParam2() == value2
    assert p4.getParam3() == value3
    assert p4.getParam4() == value4
    assert p4.getParameter(1) == value1
    assert p4.getParameter(2) == value2
    assert p4.getParameter(3) == value3
    assert p4.getParameter(4) == value4
    assert p4.getParameterLength() == 4

    print("Testing of package parameter: SUCCESSFUL")
except AssertionError:
    print("Testing of package parameter: FAILED")



# Methods test of package term
# FUZZY TERM
ft = FuzzyTermType(name="negative", type_java=FuzzyTermType.TYPE_triangularShape, param=[48.0, 88.0, 128.0])

# AGGREGATED FUZZY TERM
aft = AggregatedFuzzyTermType("acceptable")
acceptable_t1 = ClauseType(food, delicious)
acceptable_t2 = ClauseType(service, good)
acceptable_t3 = ClauseType(service, excellent)
acceptable_or = OrAggregatedType(c1=acceptable_t2, c2=acceptable_t3)
acceptable_and = AndAggregatedType(c1=acceptable_t1, term2=acceptable_or)
aft.setAnd(acceptable_and)

# CIRCULAR TERM TYPE
cir  = CircularTermType("Name Circular Term")

# TSK TERM TYPE
tskTerm = TskTermType(name="cheap", order=TskTerm._ORDER_1, coeff=[1.9, 5.6, 6.0])

# TSUKAMOTO TERM TYPE
param = [20.0, 10.0]
tsu = TsukamotoTermType(name="generous", type_java=FuzzyTermType.TYPE_rightGaussianShape, paramList=param)
try:
    #FuzzyTermType
    assert str(ft) == str(ft.copy())

    complement = "property complement"
    ft.setComplement(complement)
    assert ft.getComplement() == complement

    name = "Name ft"
    ft.setName(name)
    assert ft.getName() == name

    #AggregatedFuzzyTermType
    name2 = "Name aft"
    aft.setName(name2)
    assert aft.getName() == name2

    #CircularTermType
    cir.setComplement(complement)
    assert cir.getComplement() == complement

    #TskTermType
    assert str(tskTerm) == str(tskTerm.copy())

    name3 = "Name TSK"
    tskTerm.setName(name3)
    assert tskTerm.getName() == name3

    order = TskTerm._ORDER_1
    tskTerm.setOrder(order)
    assert tskTerm.getOrder() == order

    #TsukamotoTermTypeo
    assert str(tsu) == str(tsu.copy())

    name4 = "Name TSUKAMOTO"
    tsu.setName(name4)
    assert tsu.getName() == name4

    tsu.setComplement(complement)
    assert tsu.getComplement() == complement

    print("Testing of package term: SUCCESSFUL")
except AssertionError:
    print("Testing of package term: FAILED")



# Methods test of package membershipfunction
domainLeft = 0.5
domainRight = 2.5
z = ZShapeMembershipFunction()
t = TriangularMembershipFunction()
trap = TrapezoidMembershipFunction()
ss = SShapeMembershipFunction()
sin = SingletonMembershipFunction()
rl = RightLinearMembershipFunction()
rgauss = RightGaussianMembershipFunction()
rmf = RectangularMembershipFunction()
o1 = PointType(x=0.8,y=9.6)
o2 = PointType(x=0.2,y=4.6)
pst = PointSetShapeType(domainLeft=domainLeft,domainRight=domainRight,points=[o1,o2])
psst = PointSetMonotonicShapeType(domainLeft=domainLeft,domainRight=domainRight,points=[o1,o2])
pi = PiShapedMembershipFunction(p=p1,domainLeft=domainLeft,domainRight=domainRight)
leftlin = LeftLinearMembershipFunction(p=p2,domainLeft=domainLeft,domainRight=domainRight)
leftgauss = LeftGaussianMembershipFunction(p=p3,domainLeft=domainLeft,domainRight=domainRight)

try:
    #ZShapeMembershipFunction
    assert z.getName() == "ZShapeMembershipFunction"

    z.setDomainLeft(domainLeft)
    z.setDomainRight(domainRight)
    assert z.getDomainRight() == domainRight
    assert z.getDomainLeft() == domainLeft

    #TriangularMembershipFunction
    assert t.getName() == "TriangularMembershipFunction"

    t.setDomainRight(domainRight)
    t.setDomainLeft(domainLeft)
    assert t.getDomainRight() == domainRight
    assert t.getDomainLeft() == domainLeft

    #TrapezoidMembershipFunction
    assert trap.getName() == "TrapezoidMembershipFunction"

    trap.setDomainRight(domainRight)
    trap.setDomainLeft(domainLeft)
    assert trap.getDomainRight() == domainRight
    assert trap.getDomainLeft() == domainLeft

    #SShapeMembershipFunction
    assert ss.getName() == "SShapeMembershipFunction"

    ss.setDomainLeft(domainLeft)
    ss.setDomainRight(domainRight)
    assert ss.getDomainRight() == domainRight
    assert ss.getDomainLeft() == domainLeft

    #SingletonMembershipFunction
    assert sin.getName() == "SingletonMembershipFunction"

    sin.setDomainRight(domainRight)
    sin.setDomainLeft(domainLeft)
    assert sin.getDomainRight() == domainRight
    assert sin.getDomainLeft() == domainLeft

    #RightLinearMembershipFunction
    assert rl.getName() == "RightLinearMembershipFunction"

    rl.setDomainLeft(domainLeft)
    rl.setDomainRight(domainRight)
    assert rl.getDomainLeft() == domainLeft
    assert rl.getDomainRight() == domainRight

    #RightGaussianMembershipFunction
    assert rgauss.getName() == "RightGaussianMembershipFunction"

    rgauss.setDomainRight(domainRight)
    rgauss.setDomainLeft(domainLeft)
    assert rgauss.getDomainLeft() == domainLeft
    assert rgauss.getDomainRight() == domainRight

    #RectangularMembershipFunction
    assert rmf.getName() == "RectangularMembershipFunction"

    rmf.setDomainLeft(domainLeft)
    rmf.setDomainRight(domainRight)
    assert rmf.getDomainLeft() == domainLeft
    assert rmf.getDomainRight() == domainRight

    #PointType
    assert o1.compare(o1,o1) == 0
    assert o1.compare(o1,o2) == 1
    assert o1.compare(o2,o1) == -1

    newX = 2.2
    newY = 3.5
    o1.setX(newX)
    o1.setY(newY)
    assert o1.getX() == newX
    assert o1.getY() == newY

    #PointSetShapeType
    assert pst.getName() == "PointSetShapeType"
    assert str(pst.copy()) == str(pst)

    degree = 5
    pst.setDegree(degree)
    assert pst.getDegree() == degree

    pst.setInterpolationMethod(MonotonicInterpolationMethodType.LINEAR)
    assert str(pst.getInterpolationMethod()) == MonotonicInterpolationMethodType.LINEAR.upper()

    pst.setDomainRight(domainRight)
    pst.setDomainLeft(domainLeft)
    assert pst.getDomainRight() == domainRight
    assert pst.getDomainLeft() == domainLeft

    #PointSetMonotonicShapeType
    assert psst.getName() == "PointSetMonotonicShapeType"

    psst.setInterpolationMethod(MonotonicInterpolationMethodType.LINEAR)
    assert str(psst.getInterpolationMethod()) == MonotonicInterpolationMethodType.LINEAR.upper()

    psst.setDomainRight(domainRight)
    psst.setDomainLeft(domainLeft)
    assert psst.getDomainRight() == domainRight
    assert psst.getDomainLeft() == domainLeft

    #PiShapedMembershipFunction
    assert pi.getName() == "PiShapedMembershipFunction"

    pi.setDomainRight(domainRight)
    pi.setDomainLeft(domainLeft)
    assert pi.getDomainRight() == domainRight
    assert pi.getDomainLeft() == domainLeft

    #LeftLinearMembershipFunction
    assert leftlin.getName() == "LeftLinearMembershipFunction"

    leftlin.setDomainRight(domainRight)
    leftlin.setDomainLeft(domainLeft)
    assert leftlin.getDomainRight() == domainRight
    assert leftlin.getDomainLeft() == domainLeft

    #LeftGaussianMembershipFunction
    assert leftgauss.getName() == "LeftGaussianMembershipFunction"

    leftgauss.setDomainRight(domainRight)
    leftgauss.setDomainLeft(domainLeft)
    assert leftgauss.getDomainRight() == domainRight
    assert leftgauss.getDomainLeft() == domainLeft

    print("Testing of package membershipfunction: SUCCESSFUL")
except AssertionError:
    print("Testing of package membershipfunction: FAILED")

Py4jfml.kill()