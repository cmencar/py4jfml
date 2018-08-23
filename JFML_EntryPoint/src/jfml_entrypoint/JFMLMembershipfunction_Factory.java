package jfml_entrypoint;

import java.util.List;

import jfml.knowledgebase.variable.KnowledgeBaseVariable;
import jfml.membershipfunction.CircularDefinitionType;
import jfml.membershipfunction.CircularMembershipFunction;
import jfml.membershipfunction.CustomMembershipFunction;
import jfml.membershipfunction.CustomShapeType;
import jfml.membershipfunction.GaussianMembershipFunction;
import jfml.membershipfunction.LeftGaussianMembershipFunction;
import jfml.membershipfunction.LeftLinearMembershipFunction;
import jfml.membershipfunction.PiShapedMembershipFunction;
import jfml.membershipfunction.PointSetMonotonicShapeType;
import jfml.membershipfunction.PointSetShapeType;
import jfml.membershipfunction.PointType;
import jfml.membershipfunction.RectangularMembershipFunction;
import jfml.membershipfunction.RightGaussianMembershipFunction;
import jfml.membershipfunction.RightLinearMembershipFunction;
import jfml.membershipfunction.SShapeMembershipFunction;
import jfml.membershipfunction.SingletonMembershipFunction;
import jfml.membershipfunction.TrapezoidMembershipFunction;
import jfml.membershipfunction.TriangularMembershipFunction;
import jfml.membershipfunction.ZShapeMembershipFunction;
import jfml.operator.AndLogicalType;
import jfml.operator.LogicalType;
import jfml.operator.OrLogicalType;
import jfml.parameter.Parameter;
import jfml.parameter.TwoParamType;

/**
 * This class allows to return class instances of the JFML package 'membershipfunction'.
 * 
 */
public class JFMLMembershipfunction_Factory {

	public CircularDefinitionType createCircularDefinitionType()
	{
		return new CircularDefinitionType();
	}
	
	public CircularDefinitionType createCircularDefinitionType(AndLogicalType and, OrLogicalType or, KnowledgeBaseVariable var)
	{
		return new CircularDefinitionType(and,or,var);
	}
	
	public CircularDefinitionType createCircularDefinitionType(LogicalType log, KnowledgeBaseVariable var)
	{
		return new CircularDefinitionType(log,var);
	}
	
	public CircularMembershipFunction createCircularMembershipFunction()
	{
		return new CircularMembershipFunction();
	}
	
	public CircularMembershipFunction createCircularMembershipFunction(CircularDefinitionType p)
	{
		return new CircularMembershipFunction(p);
	}
	
	public CircularMembershipFunction createCircularMembershipFunction(CircularDefinitionType p, float domainLeft, float domainRight)
	{
		return new CircularMembershipFunction(p,domainLeft,domainRight);
	}
	
	public CustomMembershipFunction createCustomMembershipFunction()
	{
		return new CustomMembershipFunction();
	}
	
	public CustomMembershipFunction createCustomMembershipFunction(CustomShapeType c)
	{
		return new CustomMembershipFunction(c);
	}
	
	public CustomMembershipFunction createCustomMembershipFunction(CustomShapeType customShape, float domainLeft, float domainRight)
	{
		return new CustomMembershipFunction(customShape,domainLeft,domainRight);
	}
	
	public CustomMembershipFunction createCustomMembershipFunction(Parameter p)
	{
		return new CustomMembershipFunction(p);
	}
	
	public CustomShapeType createCustomShapeType()
	{
		return new CustomShapeType();
	}
	
	public GaussianMembershipFunction createGaussianMembershipFunction()
	{
		return new GaussianMembershipFunction();
	}
	
	public GaussianMembershipFunction createGaussianMembershipFunction(Parameter p)
	{
		return new GaussianMembershipFunction(p);
	}
	
	public GaussianMembershipFunction createGaussianMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new GaussianMembershipFunction(p,domainLeft,domainRight);
	}
	
	public LeftGaussianMembershipFunction createLeftGaussianMembershipFunction()
	{
		return new LeftGaussianMembershipFunction();
	}
	
	public LeftGaussianMembershipFunction createLeftGaussianMembershipFunction(Parameter p)
	{
		return new LeftGaussianMembershipFunction(p);
	}
	
	public LeftGaussianMembershipFunction createLeftGaussianMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new LeftGaussianMembershipFunction(p,domainLeft,domainRight);
	}
	
	public LeftLinearMembershipFunction createLeftLinearMembershipFunction()
	{
		return new LeftLinearMembershipFunction();
	}
	
	public LeftLinearMembershipFunction createLeftLinearMembershipFunction(Parameter p)
	{
		return new LeftLinearMembershipFunction(p);
	}
	
	public LeftLinearMembershipFunction createLeftLinearMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new LeftLinearMembershipFunction(p,domainLeft,domainRight);
	}
	
	public PiShapedMembershipFunction createPiShapedMembershipFunction()
	{
		return new PiShapedMembershipFunction();
	}
	
	public PiShapedMembershipFunction createPiShapedMembershipFunction(Parameter p)
	{
		return new PiShapedMembershipFunction(p);
	}
	
	public PiShapedMembershipFunction createPiShapedMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new PiShapedMembershipFunction(p,domainLeft,domainRight);
	}
	
	public PointSetMonotonicShapeType createPointSetMonotonicShapeType()
	{
		return new PointSetMonotonicShapeType();
	}
	
	public PointSetMonotonicShapeType createPointSetMonotonicShapeType(float domainLeft, float domainRight)
	{
		return new PointSetMonotonicShapeType(domainLeft,domainRight);
	}
	
	public PointSetMonotonicShapeType createPointSetMonotonicShapeType(float domainLeft, float domainRight, List<PointType> points)
	{
		return new PointSetMonotonicShapeType(domainLeft,domainRight,points);
	}
	
	public PointSetMonotonicShapeType createPointSetMonotonicShapeType(List<PointType> points)
	{
		return new PointSetMonotonicShapeType(points);
	}
	
	public PointSetShapeType createPointSetShapeType()
	{
		return new PointSetShapeType();
	}
	
	public PointSetShapeType createPointSetShapeType(float domainLeft, float domainRight)
	{
		return new PointSetShapeType(domainLeft,domainRight);
	}
	
	public PointSetShapeType createPointSetShapeType(float domainLeft, float domainRight, List<PointType> points)
	{
		return new PointSetShapeType(domainLeft,domainRight,points);
	}
	
	public PointSetShapeType createPointSetShapeType(List<PointType> points)
	{
		return new PointSetShapeType(points);
	}
	
	public PointType createPointType()
	{
		return new PointType();
	}
	
	public PointType createPointType(float x, float y)
	{
		return new PointType(x,y);
	}
	
	public RectangularMembershipFunction createRectangularMembershipFunction(Parameter p)
	{
		return new RectangularMembershipFunction(p);
	}
	
	public RectangularMembershipFunction createRectangularMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new RectangularMembershipFunction(p,domainLeft,domainRight);
	}
	
	public RightGaussianMembershipFunction createRightGaussianMembershipFunction()
	{
		return new RightGaussianMembershipFunction();
	}
	
	public RightGaussianMembershipFunction createRightGaussianMembershipFunction(Parameter p)
	{
		return new RightGaussianMembershipFunction(p);
	}
	
	public RightGaussianMembershipFunction createRightGaussianMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new RightGaussianMembershipFunction(p,domainLeft,domainRight);
	}
	
	public RightLinearMembershipFunction createRightLinearMembershipFunction()
	{
		return new RightLinearMembershipFunction();
	}
	
	public RightLinearMembershipFunction createRightLinearMembershipFunction(Parameter p)
	{
		return new RightLinearMembershipFunction(p);
	}
	
	public RightLinearMembershipFunction createRightLinearMembershipFunction(TwoParamType p, float domainLeft, float domainRight)
	{
		return new RightLinearMembershipFunction(p,domainLeft,domainRight);
	}
	
	public SingletonMembershipFunction createSingletonMembershipFunction()
	{
		return new SingletonMembershipFunction();
	}
	
	public SingletonMembershipFunction createSingletonMembershipFunction(Parameter p)
	{
		return new SingletonMembershipFunction(p);
	}
	
	public SingletonMembershipFunction createSingletonMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new SingletonMembershipFunction(p,domainLeft,domainRight);
	}
	
	public SShapeMembershipFunction createSShapeMembershipFunction()
	{
		return new SShapeMembershipFunction();
	}
	
	public SShapeMembershipFunction createSShapeMembershipFunction(Parameter p)
	{
		return new SShapeMembershipFunction(p);
	}
	
	public SShapeMembershipFunction createSShapeMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new SShapeMembershipFunction(p,domainLeft,domainRight);
	}
	
	public TrapezoidMembershipFunction createTrapezoidMembershipFunction()
	{
		return new TrapezoidMembershipFunction();
	}
	
	public TrapezoidMembershipFunction createTrapezoidMembershipFunction(Parameter p)
	{
		return new TrapezoidMembershipFunction(p);
	}
	
	public TrapezoidMembershipFunction createTrapezoidMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new TrapezoidMembershipFunction(p,domainLeft,domainRight);
	}
	
	public TriangularMembershipFunction createTriangularMembershipFunction()
	{
		return new TriangularMembershipFunction();
	}
	
	public TriangularMembershipFunction createTriangularMembershipFunction(Parameter p)
	{
		return new TriangularMembershipFunction(p);
	}
	
	public TriangularMembershipFunction createTriangularMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new TriangularMembershipFunction(p,domainLeft,domainRight);
	}
	
	public ZShapeMembershipFunction createZShapeMembershipFunction()
	{
		return new ZShapeMembershipFunction();
	}
	
	public ZShapeMembershipFunction createZShapeMembershipFunction(Parameter p)
	{
		return new ZShapeMembershipFunction(p);
	}
	
	public ZShapeMembershipFunction createZShapeMembershipFunction(Parameter p, float domainLeft, float domainRight)
	{
		return new ZShapeMembershipFunction(p,domainLeft,domainRight);
	}
	
}
