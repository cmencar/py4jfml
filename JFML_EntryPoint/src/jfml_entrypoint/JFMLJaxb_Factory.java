package jfml_entrypoint;

import java.util.List;

import jfml.jaxb.FuzzySystemType;
import jfml.jaxb.ObjectFactory;
import jfml.knowledgebase.KnowledgeBaseType;

/**
 * This class allows to return class instances of the JFML package 'jaxb'.
 *  
 */
public class JFMLJaxb_Factory {
	
	public FuzzySystemType createFuzzySystemType()
	{
		return new FuzzySystemType();
	}
	
	public FuzzySystemType createFuzzySystemType(String name)
	{
		return new FuzzySystemType(name);
	}
	
	public FuzzySystemType createFuzzySystemType(String name, KnowledgeBaseType knowledgeBase, List<Object> ruleBase, String networkAddress) 
	{
		return new FuzzySystemType(name,knowledgeBase,ruleBase,networkAddress);
	}
	
	public ObjectFactory createObjectFactory()
	{
		return new ObjectFactory();
	}

}
