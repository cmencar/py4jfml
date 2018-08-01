package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardAndMethodType;

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
