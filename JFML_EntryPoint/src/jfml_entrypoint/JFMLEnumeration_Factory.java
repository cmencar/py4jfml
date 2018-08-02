package jfml_entrypoint;

import jfml_entrypoint.enumeration.JFMLEnumeration_InterpolationMethodType;
import jfml_entrypoint.enumeration.JFMLEnumeration_MonotonicInterpolationMethodType;
import jfml_entrypoint.enumeration.JFMLEnumeration_StandardAccumulationType;
import jfml_entrypoint.enumeration.JFMLEnumeration_StandardActivationMethodType;
import jfml_entrypoint.enumeration.JFMLEnumeration_StandardAndMethodType;
import jfml_entrypoint.enumeration.JFMLEnumeration_StandardCombinationType;
import jfml_entrypoint.enumeration.JFMLEnumeration_StandardDefuzzifierType;
import jfml_entrypoint.enumeration.JFMLEnumeration_StandardModifierType;
import jfml_entrypoint.enumeration.JFMLEnumeration_StandardOrMethodType;
import jfml_entrypoint.enumeration.JFMLEnumeration_StandardTconormType;
import jfml_entrypoint.enumeration.JFMLEnumeration_StandardTnormType;

public class JFMLEnumeration_Factory {
	
	public JFMLEnumeration_InterpolationMethodType createJFMLEnumeration_InterpolationMethodType(){
		return new JFMLEnumeration_InterpolationMethodType();
	}
	
	public JFMLEnumeration_MonotonicInterpolationMethodType createJFMLEnumeration_MonotonicInterpolationMethodType(){
		return new JFMLEnumeration_MonotonicInterpolationMethodType();
	}
	
	public JFMLEnumeration_StandardAccumulationType createJFML_Enumeration_StandardAccumulationType(){
		return new JFMLEnumeration_StandardAccumulationType();
	}
	
	public JFMLEnumeration_StandardActivationMethodType createJFMLEnumeration_StandardActivationMethodType(){
		return new JFMLEnumeration_StandardActivationMethodType();
	}
	
	public JFMLEnumeration_StandardAndMethodType createJFMLEnumeration_StandardAndMethodType(){
		return new JFMLEnumeration_StandardAndMethodType();
	}
	
	public JFMLEnumeration_StandardCombinationType createJFMLEnumeration_StandardCombinationType(){
		return new JFMLEnumeration_StandardCombinationType();
	}
	
	public JFMLEnumeration_StandardDefuzzifierType createJFMLEnumeration_StandardDefuzzifierType(){
		return new JFMLEnumeration_StandardDefuzzifierType();
	}
	
	public JFMLEnumeration_StandardModifierType createJFMLEnumeration_StandardModifierType(){
		return new JFMLEnumeration_StandardModifierType();
	}
	
	public JFMLEnumeration_StandardOrMethodType createJFMLEnumeration_StandardOrMethodType(){
		return new JFMLEnumeration_StandardOrMethodType();
	}
	
	public JFMLEnumeration_StandardTconormType createJFMLEnumeration_StandardTconormType(){
		return new JFMLEnumeration_StandardTconormType();
	}
	
	public JFMLEnumeration_StandardTnormType createJFMLEnumeration_StandardTnormType(){
		return new JFMLEnumeration_StandardTnormType();
	}
}
