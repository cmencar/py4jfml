package jfml_entrypoint;

import py4j.GatewayServer;

public class JFML_EntryPoint {
	
	public JFML_Factory getJFML_Factory()
	{
		return new JFML_Factory();
	}
	
	public JFMLAggregated_Factory getJFMLAggregated_Factory()
	{
		return new JFMLAggregated_Factory();
	}
	
	public JFMLCompatibility_Factory getJFMLCompatibility_Factory()
	{
		return new JFMLCompatibility_Factory();
	}
	
	public JFMLDefuzzifier_Factory getJFMLDefuzzifier_Factory()
	{
		return new JFMLDefuzzifier_Factory();
	}

	public JFMLJaxb_Factory getJFMLjaxb_Factory()
	{
		return new JFMLJaxb_Factory(); 
	}
	
	public JFMLKnowledgebase_Factory getJFMLKnowledgebase_Factory()
	{
		return new JFMLKnowledgebase_Factory();
	}
	
	public JFMLKnowledgebaseVariable_Factory getJFMLKnowledgebaseVariable_Factory()
	{
		return new JFMLKnowledgebaseVariable_Factory();
	}
	
	public JFMLMembershipfunction_Factory getJFMLMembershipfunction_Factory()
	{
		return new JFMLMembershipfunction_Factory();
	}
	
	public JFMLOperator_Factory getJFMLOperator_Factory()
	{
		return new JFMLOperator_Factory();
	}
	
	public JFMLParameter_Factory getJFMLParameter_Factory()
	{
		return new JFMLParameter_Factory();
	}
	
	public JFMLRule_Factory getJFMLRule_Factory()
	{
		return new JFMLRule_Factory();
	}
	
	public JFMLRulebase_Factory getJFMLRulebase_Factory()
	{
		return new JFMLRulebase_Factory();
	}
	
	public JFMLTerm_Factory getJFMLTerm_Factory()
	{
		return new JFMLTerm_Factory();
	}
	
	public JFMLEnumeration_Factory getJFMLEnemeration_Factory()
	{
		return new JFMLEnumeration_Factory();
	}
	
	//Start server
	public static void main(String[] args) 
	{
		JFML_EntryPoint jf = new JFML_EntryPoint();
		GatewayServer gatewayServer = new GatewayServer(jf);
		gatewayServer.start();
		System.out.println("Gateway PY4JFML Server Started!");
	}

}
