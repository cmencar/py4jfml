package jfml_entrypoint;
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
