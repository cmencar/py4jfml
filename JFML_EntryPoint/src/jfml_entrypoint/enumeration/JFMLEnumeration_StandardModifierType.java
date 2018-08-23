package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardModifierType;

/**
 * This class contains enumerated constants of JFML Enum Type 'StandardModifierType'.
 * This middle class is needed to use Java enumerated constants through Py4J.
 *
 */
public class JFMLEnumeration_StandardModifierType {
	
	StandardModifierType ABOVE;
	StandardModifierType ANY;
	StandardModifierType BELOW;
	StandardModifierType EXTREMELY;
	StandardModifierType INTENSIFY;
	StandardModifierType MORE_OR_LESS;
	StandardModifierType NORM;
	StandardModifierType NOT;
	StandardModifierType PLUS;
	StandardModifierType SELDOM;
	StandardModifierType SLIGHTLY;
	StandardModifierType SOMEWHAT;
	StandardModifierType VERY;
	
	public JFMLEnumeration_StandardModifierType(){
		ABOVE = StandardModifierType.ABOVE;
		ANY = StandardModifierType.ANY;
		BELOW = StandardModifierType.BELOW;
		EXTREMELY = StandardModifierType.EXTREMELY;
		INTENSIFY = StandardModifierType.INTENSIFY;
		MORE_OR_LESS = StandardModifierType.MORE_OR_LESS;
		NORM = StandardModifierType.NORM;
		NOT = StandardModifierType.NOT;
		PLUS = StandardModifierType.PLUS;
		SELDOM = StandardModifierType.SELDOM;
		SLIGHTLY = StandardModifierType.SLIGHTLY;
		SOMEWHAT = StandardModifierType.SOMEWHAT;
		VERY = StandardModifierType.VERY;
	}
	
	public StandardModifierType fromValue(String v){
		return StandardModifierType.fromValue(v);
	}

}
