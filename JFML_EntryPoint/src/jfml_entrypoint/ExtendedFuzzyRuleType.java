package jfml_entrypoint;
import jfml.rule.AntecedentType;
import jfml.rule.ConsequentType;
import jfml.rule.FuzzyRuleType;

public class ExtendedFuzzyRuleType extends FuzzyRuleType{
	
	public ExtendedFuzzyRuleType(){
		super();
	}
	
	public ExtendedFuzzyRuleType(String name){
		super(name);
	}
	
	public ExtendedFuzzyRuleType(String name, AntecedentType ant, ConsequentType con){
		super(name,ant,con);
	}
	
	public ExtendedFuzzyRuleType(String name, Float weight){
		super(name,weight);
	}
	
	public ExtendedFuzzyRuleType(String name, String connector, String connectorMethod, Float weight){
		super(name,connector,connectorMethod,weight);
	}
	
	public ExtendedFuzzyRuleType(String name, String connector, String andMethod, String orMethod, Float weight){
		super(name,connector,andMethod,orMethod,weight);
	}
	
	public float andFunction(float[] degrees){	
		return this.and(degrees);
	}
	
	public float andFunction(String andMethod, float[] degrees){
		return this.and(andMethod, degrees);
	}
	
	public float orFunction(float[] degrees){	
		return this.or(degrees);
	}
	
	public float orFunction(String andMethod, float[] degrees){
		return this.or(andMethod, degrees);
	}
}
