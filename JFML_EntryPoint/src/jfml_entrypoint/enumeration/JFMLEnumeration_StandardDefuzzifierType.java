package jfml_entrypoint.enumeration;

import jfml.enumeration.StandardDefuzzifierType;

public class JFMLEnumeration_StandardDefuzzifierType {
	
	StandardDefuzzifierType MOM;
	StandardDefuzzifierType LM;
	StandardDefuzzifierType RM;
	StandardDefuzzifierType COG;
	StandardDefuzzifierType COA;
	
	public JFMLEnumeration_StandardDefuzzifierType(){
		MOM = StandardDefuzzifierType.MOM;
		LM = StandardDefuzzifierType.LM;
		RM = StandardDefuzzifierType.RM;
		COG = StandardDefuzzifierType.COG;
		COA = StandardDefuzzifierType.COA;
	}
	
	public StandardDefuzzifierType fromValue(String v){
		return StandardDefuzzifierType.fromValue(v);
	}
	
}
