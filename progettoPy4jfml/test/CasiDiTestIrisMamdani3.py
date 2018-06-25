import py4jfml.Py4jfml as fml
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

#percorso del file xml da valutare
str_xml = "C:\\Users\\andrea\\PycharmProjects\\untitled\\progettoPy4jfml\\XMLFiles\\IrisMamdani3.xml"

#creazione sistema fuzzy
fs1 = fml.PY4JFML.load(str_xml)
fs2 = fml.PY4JFML.load(str_xml)
fs3 = fml.PY4JFML.load(str_xml)

#imposto i valori di input

#caso limite minimo
pw1 = fs1.getVariable("PetalWidth")
pw1.setValue(0.1)
#caso medio
pw2 = fs2.getVariable("PetalWidth")
pw2.setValue(2.5)
#caso limite massimo
pw3 = fs3.getVariable("PetalWidth")
pw3.setValue(1.2)

#valutazione fuzzy test 1
fs1.evaluate()

#valutazione fuzzy test 2
fs2.evaluate()

#valutazione fuzzy test 3
fs3.evaluate()

#ottengo valore output test 1
irisClass1 = fs1.getVariable("irisClass")
value1 = irisClass1.getValue()

#ottengo valore output test 2
irisClass2 = fs2.getVariable("irisClass")
value2 = irisClass2.getValue()

#ottengo valore output test 3
irisClass3 = fs3.getVariable("irisClass")
value3 = irisClass3.getValue()

#stampo i risultati pw1
print("RESULTS1")
print(" (INPUT): " + str(pw1.getName()) + "=" + str(pw1.getValue()))
print(" (OUTPUT): " + str(irisClass1.getName()) + "=" + str(value1))

#stampo i risultati pw2
print("RESULTS2")
print(" (INPUT): " + str(pw2.getName()) + "=" + str(pw2.getValue()))
print(" (OUTPUT): " + str(irisClass2.getName()) + "=" + str(value2))

#stampo i risultati pw3
print("RESULTS3")
print(" (INPUT): " + str(pw3.getName()) + "=" + str(pw3.getValue()))
print(" (OUTPUT): " + str(irisClass3.getName()) + "=" + str(value3))

#stampo il sistema fuzzy test 1
print("PRIMO SISTEMA FUZZY")
print(fs1)
#stampo il sistema fuzzy test 2
print("SECONDO SISTEMA FUZZY")
print(fs2)
#stampo il sistema fuzzy test 3
print("TERZO SISTEMA FUZZY")
print(fs3)