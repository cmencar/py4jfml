package jfml_esempio;

import java.io.File;

import jfml.FuzzyInferenceSystem;
import jfml.JFML;
import jfml.knowledgebase.variable.KnowledgeBaseVariable;

public class Jfml_FuzzyInference {

		public static void main(String[] args) {
            // Loading Fuzzy System from an XML file according the standard IEEE 1855
            File xml = new File("C:/Users/andrea/workspace/Jfml_Esempio/src/jfml_esempio/XMLFiles/TipperMamdani1.xml");
            FuzzyInferenceSystem tipper = JFML.load(xml);
            
            FuzzyInferenceSystem fs = new FuzzyInferenceSystem(tipper);
            // Set inputs values
            KnowledgeBaseVariable food =  fs.getVariable("food");
            KnowledgeBaseVariable service =  fs.getVariable("service");
            food.setValue(6);
            service.setValue(8);
            
            // Fuzzy inference
            tipper.evaluate();	
            
            // Get output
            KnowledgeBaseVariable tip =  fs.getVariable("tip");
            float value = tip.getValue();
            
            // Printing results
            System.out.println("RESULTS");
            System.out.println(" (INPUT): " + food.getName() + "=" + food.getValue() + ", " + service.getName() + "=" + service.getValue());
            System.out.println(" (OUTPUT): " + tip.getName() + "=" + value);
            
            
            // Printing the FuzzySystem
            System.out.println(fs.toString());
        }


	}


