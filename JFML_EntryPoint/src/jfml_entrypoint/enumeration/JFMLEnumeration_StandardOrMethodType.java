package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardOrMethodType;

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
