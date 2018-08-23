package jfml_entrypoint;

import jfml.compatibility.ExportFCL;
import jfml.compatibility.ExportMatlab;
import jfml.compatibility.ExportPMML;
import jfml.compatibility.ImportFCL;
import jfml.compatibility.ImportMatlab;
import jfml.compatibility.ImportPMML;
import jfml.compatibility.SuppCollection;
import jfml.compatibility.pmmlReader;

/**
 * This class allows to return class instances of the JFML package 'compatibility'.
 *  
 */
public class JFMLCompatibility_Factory {
	
	public ExportFCL createExportFCL()
	{
		return new ExportFCL();
	}
	
	public ExportMatlab createExportMatlab()
	{
		return new ExportMatlab();
	}
	
	public ExportPMML createExportPMML()
	{
		return new ExportPMML();
	}
	
	public ImportFCL createImportFCL()
	{
		return new ImportFCL();
	}
	
	public ImportMatlab createImportMatlab()
	{
		return new ImportMatlab();
	}
	
	public ImportPMML createImportPMML()
	{
		return new ImportPMML();
	}
	
	public pmmlReader createpmmlReader(String filename)
	{
		return new pmmlReader(filename);
	}
	
	public SuppCollection createSuppCollection()
	{
		return new SuppCollection();
	}
}
