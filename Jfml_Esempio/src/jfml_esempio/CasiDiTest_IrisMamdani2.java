package jfml_esempio;

import java.io.File;

import jfml.FuzzyInferenceSystem;
import jfml.JFML;
import jfml.knowledgebase.variable.KnowledgeBaseVariable;

public class CasiDiTest_IrisMamdani2 {

	public static void main(String[] args) {
		// Loading Fuzzy System from an XML file according the standard IEEE
		// 1855
		File xml = new File("./XMLFiles/IrisMamdani2.xml");
		FuzzyInferenceSystem fs = JFML.load(xml);
		float[] limitiSL = { 4.3f, 7.9f, 6.1f };
		float[] limitiSW = { 2f, 4.4f, 3.2f };
		float[] limitiPL = { 1f, 6.9f, 3.9f };
		float[] limitiPW = { 0.1f, 2.5f, 1.2f };
		// Set inputs values SepalLength
		KnowledgeBaseVariable fuzzyVarSP;

		// Set inputs values SepalWidth
		KnowledgeBaseVariable fuzzyVarSW;

		// Set inputs values PetalLength
		KnowledgeBaseVariable fuzzyVarPL;

		// Set inputs values PetalWidth
		KnowledgeBaseVariable fuzzyVarPW;

		for (int i = 0; i < limitiSL.length; i++) {
			fuzzyVarSP = fs.getVariable("SepalLength");
			fuzzyVarSP.setValue(limitiSL[i]);
			for (int j = 0; j < limitiSW.length; j++) {
				fuzzyVarSW = fs.getVariable("SepalWidth");
				fuzzyVarSW.setValue(limitiSW[j]);
				for (int j2 = 0; j2 < limitiPL.length; j2++) {
					fuzzyVarPL = fs.getVariable("PetalLength");
					fuzzyVarPL.setValue(limitiPL[j2]);
					for (int k = 0; k < limitiPW.length; k++) {
						fuzzyVarPW = fs.getVariable("PetalWidth");
						fuzzyVarPW.setValue(limitiPW[k]);
						// Fuzzy inference test System Fuzzy
						fs.evaluate();

						// Get output test System Fuzzy
						KnowledgeBaseVariable irisClass = fs.getVariable("irisClass");
						float value = irisClass.getValue();

						// Printing results System Fuzzy
						System.out.println("RESULTS System Fuzzy");
						System.out.println(" (INPUT): " + fuzzyVarSP.getName() + "=" + fuzzyVarSP.getValue()
								+ fuzzyVarSW.getName() + "=" + fuzzyVarSW.getValue() + fuzzyVarPL.getName() + "="
								+ fuzzyVarPL.getValue() + fuzzyVarPW.getName() + "=" + fuzzyVarPW.getValue());
						System.out.println(" (OUTPUT): " + irisClass.getName() + "=" + value);

						// Printing the FuzzySystem System Fuzzy test
						System.out.println(fs.toString());
					}
				}
			}
		}
		/*
		 * // Fuzzy inference test System Fuzzy fs.evaluate();
		 * 
		 * // Get output test System Fuzzy KnowledgeBaseVariable irisClass =
		 * fs.getVariable("irisClass"); float value = irisClass.getValue();
		 * 
		 * // Printing results System Fuzzy System.out.println(
		 * "RESULTS System Fuzzy"); System.out.println(" (INPUT): " +
		 * fuzzyVarSP.getName() + "=" + fuzzyVarSP.getValue() +
		 * fuzzyVarSW.getName() + "=" + fuzzyVarSW.getValue() +
		 * fuzzyVarPL.getName() + "=" + fuzzyVarPL.getValue() +
		 * fuzzyVarPW.getName() + "=" + fuzzyVarPW.getValue());
		 * System.out.println(" (OUTPUT): " + irisClass.getName() + "=" +
		 * value);
		 * 
		 * // Printing the FuzzySystem System Fuzzy test
		 * System.out.println(fs.toString());
		 */
	}

}
