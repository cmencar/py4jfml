package jfml_entrypoint;

import java.util.ArrayList;

import jfml.FuzzyInferenceSystem;
import jfml.JFML;
import jfml.jaxb.FuzzySystemType;
import jfml.knowledgebase.KnowledgeBaseType;
import jfml.knowledgebase.variable.FuzzyVariableType;
import jfml.rule.AntecedentType;
import jfml.rule.ClauseType;
import jfml.rule.ConsequentType;
import jfml.rule.FuzzyRuleType;
import jfml.rulebase.MamdaniRuleBaseType;
import jfml.term.FuzzyTermType;
import py4j.GatewayServer;

public class JFML_EntryPoint {
	// FuzzyInferenceSystem
	public FuzzyInferenceSystem createFuzzyInferenceSystem() {
		return new FuzzyInferenceSystem();
	}

	public FuzzyInferenceSystem createFuzzyInferenceSystem(String name) {
		return new FuzzyInferenceSystem(name);
	}

	public FuzzyInferenceSystem createFuzzyInferenceSystem(FuzzySystemType fst) {
		return new FuzzyInferenceSystem(fst);
	}
	// fine FuzzyInferenceSystem

	// KnowledgeBaseType
	public KnowledgeBaseType createKnowledgeBaseType() {
		return new KnowledgeBaseType();
	}
	// fine KnowledgeBaseType

	// FuzzyVariableType
	public FuzzyVariableType createFuzzyVariableType(String name, float domainLeft, float domainRight) {
		return new FuzzyVariableType(name, domainLeft, domainRight);
	}
	// fine FuzzyVariableType

	// FuzzyTermType
	public FuzzyTermType createFuzzyTermType(String name, int type, ArrayList<Double> param) {
		float[] arFloat = new float[param.size()];
		for (int i = 0; i < param.size(); i++) {
			arFloat[i] = param.get(i).floatValue();
		}
		return new FuzzyTermType(name, type, arFloat);
	}
	// fine FuzzyTermType

	// inizio MamdaniRuleBaseType
	public MamdaniRuleBaseType createMamdaniRuleBaseType(String name) {
		return new MamdaniRuleBaseType(name);
	}
	// fine MamdaniRuleBaseType

	// inizio FuzzyRuleType
	public FuzzyRuleType createFuzzyRuleType() {
		return new FuzzyRuleType();
	}

	public FuzzyRuleType createFuzzyRuleType(String name, String connector, String connectorMethod, float weight) {
		Float weight1 = weight;
		return new FuzzyRuleType(name, connector, connectorMethod, weight1);
	}
	// fine FuzzyRuleType

	// inizio AntecedentType
	public AntecedentType createAntecedentType() {
		return new AntecedentType();
	}
	// fine AntecedentType

	// inizio ConsequentType
	public ConsequentType createConsequentType() {
		return new ConsequentType();
	}
	// fine ConsequentType

	// inizio ClauseType
	public ClauseType createClauseType(Object variable, Object term) {
		return new ClauseType(variable, term);
	}

	public ClauseType createClauseType(Object variable, Object term, String modifier) {
		return new ClauseType(variable, term, modifier);
	}
	// fine ClauseType

	// inizio JFML
	public JFML createJFML() {
		return new JFML();
	}

	// fine JFML

	// avvio server
	public static void main(String[] args) {
		JFML_EntryPoint jf = new JFML_EntryPoint();
		GatewayServer gatewayServer = new GatewayServer(jf);
		gatewayServer.start();
		System.out.println("Gateway Server Started!");

	}

}
