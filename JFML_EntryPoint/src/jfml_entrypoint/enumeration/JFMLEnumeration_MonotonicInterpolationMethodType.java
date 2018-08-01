package jfml_entrypoint.enumeration;
import jfml.enumeration.MonotonicInterpolationMethodType;;

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
