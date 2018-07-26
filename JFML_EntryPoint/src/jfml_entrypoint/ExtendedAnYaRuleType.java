package jfml_entrypoint;
import jfml.rule.AnYaAntecedentType;
import jfml.rule.AnYaRuleType;
import jfml.rule.ConsequentType;
import jfml.rule.TskConsequentType;;

public class ExtendedAnYaRuleType extends AnYaRuleType{
	
	public ExtendedAnYaRuleType(){
		super();
	}
	
	public ExtendedAnYaRuleType(String name){
		super(name);
	}
	
	public ExtendedAnYaRuleType(String name, AnYaAntecedentType ant, ConsequentType con){
		super(name,ant,con);
	}
	
	public ExtendedAnYaRuleType(String name, AnYaAntecedentType ant, TskConsequentType con){
		super(name,ant,con);
	}
	
	public ExtendedAnYaRuleType(String name, java.lang.Float weight){
		super(name,weight);
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
