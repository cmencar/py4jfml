from py4j.java_gateway import JavaGateway
from py4jfml.rule import AnYaRuleType as art
from py4jfml.rulebase import FuzzySystemRuleBase as fsrb

gateway = JavaGateway()

class AnYaRuleBaseType(fsrb.FuzzySystemRuleBase):

    '''
    Python for anYaRuleBaseType complex type.
    '''

    def __init__(self, name=None):
        '''
        :param name: the name of AnYa rule base
        '''
        if name==None:
            self.java_fsrb = gateway.entry_point.getJFMLRulebase_Factory().createAnYaRuleBaseType()
        else:
            assert type(name)==str
            self.java_fsrb = gateway.entry_point.getJFMLRulebase_Factory().createAnYaRuleBaseType(name)


    #Three methods of FuzzySystemRuleBase

    def getRuleBaseSystemType(self):
        '''
        Gets the representation of the fuzzy system according to the static variables
        :return: the representation of the fuzzy system
        '''
        return self.java_fsrb.getRuleBaseSystemType()

    def getRuleBaseSystemTypeName(self):
        '''
        Gets the name of the Rule Base fuzzy system
        :return: the name of the Rule Base fuzzy system
        '''
        return self.java_fsrb.getRuleBaseSystemTypeName()

    def setRuleBaseSystemType(self, ruleType):
        '''
        Sets the fuzzy system type according to static variables
        :param type: the type of the rule base
        '''
        assert type(ruleType)==int
        self.java_fsrb.setRuleBaseSystemType(ruleType)



    def addAnYaRule(self, rule):
        '''
        Adds a AnYaRuleType to the list of rules
        :param rule: the AnYaRuleType
        '''
        assert type(rule)==art.AnYaRuleType
        self.java_fsrb.addAnYaRule(rule.java_r)

    def evaluate(self):
        '''
        Evaluates the rules
        '''
        self.java_fsrb.evaluate()

    def getActivatedRules(self):
        '''
        Gets the activated rules
        :return: a String with the activated rules
        '''
        return self.java_fsrb.getActivatedRules()

    def getActivationMethod(self):
        '''
        Gets the value of the property activationMethod
        :return: possible object is String
        '''
        return self.java_fsrb.getActivationMethod()

    def getAnYaRules(self):
        '''
        Gets the value of the anYaRule property
        :return: a list of AnYaRuleType objects
        '''
        return self.java_fsrb.getAnYaRules()

    def getName(self):
        '''
        Gets the value of the property name
        :return: possible object is String
        '''
        return self.java_fsrb.getName()

    def getNetworkAddress(self):
        '''
        Gets the value of the property networkAddress
        :return: possible object is String
        '''
        return self.java_fsrb.getNetworkAddress()

    def reset(self):
        self.java_fsrb.reset()

    def setActivationMethod(self, value):
        '''
        Sets the value of the property activationMethod
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_fsrb.setActivationMethod(value)

    def setName(self, value):
        '''
        Sets the value of the property name
        :param value: allowed object is String
        '''
        assert type(value) == str
        self.java_fsrb.setName(value)

    def setNetworkAddress(self, value):
        '''
        Sets the value of the property NetworkAddress
        :param value: allowed object is String
        '''
        assert type(value) == str
        self.java_fsrb.setNetworkAddress(value)

    def __str__(self):
        '''
        Returns a String object representing this object
        :return: allowed object is String
        '''
        return self.java_fsrb.toString()