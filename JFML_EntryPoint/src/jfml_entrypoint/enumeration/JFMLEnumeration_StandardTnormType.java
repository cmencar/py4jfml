package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardTnormType;

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
