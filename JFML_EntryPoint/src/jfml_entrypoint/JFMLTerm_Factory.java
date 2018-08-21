package jfml_entrypoint;

import java.util.ArrayList;
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
	
	public FuzzyTermType createFuzzyTermType(String name, int type, ArrayList<Object> param)
	{
		if(!param.isEmpty() && param.get(0) instanceof Double){
			float[] arFloat = new float[param.size()];
			for (int i = 0; i < param.size(); i++) {
				Double paramDouble = (Double) param.get(i);
				arFloat[i] = paramDouble.floatValue();
			}
			return new FuzzyTermType(name,type,arFloat);
		}else if(!param.isEmpty() && param.get(0) instanceof PointType){
			ArrayList<PointType> points = new ArrayList<>();
			for (int i = 0; i < param.size(); i++) {
				PointType point = (PointType) param.get(i);
				points.add(point);
			}
			return new FuzzyTermType(name,type,points);
		}
		return null;
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
	
	public TskTermType createTskTermType(String name, int order, ArrayList<Double> coeff)
	{
		float[] arFloat = new float[coeff.size()];
		for (int i = 0; i < coeff.size(); i++) {
			arFloat[i] = coeff.get(i).floatValue();
		}
		return new TskTermType(name,order,arFloat);
	}
	
	public TsukamotoTermType createTsukamotoTermType()
	{
		return new TsukamotoTermType();
	}
	
	public TsukamotoTermType createTsukamotoTermType(String name, int type, ArrayList<Object> param)
	{
		if(!param.isEmpty() && param.get(0) instanceof Double){
			float[] arFloat = new float[param.size()];
			for (int i = 0; i < param.size(); i++) {
				Double paramDouble = (Double) param.get(i);
				arFloat[i] = paramDouble.floatValue();
			}
			return new TsukamotoTermType(name,type,arFloat);
		}else if(!param.isEmpty() && param.get(0) instanceof PointType){
			ArrayList<PointType> points = new ArrayList<>();
			for (int i = 0; i < param.size(); i++) {
				PointType point = (PointType) param.get(i);
				points.add(point);
			}
			return new TsukamotoTermType(name,type,points);
		}
		return null;
	}
	
	public TsukamotoTermType createTsukamotoTermType(String name, PointSetMonotonicShapeType psm)
	{
		return new TsukamotoTermType(name,psm);
	}

}
