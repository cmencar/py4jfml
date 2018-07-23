from py4j.java_gateway import JavaGateway

from py4jfml.rule import FuzzyRuleType

gateway = JavaGateway()

class TsukamotoRuleBaseType():
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

#METHODS OF FuzzySystemRuleBase

    def getRuleBaseSystemType(self):
        '''
        Gets the representation of the fuzzy system according to the static variables
        - TYPE_MAMDANI - Mamdani Rule Base
        - TYPE_TSUKAMOTO - tsukamoto Rule Base
        - TYPE_TSK - tsk Rule Base
        - TYPE_ANYA - AnYa Rule Base
        - TYPE_OTHER - other Rule Base
        :return: the representation of the fuzzy system
        '''
        return self.java_fsrb.getRuleBaseSystemType()

    def getRuleBaseSystemTypeName(self):
        '''
        Gets the name of the Rule Base fuzzy system
        - TYPE_MAMDANI - mamdani
        - TYPE_TSUKAMOTO - tsukamoto
        - TYPE_TSK - tsk
        - TYPE_ANYA - anYa
        - TYPE_OTHER - other
        :return: the name of the Rule Base fuzzy system
        '''
        return self.java_fsrb.getRuleBaseSystemTypeName()

    def setRuleBaseSystemType(self, ruleBaseType):
        '''
        Sets the fuzzy system type according to static variables
        - TYPE_MAMDANI - Mamdani Rule Base
        - TYPE_TSUKAMOTO - tsukamoto Rule Base
        - TYPE_TSK - tsk Rule Base
        - TYPE_ANYA - AnYa Rule Base
        - TYPE_OTHER - other Rule Base
        :param ruleBaseType: the type of the rule base
        '''
        assert type(ruleBaseType)==int
        self.java_fsrb.setRuleBaseSystemType(ruleBaseType)



    def addRule(self, rule):
        '''
        Adds a FuzzyRuleType to the list of rules
        :param rule: the FuzzyRuleType
        '''
        assert type(rule)==FuzzyRuleType
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