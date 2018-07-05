package jfml_entrypoint;

import jfml.operator.AndLogicalType;
import jfml.operator.OrLogicalType;

public class JFMLOperator_Factory {

	public AndLogicalType createAndLogicalType()
	{
		return new AndLogicalType();
	}
	
	public AndLogicalType createAndLogicalType(AndLogicalType term1, AndLogicalType term2)
	{
		return new AndLogicalType(term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(AndLogicalType term1, OrLogicalType term2)
	{
		return new AndLogicalType(term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(OrLogicalType term1, AndLogicalType term2)
	{
		return new AndLogicalType(term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(OrLogicalType term1, OrLogicalType term2)
	{
		return new AndLogicalType(term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(String term1, AndLogicalType term2)
	{
		return new AndLogicalType(term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(String tNorm, AndLogicalType term1, AndLogicalType term2)
	{
		return new AndLogicalType(tNorm,term1,term2);
	}

	public AndLogicalType createAndLogicalType(String tNorm, AndLogicalType term1, OrLogicalType term2)
	{
		return new AndLogicalType(tNorm,term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(String term1, OrLogicalType term2)
	{
		return new AndLogicalType(term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(String tNorm, OrLogicalType term1, AndLogicalType term2)
	{
		return new AndLogicalType(tNorm,term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(String tNorm, OrLogicalType term1, OrLogicalType term2)
	{
		return new AndLogicalType(tNorm,term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(String term1, String term2)
	{
		return new AndLogicalType(term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(String tNorm, String term1, AndLogicalType term2)
	{
		return new AndLogicalType(tNorm,term1,term2);
	}
	
	public AndLogicalType createAndLogicalType(String tNorm, String term1, OrLogicalType term2)
	{
		return new AndLogicalType(tNorm,term1,term2);
	}

	public AndLogicalType createAndLogicalType(String tNorm, String term1, String term2)
	{
		return new AndLogicalType(tNorm,term1,term2);
	}
	
	public OrLogicalType createOrLogicalType()
	{
		return new OrLogicalType();
	}
	
	public OrLogicalType createOrLogicalType(AndLogicalType term1, AndLogicalType term2)
	{
		return new OrLogicalType(term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(AndLogicalType term1, OrLogicalType term2)
	{
		return new OrLogicalType(term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(OrLogicalType term1, AndLogicalType term2)
	{
		return new OrLogicalType(term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(OrLogicalType term1, OrLogicalType term2)
	{
		return new OrLogicalType(term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(String term1, AndLogicalType term2)
	{
		return new OrLogicalType(term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(String tConorm, AndLogicalType term1, AndLogicalType term2)
	{
		return new OrLogicalType(tConorm,term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(String tConorm, AndLogicalType term1, OrLogicalType term2)
	{
		return new OrLogicalType(tConorm,term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(String term1, OrLogicalType term2)
	{
		return new OrLogicalType(term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(String tConorm, OrLogicalType term1, AndLogicalType term2)
	{
		return new OrLogicalType(tConorm,term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(String tConorm, OrLogicalType term1, OrLogicalType term2)
	{
		return new OrLogicalType(tConorm,term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(String term1, String term2)
	{
		return new OrLogicalType(term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(String tConorm, String term1, OrLogicalType term2)
	{
		return new OrLogicalType(tConorm,term1,term2);
	}
	
	public OrLogicalType createOrLogicalType(String tConorm, String term1, String term2)
	{
		return new OrLogicalType(tConorm,term1,term2);
	}
		
}
