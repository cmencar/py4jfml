import click
import py4jfml.Py4Jfml as fml
from py4j.java_gateway import JavaGateway
from py4jfml.FuzzyInferenceSystem import *

@click.command()
@click.option('-l', '--load', default="", help=": Load xml file")
@click.option('-w', '--write', default="", help=": Write xml file")
@click.option('-t', '--tipper', default="", help=": Tipper")
@click.option('-m', '--mamdani', default="", help=": Mamdami Rule Base")

def startCLI(load, write, tipper, mamdani):
    #Opzione load
    if load is not "":
        fml.Py4jfml.load(load)
        
        print('File uploaded successfully!')
    #Opzione write
    if write is not "" and tipper is not "" and mamdani is not "":
        #Creazione oggetto tipper
        tipperObj = FuzzyInferenceSystem(tipper)
        
        #Creazione dell'oggetto kb e aggiunta all'insieme di conoscenza fuzzy
        kb = KnowledgeBaseType()
        tipperObj.setKnowledgeBase(kb)
        
        #Creazione oggetto MamdaniRB1 con aggiunta regole mandami
        rbMam = MamdaniRuleBaseType(mamdani)
        tipperObj.addRuleBase(rbMam)
        
        #Scrittura file
        fml.Py4jfml.writeFSTtoXML(tipperObj, write)
        
        print('File written successfully!')
        
if __name__ == '__main__':
    startCLI()