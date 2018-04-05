package jfml_esempio;

import java.io.File;

import jfml.FuzzyInferenceSystem;
import jfml.JFML;
import jfml.knowledgebase.variable.KnowledgeBaseVariable;

public class CasiDiTest_IrisMamdani1 {

	public static void main(String[] args) {
		// Loading Fuzzy System from an XML file according the standard IEEE
		// 1855
		File xml = new File("./XMLFiles/IrisMamdani1.xml");
		FuzzyInferenceSystem fs1 = JFML.load(xml);
		FuzzyInferenceSystem fs2 = JFML.load(xml);
		FuzzyInferenceSystem fs3 = JFML.load(xml);

		// Set inputs values
		KnowledgeBaseVariable pw1 = fs1.getVariable("PetalWidth");
		pw1.setValue(0.1f);
		KnowledgeBaseVariable pw2 = fs2.getVariable("PetalWidth");
		pw2.setValue(2.5f);
		KnowledgeBaseVariable pw3 = fs3.getVariable("PetalWidth");
		pw3.setValue(1.2f);

		// Fuzzy inference test 1
		fs1.evaluate();

		// Fuzzy inference test 2
		fs2.evaluate();

		// Fuzzy inference test 3
		fs3.evaluate();

		// Get output test 1
		KnowledgeBaseVariable irisClass1 = fs1.getVariable("irisClass");
		float value1 = irisClass1.getValue();

		// Get output test 2
		KnowledgeBaseVariable irisClass2 = fs2.getVariable("irisClass");
		float value2 = irisClass2.getValue();

		// Get output test 3
		KnowledgeBaseVariable irisClass3 = fs3.getVariable("irisClass");
		float value3 = irisClass3.getValue();

		// Printing results pw1
		System.out.println("RESULTS1");
		System.out.println(" (INPUT): " + pw1.getName() + "=" + pw1.getValue());
		System.out.println(" (OUTPUT): " + irisClass1.getName() + "=" + value1);

		// Printing results pw2
		System.out.println("RESULTS2");
		System.out.println(" (INPUT): " + pw2.getName() + "=" + pw2.getValue());
		System.out.println(" (OUTPUT): " + irisClass2.getName() + "=" + value2);

		// Printing results pw3
		System.out.println("RESULTS3");
		System.out.println(" (INPUT): " + pw3.getName() + "=" + pw3.getValue());
		System.out.println(" (OUTPUT): " + irisClass3.getName() + "=" + value3);

		// Printing the FuzzySystem test 1
		System.out.println(fs1.toString());
		// Printing the FuzzySystem test 2
		System.out.println(fs2.toString());
		// Printing the FuzzySystem test 3
		System.out.println(fs3.toString());
		
		
	}

}
