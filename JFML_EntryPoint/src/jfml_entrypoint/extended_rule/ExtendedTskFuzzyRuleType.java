package jfml_entrypoint.extended_rule;
import java.util.ArrayList;

import jfml.rule.AntecedentType;
import jfml.rule.TskConsequentType;
import jfml.rule.TskFuzzyRuleType;

/**
 * This class extends JFML class 'TskFuzzyRuleType' to allows to use 'and' and 'or' JFML methods in Python syntax.
 * These methods have been called in new methods 'andFunction' and 'orFunction'.
 *
 */
public class ExtendedTskFuzzyRuleType extends TskFuzzyRuleType{
	
	public ExtendedTskFuzzyRuleType(){
		super();
	}
	
	public ExtendedTskFuzzyRuleType(String name){
		super(name);
	}
	
	public ExtendedTskFuzzyRuleType(String name, AntecedentType ant, TskConsequentType con){
		super(name,ant,con);
	}
	
	public ExtendedTskFuzzyRuleType(String name, Float weight){
		super(name,weight);
	}
	
	public ExtendedTskFuzzyRuleType(String name, String connector, String connectorMethod, Float weight){
		super(name,connector,connectorMethod,weight);
	}
	
	public ExtendedTskFuzzyRuleType(String name, String connector, String andMethod, String orMethod, Float weight){
		super(name,connector,andMethod,orMethod,weight);
	}
	
	public float andFunction(ArrayList<Double> degreesList){
		//Conversion of a Double list received from Python in a float Array
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		//Calling of TskFuzzyRuleType 'and' method
		return this.and(degrees);
	}
	
	public float andFunction(String andMethod, ArrayList<Double> degreesList){
		//Conversion of a Double list received from Python in a float Array
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		//Calling of TskFuzzyRuleType 'and' method
		return this.and(andMethod, degrees);
	}
	
	public float orFunction(ArrayList<Double> degreesList){
		//Conversion of a Double list received from Python in a float Array
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		//Calling of TskFuzzyRuleType 'or' method
		return this.or(degrees);
	}
	
	public float orFunction(String andMethod, ArrayList<Double> degreesList){
		//Conversion of a Double list received from Python in a float Array
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		//Calling of TskFuzzyRuleType 'or' method
		return this.or(andMethod, degrees);
	}
}
