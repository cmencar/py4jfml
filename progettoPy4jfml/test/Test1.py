import py4jfml.Py4jfml as fml
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()


#caricamento Mamdani
str_xml = "C:\\Users\\andrea\\PycharmProjects\\untitled\\progettoPy4jfml\\XMLFiles\\TipperMamdani1.xml"
tipper = fml.PY4JFML.load(str_xml)

#imposto i valori di input
food = tipper.getVariable("food")
service = tipper.getVariable("service")
food.setValue(6.)
service.setValue(8.)

#valuto il sistema
tipper.evaluate()

#ottengo output
tip = tipper.getVariable("tip")
value = tip.getValue()

#stampo i risultati
print("RESULT:")
print(" (INPUT): " + str(food.getName()) + " = " + str(food.getValue()) + ", " + str(service.getName()) + "=" + str(service.getValue()))
print(" (OUTPUT): " + str(tip.getName()) + " = " + str(value))

#stampo il sistema Fuzzy
print(tipper)