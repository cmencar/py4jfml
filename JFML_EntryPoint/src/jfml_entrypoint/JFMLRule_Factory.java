package jfml_entrypoint;

import java.util.List;

import jfml.knowledgebase.variable.AnYaDataCloudType;
import jfml.rule.AnYaAntecedentType;
import jfml.rule.AnYaRuleType;
import jfml.rule.AntecedentType;
import jfml.rule.ClauseType;
import jfml.rule.ConsequentClausesType;
import jfml.rule.ConsequentType;
import jfml.rule.FuzzyRuleType;
import jfml.rule.TskClauseType;
import jfml.rule.TskConsequentClausesType;
import jfml.rule.TskConsequentType;
import jfml.rule.TskFuzzyRuleType;

public class JFMLRule_Factory {

	public AntecedentType createAntecedentType()
	{
		return new AntecedentType();
	}
	
	public AntecedentType createAntecedentType(List<ClauseType> clauses)
	{
		return new AntecedentType(clauses);
	}
	
	public AnYaAntecedentType createAnYaAntecedentType()
	{
		return new AnYaAntecedentType();
	}
	
	public AnYaAntecedentType createAnYaAntecedentType(AnYaDataCloudType dataCloud)
	{
		return new AnYaAntecedentType(dataCloud);
	}
	
	public AnYaRuleType createAnYaRuleType()
	{
		return new AnYaRuleType();
	}
	
	public AnYaRuleType createAnYaRuleType(String name)
	{
		return new AnYaRuleType(name);
	}
	
	public AnYaRuleType createAnYaRuleType(String name, AnYaAntecedentType ant, ConsequentType con)
	{
		return new AnYaRuleType(name,ant,con);
	}
	
	public AnYaRuleType createAnYaRuleType(String name, AnYaAntecedentType ant, TskConsequentType con)
	{
		return new AnYaRuleType(name,ant,con);
	}
	
	public AnYaRuleType createAnYaRuleType(String name, java.lang.Float weight)
	{
		return new AnYaRuleType(name,weight);
	}
	
	public ClauseType createClauseType()
	{
		return new ClauseType();
	}
	
	public ClauseType createClauseType(Object variable, Object term)
	{
		return new ClauseType(variable,term);
	}
	
	public ClauseType createClauseType(Object variable, Object term, String modifier)
	{
		return new ClauseType(variable,term,modifier);
	}
	
	public ConsequentClausesType createConsequentClausesType()
	{
		return new ConsequentClausesType();
	}
	
	public ConsequentClausesType createConsequentClausesType(List<ClauseType> clauses)
	{
		return new ConsequentClausesType(clauses);
	}
	
	public ConsequentType createConsequentType()
	{
		return new ConsequentType();
	}
	
	public ConsequentType createConsequentType(ConsequentClausesType then, ConsequentClausesType _else)
	{
		return new ConsequentType(then,_else);
	}
	
	public FuzzyRuleType createFuzzyRuleType()
	{
		return new FuzzyRuleType();
	}
	
	public FuzzyRuleType createFuzzyRuleType(String name)
	{
		return new FuzzyRuleType(name);
	}
	
	public FuzzyRuleType createFuzzyRuleType(String name, AntecedentType ant, ConsequentType con)
	{
		return new FuzzyRuleType(name,ant,con);
	}
	
	public FuzzyRuleType createFuzzyRuleType(String name, Float weight)
	{
		return new FuzzyRuleType(name,weight);
	}
	
	public FuzzyRuleType createFuzzyRuleType(String name, String connector, String connectorMethod, Float weight)
	{
		return new FuzzyRuleType(name,connector,connectorMethod,weight);
	}
	
	public FuzzyRuleType createFuzzyRuleType(String name, String connector, String andMethod, String orMethod, Float weight)
	{
		return new FuzzyRuleType(name,connector,andMethod,orMethod,weight);
	}
	
	public TskClauseType createTskClauseType()
	{
		return new TskClauseType();
	}
	
	public TskClauseType createTskClauseType(Object variable, Object term)
	{
		return new TskClauseType(variable,term);
	}
	
	public TskConsequentClausesType createTskConsequentClausesType()
	{
		return new TskConsequentClausesType();
	}
	
	public TskConsequentType createTskConsequentType()
	{
		return new TskConsequentType();
	}
	
	public TskConsequentType createTskConsequentType(TskConsequentClausesType then, TskConsequentClausesType _else)
	{
		return new TskConsequentType(then,_else);
	}
	
	public TskFuzzyRuleType createTskFuzzyRuleType()
	{
		return new TskFuzzyRuleType();
	}
	
	public TskFuzzyRuleType createTskFuzzyRuleType(String name)
	{
		return new TskFuzzyRuleType(name);
	}
	
	public TskFuzzyRuleType createTskFuzzyRuleType(String name, AntecedentType ant, TskConsequentType con)
	{
		return new TskFuzzyRuleType(name,ant,con);
	}
	
	public TskFuzzyRuleType createTskFuzzyRuleType(String name, Float weight)
	{
		return new TskFuzzyRuleType(name,weight);
	}
	
	public TskFuzzyRuleType createTskFuzzyRuleType(String name, String connector, String connectorMethod, Float weight)
	{
		return new TskFuzzyRuleType(name,connector,connectorMethod,weight);
	}
	
	public TskFuzzyRuleType createTskFuzzyRuleType(String name, String connector, String andMethod, String orMethod, Float weight)
	{
		return new TskFuzzyRuleType(name,connector,andMethod,orMethod,weight);
	}
	
}
