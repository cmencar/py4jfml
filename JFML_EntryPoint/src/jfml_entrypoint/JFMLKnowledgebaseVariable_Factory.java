package jfml_entrypoint;

import java.util.List;

import jfml.knowledgebase.variable.AggregatedFuzzyVariableType;
import jfml.knowledgebase.variable.AnYaDataCloudType;
import jfml.knowledgebase.variable.FuzzyVariableType;
import jfml.knowledgebase.variable.TskVariableType;
import jfml.knowledgebase.variable.TsukamotoVariableType;
import jfml.knowledgebase.variable.WZ;

public class JFMLKnowledgebaseVariable_Factory 
{
	public AggregatedFuzzyVariableType createAggregatedFuzzyVariableType()
	{
		return new AggregatedFuzzyVariableType();
	}
	
	public AggregatedFuzzyVariableType createAggregatedFuzzyVariableType(String name)
	{
		return new AggregatedFuzzyVariableType(name);
	}

	public AggregatedFuzzyVariableType createAggregatedFuzzyVariableType(String name, String type)
	{
		return new AggregatedFuzzyVariableType(name,type);
	}
	
	public AnYaDataCloudType createAnYaDataCloudType()
	{
		return new AnYaDataCloudType();
	}
	
	public AnYaDataCloudType createAnYaDataCloudType(String name)
	{
		return new AnYaDataCloudType(name);
	}
	
	public AnYaDataCloudType createAnYaDataCloudType(String name, List<java.lang.Double> terms)
	{
		return new AnYaDataCloudType(name,terms);
	}
	
	public FuzzyVariableType createFuzzyVariableType() 
	{
		return new FuzzyVariableType();
	}
	
	public FuzzyVariableType createFuzzyVariableType(String name, float domainLeft, float domainRight) 
	{
		return new FuzzyVariableType(name,domainLeft,domainRight);
	}
	
	public TskVariableType createTskVariableType() 
	{
		return new TskVariableType();
	}
	
	public TskVariableType createTskVariableType(String name)
	{
		return new TskVariableType(name);
	}
	
	public TsukamotoVariableType createTsukamotoVariableType()
	{
		return new TsukamotoVariableType();
	}
	
	public TsukamotoVariableType createTsukamotoVariableType(String name, float domainLeft, float domainRight)
	{
		return new TsukamotoVariableType(name,domainLeft,domainRight);
	}
	
	public WZ createWZ(float w, float z)
	{
		return new WZ(w,z);
	}
	
}
