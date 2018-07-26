package jfml_entrypoint;
import java.util.ArrayList;

import jfml.rule.AntecedentType;
import jfml.rule.TskConsequentType;
import jfml.rule.TskFuzzyRuleType;

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
	
	public float andFunction(ArrayList<Float> degreesList){	
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		return this.and(degrees);
	}
	
	public float andFunction(String andMethod, ArrayList<Float> degreesList){
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		return this.and(andMethod, degrees);
	}
	
	public float orFunction(ArrayList<Float> degreesList){	
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		return this.or(degrees);
	}
	
	public float orFunction(String andMethod, ArrayList<Float> degreesList){
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		return this.or(andMethod, degrees);
	}
}
