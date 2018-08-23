package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardActivationMethodType;

/**
 * This class contains enumerated constants of JFML Enum Type 'StandardActivationMethodType'.
 * This middle class is needed to use java enumerated constants through Py4J.
 *
 */
public class JFMLEnumeration_StandardActivationMethodType {
	
	StandardActivationMethodType MIN;
	StandardActivationMethodType PROD;
	StandardActivationMethodType BDIF;
	StandardActivationMethodType DRP;
	StandardActivationMethodType EPROD;
	StandardActivationMethodType HPROD;
	StandardActivationMethodType NILMIN;
	
	public JFMLEnumeration_StandardActivationMethodType(){
		MIN = StandardActivationMethodType.MIN;
	    PROD = StandardActivationMethodType.PROD;
	    BDIF = StandardActivationMethodType.BDIF;
	    DRP = StandardActivationMethodType.DRP;
	    EPROD = StandardActivationMethodType.EPROD;
	    HPROD = StandardActivationMethodType.HPROD;
	    NILMIN = StandardActivationMethodType.NILMIN;
	}
	
	public StandardActivationMethodType fromValue(String v){
		return StandardActivationMethodType.fromValue(v);
	}
	
}
