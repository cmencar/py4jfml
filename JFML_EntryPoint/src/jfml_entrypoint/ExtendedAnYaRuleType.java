package jfml_entrypoint;
import java.util.ArrayList;
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
	
	public float andFunction(ArrayList<Double> degreesList){
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		return this.and(degrees);
	}
	
	public float andFunction(String andMethod, ArrayList<Double> degreesList){
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		return this.and(andMethod, degrees);
	}
	
	public float orFunction(ArrayList<Double> degreesList){
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		return this.or(degrees);
	}
	
	public float orFunction(String andMethod, ArrayList<Double> degreesList){
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		return this.or(andMethod, degrees);
	}
}
