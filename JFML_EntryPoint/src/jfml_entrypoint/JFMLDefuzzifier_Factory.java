package jfml_entrypoint;

import java.util.List;

import jfml.defuzzifier.DefuzzifierCenterOfArea;
import jfml.defuzzifier.DefuzzifierCenterOfGravity;
import jfml.term.FuzzyTermType;

public class JFMLDefuzzifier_Factory 
{
	public DefuzzifierCenterOfArea createDefuzzifierCenterOfArea(float domainleft, float domainright, List<FuzzyTermType> terms)
	{
		return new DefuzzifierCenterOfArea(domainleft,domainright,terms);
	}
	
	public DefuzzifierCenterOfGravity createDefuzzifierCenterOfGravity(float domainleft, float domainright, List<FuzzyTermType> terms)
	{
		return new DefuzzifierCenterOfGravity(domainleft,domainright,terms);
	}
}
