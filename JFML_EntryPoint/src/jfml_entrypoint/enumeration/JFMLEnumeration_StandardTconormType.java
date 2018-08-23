package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardTconormType;

/**
 * This class contains enumerated constants of JFML Enum Type 'StandardTconormType'.
 * This middle class is needed to use Java enumerated constants through Py4J.
 *
 */
public class JFMLEnumeration_StandardTconormType {
	
	StandardTconormType MAX;
	StandardTconormType PROBOR;
	StandardTconormType BSUM;
	StandardTconormType DRS;
	StandardTconormType ESUM;
	StandardTconormType HSUM;
	StandardTconormType NILMAX;
	
	public JFMLEnumeration_StandardTconormType(){
		MAX = StandardTconormType.MAX;
		PROBOR = StandardTconormType.PROBOR;
		BSUM = StandardTconormType.BSUM;
		DRS = StandardTconormType.DRS;
		ESUM = StandardTconormType.ESUM;
		HSUM = StandardTconormType.HSUM;
		NILMAX = StandardTconormType.NILMAX;
	}
	
	public StandardTconormType fromValue(String v){
		return StandardTconormType.fromValue(v);
	}

}
