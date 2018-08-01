package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardTconormType;

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
