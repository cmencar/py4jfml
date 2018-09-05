package jfml_entrypoint;

import py4j.GatewayServer;

/**
 * This class allows to start the PY4JFML gateway server. 
 * It uses Py4J to enable Python programs running in Python interpreter to dynamically access Java objects in a Java virtual machine.
 * Every getter method returns an instance of a specific factory class that represents a JFML package.
 * This class implements the Singleton Pattern. 
 * 
 */
public class JFML_EntryPoint {
	
	private static JFML_Factory jfml_Factory;
	private static JFMLAggregated_Factory jfmlAggregated_Factory;
	private static JFMLCompatibility_Factory jfmlCompatibility_Factory;
	private static JFMLDefuzzifier_Factory jfmlDefuzzifier_Factory;
	private static JFMLJaxb_Factory jfmlJaxb_Factory;
	private static JFMLKnowledgebase_Factory jfmlKnowledgebase_Factory;
	private static JFMLKnowledgebaseVariable_Factory jfmlKnowledgebaseVariable_Factory;
	private static JFMLMembershipfunction_Factory jfmlMembershipfunction_Factory;
	private static JFMLOperator_Factory jfmlOperator_Factory;
	private static JFMLParameter_Factory jfmlParameter_Factory;
	private static JFMLRule_Factory jfmlRule_Factory;
	private static JFMLRulebase_Factory jfmlRulebase_Factory;
	private static JFMLTerm_Factory jfmlTerm_Factory;
	private static JFMLEnumeration_Factory jfmlEnumeration_Factory;
	
	public JFML_Factory getJFML_Factory()
	{
		if(jfml_Factory==null){
			jfml_Factory = new JFML_Factory();
		}
		return jfml_Factory;
	}
	
	public JFMLAggregated_Factory getJFMLAggregated_Factory()
	{
		if(jfmlAggregated_Factory==null){
			jfmlAggregated_Factory = new JFMLAggregated_Factory();
		}
		return jfmlAggregated_Factory;
	}
	
	public JFMLCompatibility_Factory getJFMLCompatibility_Factory()
	{
		if(jfmlCompatibility_Factory==null){
			jfmlCompatibility_Factory = new JFMLCompatibility_Factory();
		}
		return jfmlCompatibility_Factory;
	}
	
	public JFMLDefuzzifier_Factory getJFMLDefuzzifier_Factory()
	{
		if(jfmlDefuzzifier_Factory==null){
			jfmlDefuzzifier_Factory = new JFMLDefuzzifier_Factory();
		}
		return jfmlDefuzzifier_Factory;
	}

	public JFMLJaxb_Factory getJFMLjaxb_Factory()
	{
		if(jfmlJaxb_Factory==null){
			jfmlJaxb_Factory = new JFMLJaxb_Factory();
		}
		return jfmlJaxb_Factory;
	}
	
	public JFMLKnowledgebase_Factory getJFMLKnowledgebase_Factory()
	{
		if(jfmlKnowledgebase_Factory==null){
			jfmlKnowledgebase_Factory = new JFMLKnowledgebase_Factory();
		}
		return jfmlKnowledgebase_Factory;
	}
	
	public JFMLKnowledgebaseVariable_Factory getJFMLKnowledgebaseVariable_Factory()
	{
		if(jfmlKnowledgebaseVariable_Factory==null){
			jfmlKnowledgebaseVariable_Factory = new JFMLKnowledgebaseVariable_Factory();
		}
		return jfmlKnowledgebaseVariable_Factory;
	}
	
	public JFMLMembershipfunction_Factory getJFMLMembershipfunction_Factory()
	{
		if(jfmlMembershipfunction_Factory==null){
			jfmlMembershipfunction_Factory = new JFMLMembershipfunction_Factory();
		}
		return jfmlMembershipfunction_Factory;
	}
	
	public JFMLOperator_Factory getJFMLOperator_Factory()
	{
		if(jfmlOperator_Factory==null){
			jfmlOperator_Factory = new JFMLOperator_Factory();
		}
		return jfmlOperator_Factory;
	}
	
	public JFMLParameter_Factory getJFMLParameter_Factory()
	{
		if(jfmlParameter_Factory==null){
			jfmlParameter_Factory = new JFMLParameter_Factory();
		}
		return jfmlParameter_Factory;
	}
	
	public JFMLRule_Factory getJFMLRule_Factory()
	{
		if(jfmlRule_Factory==null){
			jfmlRule_Factory = new JFMLRule_Factory();
		}
		return jfmlRule_Factory;
	}
	
	public JFMLRulebase_Factory getJFMLRulebase_Factory()
	{
		if(jfmlRulebase_Factory==null){
			jfmlRulebase_Factory = new JFMLRulebase_Factory();
		}
		return jfmlRulebase_Factory;
	}
	
	public JFMLTerm_Factory getJFMLTerm_Factory()
	{
		if(jfmlTerm_Factory==null){
			jfmlTerm_Factory = new JFMLTerm_Factory();
		}
		return jfmlTerm_Factory;
	}
	
	public JFMLEnumeration_Factory getJFMLEnemeration_Factory()
	{
		if(jfmlEnumeration_Factory==null){
			jfmlEnumeration_Factory = new JFMLEnumeration_Factory();
		}
		return jfmlEnumeration_Factory;
	}
	
	//Start server
	public static void main(String[] args) 
	{
		try{
			JFML_EntryPoint jf = new JFML_EntryPoint();
			GatewayServer gatewayServer = new GatewayServer(jf);
			gatewayServer.start();
			System.out.println("Gateway PY4JFML Server Started!");			
		}catch (py4j.Py4JNetworkException e) {
			
		}		
	}

}
