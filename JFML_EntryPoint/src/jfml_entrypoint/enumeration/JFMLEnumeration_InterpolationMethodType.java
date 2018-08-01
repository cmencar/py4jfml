package jfml_entrypoint.enumeration;
import jfml.enumeration.InterpolationMethodType;

public class JFMLEnumeration_InterpolationMethodType {
	
	InterpolationMethodType linear;
	InterpolationMethodType lagrange;
	InterpolationMethodType spline;
	
	public JFMLEnumeration_InterpolationMethodType() {
		linear = InterpolationMethodType.LINEAR;
		lagrange = InterpolationMethodType.LAGRANGE;
		spline = InterpolationMethodType.SPLINE;
	}
	
	public InterpolationMethodType fromValue(String v){
		return InterpolationMethodType.fromValue(v);
	}
}
