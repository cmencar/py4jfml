package jfml_entrypoint;

import jfml.aggregated.AndAggregatedType;
import jfml.aggregated.OrAggregatedType;
import jfml.rule.ClauseType;

/**
 * This class allows to return class instances of the JFML package 'aggregated'.
 *  
 */
public class JFMLAggregated_Factory {
	
	public AndAggregatedType createAndAggregatedType()
	{
		return new AndAggregatedType();
	}
	
	public AndAggregatedType createAndAggregatedType(AndAggregatedType term1, AndAggregatedType term2)
	{
		return new AndAggregatedType(term1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(AndAggregatedType term1, OrAggregatedType term2)
	{
		return new AndAggregatedType(term1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(ClauseType c1, AndAggregatedType term2)
	{
		return new AndAggregatedType(c1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(ClauseType c1, ClauseType c2)
	{
		return new AndAggregatedType(c1,c2);
	}
	
	public AndAggregatedType createAndAggregatedType(ClauseType c1, OrAggregatedType term2)
	{
		return new AndAggregatedType(c1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(OrAggregatedType term1, AndAggregatedType term2)
	{
		return new AndAggregatedType(term1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(OrAggregatedType term1, OrAggregatedType term2)
	{
		return new AndAggregatedType(term1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(String tNorm, AndAggregatedType term1, AndAggregatedType term2)
	{
		return new AndAggregatedType(term1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(String tNorm, AndAggregatedType term1, OrAggregatedType term2)
	{
		return new AndAggregatedType(tNorm,term1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(String tNorm, ClauseType c1, AndAggregatedType term2)
	{
		return new AndAggregatedType(tNorm,c1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(String tNorm, ClauseType c1, ClauseType c2)
	{
		return new AndAggregatedType(tNorm,c1,c2);
	}
	
	public AndAggregatedType createAndAggregatedType(String tNorm, ClauseType c1, OrAggregatedType term2)
	{
		return new AndAggregatedType(tNorm,c1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(String tNorm, OrAggregatedType term1, AndAggregatedType term2)
	{
		return new AndAggregatedType(tNorm,term1,term2);
	}
	
	public AndAggregatedType createAndAggregatedType(String tNorm, OrAggregatedType term1, OrAggregatedType term2)
	{
		return new AndAggregatedType(tNorm,term1,term2);
	}
	
	
	public OrAggregatedType createOrAggregatedType()
	{
		return new OrAggregatedType();
	}
	
	public OrAggregatedType createOrAggregatedType(AndAggregatedType term1, AndAggregatedType term2)
	{
		return new OrAggregatedType(term1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(AndAggregatedType term1, OrAggregatedType term2)
	{
		return new OrAggregatedType(term1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(ClauseType c1, AndAggregatedType term2)
	{
		return new OrAggregatedType(c1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(ClauseType c1, ClauseType c2)
	{
		return new OrAggregatedType(c1,c2);
	}
	
	public OrAggregatedType createOrAggregatedType(ClauseType c1, OrAggregatedType term2)
	{
		return new OrAggregatedType(c1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(OrAggregatedType term1, AndAggregatedType term2)
	{
		return new OrAggregatedType(term1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(OrAggregatedType term1, OrAggregatedType term2)
	{
		return new OrAggregatedType(term1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(String tConorm, AndAggregatedType term1, AndAggregatedType term2)
	{
		return new OrAggregatedType(tConorm,term1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(String tConorm, AndAggregatedType term1, OrAggregatedType term2)
	{
		return new OrAggregatedType(tConorm,term1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(String tConorm, ClauseType c1, AndAggregatedType term2)
	{
		return new OrAggregatedType(tConorm,c1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(String tConorm, ClauseType c1, ClauseType c2)
	{
		return new OrAggregatedType(tConorm,c1,c2);
	}
	
	public OrAggregatedType createOrAggregatedType(String tConorm, ClauseType c1, OrAggregatedType term2)
	{
		return new OrAggregatedType(tConorm,c1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(String tConorm, OrAggregatedType term1, AndAggregatedType term2)
	{
		return new OrAggregatedType(tConorm,term1,term2);
	}
	
	public OrAggregatedType createOrAggregatedType(String tConorm, OrAggregatedType term1, OrAggregatedType term2)
	{
		return new OrAggregatedType(tConorm,term1,term2);
	}
	
}
