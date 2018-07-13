import py4jfml.py4jfml.Py4Jfml as fml
import cProfile


#valuto l'efficienza del programma per vedere se i tempi di accesso alla libreria JFML non sia maggiore del tempo di esecuzione
pr = cProfile.Profile()
pr.enable()
fml.FuzzyInferenceSystem()
pr.disable()
pr.print_stats(sort="calls")