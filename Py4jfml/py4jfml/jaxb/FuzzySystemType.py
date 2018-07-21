from py4jfml.knowledgebase.KnowledgeBaseType import *
from py4jfml.rulebase.AnYaRuleBaseType import *
from py4jfml.rulebase.RuleBaseType import *
from py4jfml.rulebase.MamdaniRuleBaseType import *
from py4jfml.rulebase.TskRuleBaseType import *
from py4jfml.rulebase.TsukamotoRuleBaseType import *
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class FuzzySystemType:

    '''
    Python class for the fuzzySystemType complex type
    '''

    def __init__(self, name=None, knowledgeBase=None, ruleBase=None, networkAddress=None):
        '''
        :param name: the fuzzy System name
        :param knowledgeBase: an instance of class KnowledgeBaseType
        :param ruleBase: a list of objects of class Object
        :param networkAddress: the value of the networkAddress
        '''
        if name==None and knowledgeBase==None and ruleBase==None and networkAddress==None :
            self.java_fst = gateway.entry_point.getJFMLjaxb_Factory().createFuzzySystemType()
        elif knowledgeBase==None and ruleBase==None and networkAddress==None :
            assert type(name)==str
            self.java_fst = gateway.entry_point.getJFMLjaxb_Factory().createFuzzySystemType(name)
        elif knowledgeBase!=None and ruleBase!=None and networkAddress!=None:
            assert type(name)==str and type(knowledgeBase)==KnowledgeBaseType and type(ruleBase)==list and type(networkAddress)==str
            self.java_fst = gateway.entry_point.getJFMLjaxb_Factory().createFuzzySystemType(name, knowledgeBase.java_kbt, ruleBase, networkAddress)

    def addRuleBase(self,r):
        '''
        Adds a new RuleBase to the fuzzySystem
        :param r: allowed object is FuzzySystemRuleBase
        '''
        assert type(r)==AnYaRuleBaseType or type(r)==TskRuleBaseType or type(r) == RuleBaseType or type(r)==MamdaniRuleBaseType or type(r)==TsukamotoRuleBaseType
        self.java_fst.addRuleBase(r.java_fsrb)

    def evaluate(self):
        '''
        Evaluate the fuzzy system
        '''
        self.java_fst.evaluate()

    def getAllRuleBase(self):
        '''
        Gets an array with all the rule bases
        :return: an array with all the rule bases
        '''
        return self.java_fst.getAllRuleBase()

    def getInferenceResults(self):
        '''
        Gets a string with the results
        :return: a String with results
        '''
        return self.java_fst.getInferenceResults()

    def getJAXBElement(self):
        '''
        :return: the JAXBE element
        '''
        return self.java_fst.getJAXBElement()

    def getKnowledgeBase(self):
        '''
        Gets the value of the knowledgeBase property
        :return: possible object is KnowledgeBaseType
        '''
        return self.java_fst.getKnowledgeBase()

    def getName(self):
        '''
        Gets the value of the name property
        :return: possible object is String
        '''
        return self.java_fst.getName()

    def getNetworkAddress(self):
        '''
        Gets the value of the networkAddress property
        :return: possible object is String
        '''
        return self.java_fst.getNetworkAddress()

    def getRuleBase(self, index=None):
        '''
        if the parameter index is none, gets the value of the ruleBase property;
        else gets the FuzzySystemRuleBase from the list of RuleBase by the parameter index
        :param index: the index of the rulebase
        :return: if the parameter index is none, returns a list of RuleBase; else returns a FuzzySystemRuleBase or null if the index does not match
        '''
        if index==None:
            return self.java_fst.getRuleBase()
        else:
            assert type(index)==int
            return self.java_fst.getRuleBase(index)

    def getVariable(self, name):
        '''
        Return a variable instance identifies by its name
        :param name: allowed object is String
        :return: allowed object is KnowledgeBaseVariable
        '''
        assert type(name)==str
        return self.java_fst.getVariable(name)

    def getVariables(self):
        '''
        Return a variable instance identifies by its name
        :return: allowed object is KnowledgeBaseVariable
        '''
        return self.java_fst.getVariables()

    def setKnowledgeBase(self, value):
        '''
        Sets the value of the knowledgeBase property
        :param value: allowed object is KnowledgeBaseType
        '''
        assert type(value)==KnowledgeBaseType
        self.java_fst.setKnowledgeBase(value.java_kbt)

    def setName(self, value):
        '''
        Sets the value of the name property
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_fst.setName(value)

    def setNetworkAddress(self, value):
        '''
        Sets the value of the networkAddress property
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_fst.setNetworkAddress(value)

    def setVariableValue(self,var,value):
        '''
        Set a value to a variable identifies by its name
        :param var: allowed object is String
        :param value: allowed object is float
        '''
        assert type(var)==str and type(value)==float
        self.java_fst.setVariableValue(var,value)

    def __str__(self):
        '''
        Returns a String object representing this object
        :return: allowed object is String
        '''
        return self.java_fst.toString()
