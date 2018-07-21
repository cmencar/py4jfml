from py4jfml.rulebase.RuleBaseType import *

gateway = JavaGateway()

class TsukamotoRuleBaseType(RuleBaseType):
    '''
    Python class for implementing Tsukamoto rule base fuzzy systems
    '''

    def __init__(self, name=None, ruleBaseType=None, activation=None, andAlgorithm=None, orAlgorithm=None):
        '''
        :param name: name of the rule base
        :param ruleBaseType: the ruleBaseSystemType
        :param activation: the method used for the implication process according to StandardActivationMethodType
        :param andAlgorithm: the and algorithm to be used
        :param orAlgorithm: the or algorithm to be used
        '''
        if name!=None and ruleBaseType==None and activation==None and andAlgorithm==None and orAlgorithm==None:
            assert type(name)==str
            self.java_fsrb = gateway.entry_point.getJFMLRulebase_Factory().createTsukamotoRuleBaseType(name)
        else:
            super().__init__(name, ruleBaseType, activation, andAlgorithm, orAlgorithm)