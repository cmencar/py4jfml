package jfml_entrypoint;

import java.util.List;

import jfml.defuzzifier.DefuzzifierCenterOfArea;
import jfml.defuzzifier.DefuzzifierCenterOfGravity;
import jfml.defuzzifier.DefuzzifierCenterOfGravitySingletons;
import jfml.defuzzifier.DefuzzifierLeftMostMax;
import jfml.defuzzifier.DefuzzifierMeanMax;
import jfml.defuzzifier.DefuzzifierRightMostMax;
import jfml.term.FuzzyTermType;

public class JFMLDefuzzifier_Factory {
	
	public DefuzzifierCenterOfArea createDefuzzifierCenterOfArea(float domainleft, float domainright, List<FuzzyTermType> terms)
	{
		return new DefuzzifierCenterOfArea(domainleft,domainright,terms);
	}
	
	public DefuzzifierCenterOfGravity createDefuzzifierCenterOfGravity(float domainleft, float domainright, List<FuzzyTermType> terms)
	{
		return new DefuzzifierCenterOfGravity(domainleft,domainright,terms);
	}
	
	public DefuzzifierCenterOfGravitySingletons createDefuzzifierCenterOfGravitySingletons(float leftDomain, float rightDomain) 
	{
		return new DefuzzifierCenterOfGravitySingletons(leftDomain, rightDomain);
	}
	
	public DefuzzifierLeftMostMax createDefuzzifierLeftMostMax(float domainleft, float domainright, List<FuzzyTermType> terms)
	{
		return new DefuzzifierLeftMostMax(domainleft,domainright,terms);
	}
	
	public DefuzzifierMeanMax createDefuzzifierMeanMax(float domainleft, float domainright, List<FuzzyTermType> terms) 
	{
		return new DefuzzifierMeanMax(domainleft,domainright,terms);
	}

	public DefuzzifierRightMostMax createDefuzzifierRightMostMax(float domainleft, float domainright, List<FuzzyTermType> terms) 
	{
		return new DefuzzifierRightMostMax(domainleft,domainright,terms);
	}

}
