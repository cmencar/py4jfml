from py4jfml.knowledgebase import KnowledgeBaseType as kbt
from py4jfml.rulebase import MamdaniRuleBaseType as mrbt
from py4jfml.jaxb import FuzzySystemType as fst
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()


class FuzzyInferenceSystem:
    """
    Python class to create a FuzzyInferenceSystem
    """
    def __init__(self,name=None):
        """
        Constructor of class FuzzyInferenceSystem
        :param name: the name of the fuzzy system
        """
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

    def setKnowledgeBase(self, value):
        """
        Sets the value of the knowledgeBase property.
        :param value: allowed object is KnowledgeBaseType
        """
        assert type(value)==kbt.KnowledgeBaseType
        self.java_fis.setKnowledgeBase(value.java_kbt)

    def setName(self,value):
        '''
        Sets the value of the name property
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_fis.setName(value)

    def setNetworkAddress(self,value):
        '''
        Sets the value of the networkAddress property
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_fis.setNetworkAddress(value)

    def setVariableValue(self,var,value):
        '''
        Set a value to a variable identifies by its name
        :param var: allowed object is String
        :param value: allowed object is float
        '''
        assert type(var)==str and type(value)==float
        self.java_fis.setVariableValue(var,value)

    def addRuleBase(self,r):
        """
        Adds a new RuleBase to the fuzzySystem
        :param r: allowed object is FuzzySystemRuleBase
        """
        assert type(r)==mrbt.MamdaniRuleBaseType
        self.java_fis.addRuleBase(r.java_fsrb)

    def getAllRuleBase(self):
        '''
        Gets a list with all the rule bases
        :return: a list with all the rule bases
        '''
        return self.java_fis.getAllRuleBase()

    def getInferenceResults(self):
        '''
        Gets a string with inference result
        :return: a string with inference result
        '''
        return self.java_fis.getInferenceResults()

    def getJAXBElement(self):
        '''
        Gets the JAXBE element
        :return: the JAXBE element
        '''
        return self.java_fis.getJAXBElement()

    def getKnowledgeBase(self):
        '''
        Gets the value of the knowledgeBase property
        :return: possible object is KnowledgeBaseType
        '''
        return self.java_fis.getKnowledgeBase()

    def getName(self):
        '''
        Gets the value of the name property
        :return: possible object is String
        '''
        return self.java_fis.getName()

    def getNetworkAddress(self):
        '''
        Gets the value of the networkAddress property
        :return: possible object is String
        '''
        return self.java_fis.getNetworkAddress()

    def getRuleBase(self,index=None):
        '''
        Gets the FuzzySystemRuleBase from the list of RuleBase by the parameter index
        Or Gets the value of the ruleBase property.
        Objects of the following type(s) are allowed in the list Object JAXBElement<RuleBaseType> JAXBElement<TskRuleBaseType> JAXBElement<AnYaRuleBaseType> JAXBElement<RuleBaseType> Element
        :param index: the index of the rulebase
        :return: A FuzzySystemRuleBase or null if the index does not match or a list of RuleBase
        '''
        if index!=None:
            assert type(index)==int
            return self.java_fis.getRuleBase(index)
        elif index==None:
            return self.java_fis.getRuleBase()

    def getVariable(self,name):
        """
        Return a variable instance identifies by its name
        :param name: allowed object is String
        :return: allowed object is KnowledgeBaseVariable
        """
        assert type(name)==str
        return self.java_fis.getVariable(name)

    def getVariables(self):
        '''
        Return a variable instance identifies by its name
        :return: allowed object is a list of KnowledgeBaseVariable
        '''
        return self.java_fis.getVariables()

    def evaluate(self):
        """
        Evaluate the fuzzy system
        """
        self.java_fis.evaluate()

    def __str__(self):
        '''
        Gets the object as a string
        :return: possible object is string
        '''
        return self.java_fis.toString()