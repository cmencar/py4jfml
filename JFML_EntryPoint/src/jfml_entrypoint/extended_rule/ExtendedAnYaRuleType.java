package jfml_entrypoint.extended_rule;
import java.util.ArrayList;
import jfml.rule.AnYaAntecedentType;
import jfml.rule.AnYaRuleType;
import jfml.rule.ConsequentType;
import jfml.rule.TskConsequentType;;

/**
 * This class extends JFML class 'AnYaRuleType' to allows to use 'and' and 'or' JFML methods in Python syntax.
 * These methods have been called in new methods 'andFunction' and 'orFunction'.
 *
 */
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
		//Conversion of a Double list received from Python in a float Array
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		//Calling of AnYaRuleType 'and' method
		return this.and(degrees);
	}
	
	public float andFunction(String andMethod, ArrayList<Double> degreesList){
		//Conversion of a Double list received from Python in a float Array
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		//Calling of AnYaRuleType 'and' method
		return this.and(andMethod, degrees);
	}
	
	public float orFunction(ArrayList<Double> degreesList){
		//Conversion of a Double list received from Python in a float Array
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		//Calling of AnYaRuleType 'or' method
		return this.or(degrees);
	}
	
	public float orFunction(String andMethod, ArrayList<Double> degreesList){
		//Conversion of a Double list received from Python in a float Array
		float[] degrees = new float[degreesList.size()];
		for (int i = 0; i < degreesList.size(); i++) {
			degrees[i] = degreesList.get(i).floatValue();
		}
		//Calling of AnYaRuleType 'or' method
		return this.or(andMethod, degrees);
	}
}
