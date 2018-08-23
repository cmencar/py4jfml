package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardCombinationType;

/**
 * This class contains enumerated constants of JFML Enum Type 'StandardCombinationType'.
 * This middle class is needed to use Java enumerated constants through Py4J.
 *
 */
public class JFMLEnumeration_StandardCombinationType {
	
	StandardCombinationType WA;
	
	public JFMLEnumeration_StandardCombinationType(){
		WA = StandardCombinationType.WA;
	}
	
	public StandardCombinationType fromValue(String v){
		return StandardCombinationType.fromValue(v);
	}
	
}
