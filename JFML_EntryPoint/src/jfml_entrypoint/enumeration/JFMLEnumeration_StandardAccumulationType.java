package jfml_entrypoint.enumeration;
import jfml.enumeration.StandardAccumulationType;;

/**
 * This class contains enumerated constants of JFML Enum Type 'StandardAccumulationType'.
 * This middle class is needed to use java enumerated constants through Py4J.
 *
 */
public class JFMLEnumeration_StandardAccumulationType {
	StandardAccumulationType MAX;
	StandardAccumulationType PROBOR;
	StandardAccumulationType BSUM;
	StandardAccumulationType DRS;
	StandardAccumulationType ESUM;
	StandardAccumulationType HSUM;
	StandardAccumulationType NILMAX;
	
	public JFMLEnumeration_StandardAccumulationType(){
		MAX = StandardAccumulationType.MAX;
		PROBOR = StandardAccumulationType.PROBOR;
		BSUM = StandardAccumulationType.BSUM;
		DRS = StandardAccumulationType.DRS;
		ESUM = StandardAccumulationType.ESUM;
		HSUM = StandardAccumulationType.HSUM;
		NILMAX = StandardAccumulationType.NILMAX;
	}
	
	public StandardAccumulationType fromValue(String v){
		return StandardAccumulationType.fromValue(v);
	}
	
}
