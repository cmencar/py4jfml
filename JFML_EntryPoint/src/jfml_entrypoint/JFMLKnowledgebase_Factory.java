package jfml_entrypoint;

import jfml.knowledgebase.KnowledgeBaseType;

/**
 * This class allows to return class instances of the JFML package 'knowledgebase'.
 *  
 */
public class JFMLKnowledgebase_Factory {
	
	public KnowledgeBaseType createKnowledgeBaseType()
	{
		return new KnowledgeBaseType();
	}
	
}
