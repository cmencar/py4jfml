from py4j.java_gateway import JavaGateway
from py4jfml.Py4Jfml import Py4jfml
import os

gateway = JavaGateway()

#percorso del file xml da valutare
str_xml = os.getcwd()+"/"+ "IrisMamdani2.xml"


#Sistema fuzzy
fs = Py4jfml.load(str_xml)
#limite minimo massimo e medio SepalLength
limitiSL = [4.3, 7.9, 6.1]

#limite minimo massimo e medio SepalWidth
limitiSW = [2., 4.4, 3.2]

#limite minimo massimo e medio PetalLength
limitiPL = [1., 6.9, 3.9]

#limite minimo massimo e medio PetalWidth
limitiPW = [0.1, 2.5, 1.2]

for i in range(3):
    fuzzyVarSL = fs.getVariable("SepalLength")

    #imposto i valori
    fuzzyVarSL.setValue(float(limitiSL[i]))
    for j in range(3):
        fuzzyVarSW = fs.getVariable("SepalWidth")

        # imposto i valori
        fuzzyVarSW.setValue(float(limitiSW[j]))
        for j2 in range(3):
            fuzzyVarPL = fs.getVariable("PetalLength")

            # imposto i valori
            fuzzyVarPL.setValue(float(limitiPL[j2]))
            for k in range(3):
                fuzzyVarPW = fs.getVariable("PetalWidth")

                # imposto i valori
                fuzzyVarPW.setValue(float(limitiPW[k]))

                #valuto il sistema fuzzy
                fs.evaluate()

                #ottengo valori di output
                irisClass = fs.getVariable("irisClass")
                value = irisClass.getValue()

                # stampo i risultati del sistema fuzzy
                print("RESULTS System Fuzzy")
                print(" (INPUT): " + str(fuzzyVarSL.getName()) + "=" + str(fuzzyVarSL.getValue()) + str(fuzzyVarSW.getName()) + "=" + str(fuzzyVarSW.getValue()) + str(fuzzyVarPL.getName()) + "=" + str(fuzzyVarPL.getValue()) + str(fuzzyVarPW.getName()) + "=" + str(fuzzyVarPW.getValue()))
                print(" (OUTPUT): " + str(irisClass.getName()) + "=" + str(value))

                # stampo il sistema fuzzy
                print("System Fuzzy: ")
                print(fs)
