package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardCombinationType;

public class JFMLEnumeration_StandardCombinationType {
	
	StandardCombinationType WA;
	
	public JFMLEnumeration_StandardCombinationType(){
		WA = StandardCombinationType.WA;
	}
	
	public StandardCombinationType fromValue(String v){
		return StandardCombinationType.fromValue(v);
	}
	
}
