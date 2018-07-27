from py4j.java_gateway import JavaGateway
from py4jfml.rule import FuzzyRuleType as frt
from py4jfml.rulebase import RuleBaseType as rbt

gateway = JavaGateway()

class TsukamotoRuleBaseType(rbt.RuleBaseType):
    '''
    Python class for implementing Tsukamoto rule base fuzzy systems
    '''

    def __init__(self, name=None, ruleBaseType=None, activation=None, andAlgorithm=None, orAlgorithm=None):
        '''
        :param name: name of the tsukamoto rule base
        :param ruleBaseType: the ruleBaseSystemType
        :param activation: the method used for the implication process according to StandardActivationMethodType
        :param andAlgorithm: the and algorithm to be used
        :param orAlgorithm: the or algorithm to be used
        '''
        super().__init__()
        if name==None and ruleBaseType==None and activation==None and andAlgorithm==None and orAlgorithm==None:
            self.java_fsrb = gateway.entry_point.getJFMLRulebase_Factory().createTsukamotoRuleBaseType()
        elif name!=None and ruleBaseType==None and activation==None and andAlgorithm==None and orAlgorithm==None:
            assert type(name)==str
            self.java_fsrb = gateway.entry_point.getJFMLRulebase_Factory().createTsukamotoRuleBaseType(name)
        elif name!=None and ruleBaseType!=None and activation!=None and andAlgorithm!=None and orAlgorithm!=None:
            assert type(name)==str and type(activation)==str and type(andAlgorithm)==str and type(orAlgorithm)==str and type(ruleBaseType)==int
            self.java_fsrb = gateway.entry_point.getJFMLRulebase_Factory().createTsukamotoRuleBaseType(name, activation, andAlgorithm, orAlgorithm, ruleBaseType)

    def addRule(self, rule):
        '''
        Adds a FuzzyRuleType to the list of rules
        :param rule: the FuzzyRuleType
        '''
        assert type(rule)==frt.FuzzyRuleType
        self.java_fsrb.addRule(rule.java_r)

    def evaluate(self):
        '''
        Evaluate the rules of the rule base
        '''
        self.java_fsrb.evaluate()

    def getActivatedRules(self):
        '''
        gets a string with the activated rules
        :return: possible object is string
        '''
        return self.java_fsrb.getActivatedRules()

    def getActivationMethod(self):
        '''
        Gets the value of the property activationMethod
        :return: possible object is string
        '''
        return self.java_fsrb.getActivationMethod()

    def getAndMethod(self):
        '''
        Gets the value of the property andMethod
        :return: possible object is string
        '''
        return self.java_fsrb.getAndMethod()

    def getName(self):
        '''
        Gets the value of the property name
        :return: possible object is string
        '''
        return self.java_fsrb.getName()

    def getNetworkAddress(self):
        '''
        Gets the value of the property networkAddress
        :return: possible object is string
        '''
        return self.java_fsrb.getNetworkAddress()

    def getOrMethod(self):
        '''
        Gets the value of the property orMethod
        :return: possible object is string
        '''
        return self.java_fsrb.getOrMethod()

    def getRules(self):
        '''
        Gets the value of the rule property
        :return: possible object is a list of FuzzyRuleType
        '''
        return self.java_fsrb.getRules()

    def reset(self):
        '''
        '''
        self.java_fsrb.reset()

    def setActivationMethod(self, value):
        '''
        Sets the value of the property activationMethod
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_fsrb.setActivationMethod(value)

    def setAndMethod(self, value):
        '''
        Sets the value of the property andMethod
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_fsrb.setAndMethod(value)

    def setName(self, value):
        '''
        Sets the value of the property name
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_fsrb.setName(value)

    def setNetworkAddress(self, value):
        '''
        Sets the value of the property networkAddress
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_fsrb.setNetworkAddress(value)

    def setOrMethod(self, value):
        '''
        Sets the value of the property orMethod
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_fsrb.setOrMethod(value)

    def __str__(self):
        '''
        Returns a String object representing this variable
        :return: possible object is String
        '''
        return self.java_fsrb.toString()