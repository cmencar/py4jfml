package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardAndMethodType;

/**
 * This class contains enumerated constants of JFML Enum Type 'StandardAndMethodType'.
 * This middle class is needed to use java enumerated constants through Py4J.
 *
 */
public class JFMLEnumeration_StandardAndMethodType {

	StandardAndMethodType MIN;
	StandardAndMethodType PROD;
	StandardAndMethodType BDIF;
	StandardAndMethodType DRP;
	StandardAndMethodType EPROD;
	StandardAndMethodType HPROD;
	StandardAndMethodType NILMIN;
	
	public JFMLEnumeration_StandardAndMethodType(){
		MIN = StandardAndMethodType.MIN;
	    PROD = StandardAndMethodType.PROD;
	    BDIF = StandardAndMethodType.BDIF;
	    DRP = StandardAndMethodType.DRP;
	    EPROD = StandardAndMethodType.EPROD;
	    HPROD = StandardAndMethodType.HPROD;
	    NILMIN = StandardAndMethodType.NILMIN;
	}
	
	public StandardAndMethodType fromValue(String v){
		return StandardAndMethodType.fromValue(v);
	}
	
}
