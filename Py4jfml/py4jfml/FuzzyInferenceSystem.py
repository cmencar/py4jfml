from py4jfml.knowledgebase import KnowledgeBaseType as kbt
from py4jfml.rulebase import MamdaniRuleBaseType as mrbt
from py4jfml.jaxb import FuzzySystemType as fst
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class FuzzyInferenceSystem(fst.FuzzySystemType):
    """
    Python class to create a FuzzyInferenceSystem
    """
    def __init__(self,name=None):
        """
        Constructor of class FuzzyInferenceSystem
        :param name: the name of the fuzzy system
        """
        super().__init__(name)
        #Calling java default constructor
        if name==None:
            self.java_fis = gateway.entry_point.getJFML_Factory().createFuzzyInferenceSystem()

        #Call of the java constructor using the name of the FuzzySystem
        elif type(name)==str:
            assert type(name)==str
            self.java_fis = gateway.entry_point.getJFML_Factory().createFuzzyInferenceSystem(str(name))

        #Call of the java constructor using another FuzzySystemType instance
        else:
            #assert type(name)==FuzzyInferenceSystem or type(name)==fst.FuzzySystemType
            self.java_fis = gateway.entry_point.getJFML_Factory().createFuzzyInferenceSystem(name)