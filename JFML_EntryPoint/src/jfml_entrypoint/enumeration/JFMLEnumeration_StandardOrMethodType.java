package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardOrMethodType;

/**
 * This class contains enumerated constants of JFML Enum Type 'StandardOrMethodType'.
 * This middle class is needed to use Java enumerated constants through Py4J.
 *
 */
public class JFMLEnumeration_StandardOrMethodType {

	StandardOrMethodType MAX;
	StandardOrMethodType PROBOR;
	StandardOrMethodType BSUM;
	StandardOrMethodType DRS;
	StandardOrMethodType ESUM;
	StandardOrMethodType HSUM;
	StandardOrMethodType NILMAX;
	
	public JFMLEnumeration_StandardOrMethodType(){
		MAX = StandardOrMethodType.MAX;
		PROBOR = StandardOrMethodType.PROBOR;
		BSUM = StandardOrMethodType.BSUM;
		DRS = StandardOrMethodType.DRS;
		ESUM = StandardOrMethodType.ESUM;
		HSUM = StandardOrMethodType.HSUM;
		NILMAX = StandardOrMethodType.NILMAX;
	}
	
	public StandardOrMethodType fromValue(String v){
		return StandardOrMethodType.fromValue(v);
	}
	
}
