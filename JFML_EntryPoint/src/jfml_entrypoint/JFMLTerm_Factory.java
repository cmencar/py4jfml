package jfml_entrypoint;

import java.util.List;

import jfml.aggregated.AggregatedType;
import jfml.aggregated.AndAggregatedType;
import jfml.aggregated.OrAggregatedType;
import jfml.membershipfunction.CircularDefinitionType;
import jfml.membershipfunction.CustomShapeType;
import jfml.membershipfunction.PointSetMonotonicShapeType;
import jfml.membershipfunction.PointSetShapeType;
import jfml.membershipfunction.PointType;
import jfml.term.AggregatedFuzzyTermType;
import jfml.term.CircularTermType;
import jfml.term.FuzzyTerm;
import jfml.term.FuzzyTermType;
import jfml.term.TskTermType;
import jfml.term.TsukamotoTermType;

public class JFMLTerm_Factory {
	
	public AggregatedFuzzyTermType createAggregatedFuzzyTermType()
	{
		return new AggregatedFuzzyTermType();
	}
	
	public AggregatedFuzzyTermType createAggregatedFuzzyTermType(String name)
	{
		return new AggregatedFuzzyTermType(name);
	}
	
	public AggregatedFuzzyTermType createAggregatedFuzzyTermType(String name, AggregatedType agg)
	{
		return new AggregatedFuzzyTermType(name,agg);
	}
	
	public AggregatedFuzzyTermType createAggregatedFuzzyTermType(String name, AndAggregatedType and, OrAggregatedType or)
	{
		return new AggregatedFuzzyTermType(name,and,or);
	}
	
	public CircularTermType createCircularTermType()
	{
		return new CircularTermType();
	}
	
	public CircularTermType createCircularTermType(String name)
	{
		return new CircularTermType(name);
	}
	
	public FuzzyTermType createFuzzyTermType()
	{
		return new FuzzyTermType();
	}

	public FuzzyTermType createFuzzyTermType(String name, CircularDefinitionType c)
	{
		return new FuzzyTermType(name,c);
	}
	
	public FuzzyTermType createFuzzyTermType(String name, CustomShapeType c)
	{
		return new FuzzyTermType(name,c);
	}
	
	public FuzzyTermType createFuzzyTermType(String name, int type, float[] param)
	{
		return new FuzzyTermType(name,type,param);
	}
	
	public FuzzyTermType createFuzzyTermType(String name, int type, List<PointType> points)
	{
		return new FuzzyTermType(name,type,points);
	}

	public FuzzyTermType createFuzzyTermType(String name, PointSetShapeType p)
	{
		return new FuzzyTermType(name,p);
	}
	
	public FuzzyTermType createFuzzyTermType(String name, String complement, CircularDefinitionType circular)
	{
		return new FuzzyTermType(name,complement,circular);
	}
	
	public FuzzyTermType createFuzzyTermType(String name, String complement, PointSetShapeType point)
	{
		return new FuzzyTermType(name,complement,point);
	}
	
	public TskTermType createTskTermType()
	{
		return new TskTermType();
	}
	
	public TskTermType createTskTermType(String name, int order, float[] coeff)
	{
		return new TskTermType(name,order,coeff);
	}
	
	public TsukamotoTermType createTsukamotoTermType()
	{
		return new TsukamotoTermType();
	}
	
	public TsukamotoTermType createTsukamotoTermType(String name, int type, float[] param)
	{
		return new TsukamotoTermType(name,type,param);
	}
	
	public TsukamotoTermType createTsukamotoTermType(String name, int type, List<PointType> param)
	{
		return new TsukamotoTermType(name,type,param);
	}
	
	public TsukamotoTermType createTsukamotoTermType(String name, PointSetMonotonicShapeType psm)
	{
		return new TsukamotoTermType(name,psm);
	}

}
