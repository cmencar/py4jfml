package jfml_entrypoint.enumeration;
import jfml.enumeration.MonotonicInterpolationMethodType;;

/**
 * This class contains enumerated constants of JFML Enum Type 'MonotonicInterpolationMethodType'.
 * This middle class is needed to use java enumerated constants through Py4J.
 *
 */
public class JFMLEnumeration_MonotonicInterpolationMethodType {
	
	MonotonicInterpolationMethodType linear;
	MonotonicInterpolationMethodType cubic;
	
	public JFMLEnumeration_MonotonicInterpolationMethodType(){
		linear = MonotonicInterpolationMethodType.LINEAR;
		cubic = MonotonicInterpolationMethodType.CUBIC;		
	}
	
	public MonotonicInterpolationMethodType fromValue(String v){
		return MonotonicInterpolationMethodType.fromValue(v);
	}
}
