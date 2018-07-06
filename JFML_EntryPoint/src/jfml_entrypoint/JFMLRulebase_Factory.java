package jfml_entrypoint;

import jfml.rulebase.AnYaRuleBaseType;
import jfml.rulebase.MamdaniRuleBaseType;
import jfml.rulebase.RuleBaseType;
import jfml.rulebase.TskRuleBaseType;
import jfml.rulebase.TsukamotoRuleBaseType;

public class JFMLRulebase_Factory {

	public AnYaRuleBaseType createAnYaRuleBaseType()
	{
		return new AnYaRuleBaseType();
	}
	
	public AnYaRuleBaseType createAnYaRuleBaseType(String name)
	{
		return new AnYaRuleBaseType(name);
	}
	
	public MamdaniRuleBaseType createMamdaniRuleBaseType()
	{
		return new MamdaniRuleBaseType();
	}
	
	public MamdaniRuleBaseType createMamdaniRuleBaseType(String name)
	{
		return new MamdaniRuleBaseType(name);
	}
	
	public MamdaniRuleBaseType createMamdaniRuleBaseType(String name, String activation, String and, String or, int type)
	{
		return new MamdaniRuleBaseType(name,activation,and,or,type);
	}
	
	public RuleBaseType createRuleBaseType()
	{
		return new RuleBaseType();
	}
	
	public RuleBaseType createRuleBaseType(String name, int type)
	{
		return new RuleBaseType(name,type);
	}
	
	public RuleBaseType createRuleBaseType(String name, String activation, String and, String or, int type)
	{
		return new RuleBaseType(name,activation,and,or,type);
	}
	
	public TskRuleBaseType createTskRuleBaseType()
	{
		return new TskRuleBaseType();
	}
	
	public TskRuleBaseType createTskRuleBaseType(String name, int type)
	{
		return new TskRuleBaseType(name,type);
	}
	
	public TskRuleBaseType createTskRuleBaseType(String name, String activation, String and, String or, int type)
	{
		return new TskRuleBaseType(name,activation,and,or,type);
	}
	
	public TsukamotoRuleBaseType createTsukamotoRuleBaseType()
	{
		return new TsukamotoRuleBaseType();
	}
	
	public TsukamotoRuleBaseType createTsukamotoRuleBaseType(String name)
	{
		return new TsukamotoRuleBaseType(name);
	}
	
	public TsukamotoRuleBaseType createTsukamotoRuleBaseType(String name, String activation, String and, String or, int type)
	{
		return new TsukamotoRuleBaseType(name,activation,and,or,type);
	}
}
