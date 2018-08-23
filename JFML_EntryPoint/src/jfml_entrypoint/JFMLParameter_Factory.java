package jfml_entrypoint;

import jfml.parameter.FourParamType;
import jfml.parameter.OneParamType;
import jfml.parameter.ParameterType;
import jfml.parameter.ThreeParamType;
import jfml.parameter.TwoParamType;

/**
 * This class allows to return class instances of the JFML package 'parameter'.
 * 
 */
public class JFMLParameter_Factory {

	public FourParamType createFourParamType()
	{
		return new FourParamType(); 
	}
	
	public OneParamType createOneParamType()
	{
		return new OneParamType();
	}
	
	public ParameterType createParameterType()
	{
		return new ParameterType();
	}
	
	public ThreeParamType createThreeParamType()
	{
		return new ThreeParamType();
	}
	
	public TwoParamType createTwoParamType()
	{
		return new TwoParamType();
	}
	
}
