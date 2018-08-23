package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardTnormType;

/**
 * This class contains enumerated constants of JFML Enum Type 'StandardTnormType'.
 * This middle class is needed to use Java enumerated constants through Py4J.
 *
 */
public class JFMLEnumeration_StandardTnormType {
	
	StandardTnormType MIN;
	StandardTnormType PROD;
	StandardTnormType BSUM;
	StandardTnormType DRS;
	StandardTnormType EPROD;
	StandardTnormType HPROD;
	StandardTnormType NILMIN;
	
	public JFMLEnumeration_StandardTnormType(){
		MIN = StandardTnormType.MIN;
		PROD = StandardTnormType.PROD;
		BSUM = StandardTnormType.BSUM;
		DRS = StandardTnormType.DRS;
		EPROD = StandardTnormType.EPROD;
		HPROD = StandardTnormType.HPROD;
		NILMIN = StandardTnormType.NILMIN;		
	}
	
	public StandardTnormType fromValue(String v){
		return StandardTnormType.fromValue(v);
	}

}
