from py4j.java_gateway import JavaGateway

from py4jfml.rule import AnYaAntecedentType
from py4jfml.rule import ConsequentType
from py4jfml.rule import TskConsequentType

gateway = JavaGateway()

class AnYaRuleType:
    '''
    Python class for anYaRuleType complex type.
    '''

    def __int__(self, name=None, ant=None, con=None, weight=None):
        '''
        :param name: name of the AnYa Rule
        :param ant: the AnYa Antecedent AnYaAntecedentType
        :param con: the Consequent
        :param weight: the importance of the rule to be used by the inference engine
        '''
        if name==None and ant==None and con==None and weight==None:
            self.java_r = gateway.entry_point.getJFMLRule_Factory().createAnYaRuleType()
        elif name!=None and ant==None and con==None and weight==None:
            assert type(name)==str
            self.java_r = gateway.entry_point.getJFMLRule_Factory().createAnYaRuleType(name)
        elif name!=None and ant!=None and con!=None and weight==None:
            assert type(name)==str and type(ant)==AnYaAntecedentType
            assert type(con)==ConsequentType or type(con)==TskConsequentType
            if type(con)==ConsequentType:
                self.java_r = gateway.entry_point.getJFMLRule_Factory().createAnYaRuleType(name, ant.java_aat, con.java_ct)
            else:
                self.java_r = gateway.entry_point.getJFMLRule_Factory().createAnYaRuleType(name, ant.java_aat, con.java_tskct)
        elif name!=None and ant==None and con==None and weight!=None:
            assert type(name)==str and type(weight)==float
            self.java_r = gateway.entry_point.getJFMLRule_Factory().createAnYaRuleType(name, weight)


    # 5 methods from class Rule

    '''
    def andFunction(self, degrees, andMethod=None):
        #param andMethod: andMethod
        #return:
        assert type(degrees)==list
        if andMethod==None:
            return self.java_r.and(degrees)
        else:
            assert type(andMethod)==str
            return self.java_r.and(andMethod, degrees)
    '''

    def getEvaluation(self):
        '''
        Gets the evaluation
        :return: possible object is float
        '''
        return self.java_r.getEvaluation()

    '''
    def orFunction(self, degrees, orMethod=None):
        # param orMethod: orMethod
        # return:
        assert type(degrees) == list
        if orMethod == None:
            return self.java_r.or(degrees)
        else:
            assert type(orMethod) == str
            return self.java_r.or(orMethod, degrees)
    '''

    def reset(self):
        '''
        '''
        self.java_r.reset()

    def setEvaluation(self, evaluation):
        '''
        :param evaluation: allowed object is float
        '''
        assert type(evaluation)==float
        self.java_r.setEvaluation(evaluation)



    def aggregation(self, degrees):
        '''
        Performs the combination of the multiple clauses contained in the antecedent part of a rule by means two connectors, and or or
        :param degrees:
        :return: aggregation value
        '''
        assert type(degrees)==list
        return self.java_r.aggregation(degrees)

    def getAnYaAntecedent(self):
        '''
        Gets the value of the property anYaAntecedent
        :return: possible object is AnYaAntecedentType
        '''
        return self.java_r.getAnYaAntecedent()


    def getConsequent(self):
        '''
        Gets the value of the property consequent
        :return: possible object is ConsequentType
        '''
        return self.java_r.getConsequent()

    def getName(self):
        '''
        Gets the value of the property name
        :return: possible object is String
        '''
        return self.java_r.getName()

    def getNetworkAddress(self):
        '''
        Gets the value of the property networkAddress
        :return: possible object is String
        '''
        return self.java_r.getNetworkAddress()

    def getTskConsequent(self):
        '''
        Gets the value of the property tskConsequent
        :return: possible object is TskConsequentType
        '''
        return self.java_r.getTskConsequent()

    def getWeight(self):
        '''
        Gets the value of the property weight
        :return: possible object is float
        '''
        return self.java_r.getWeight()

    def setAnYaAntecedent(self, value):
        '''
        Sets the value of the property anYaAntecedent
        :param value: allowed object is AnYaAntecedentTypeì
        '''
        assert type(value)==AnYaAntecedentType
        self.java_r.setAnYaAntecedent(value.java_aat)

    def setConsequent(self, value):
        '''
        Sets the value of the property consequent
        :param value: allowed object is ConsequentType
        '''
        assert type(value)==ConsequentType
        self.java_r.setConsequent(value.java_ct)

    def setName(self, value):
        '''
        Sets the value of the property name
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_r.setName(value)

    def setNetworkAddress(self, value):
        '''
        Sets the value of the property networkAddress
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_r.setNetworkAddress(value)

    def setTskConsequent(self, value):
        '''
        Sets the value of the property tskConsequent
        :param value: allowed object is TskConsequentType
        '''
        assert type(value)==TskConsequentType
        self.java_r.setTskConsequent(value.tskct)

    def setWeight(self, value):
        '''
        Sets the value of the property weight
        :param value:  allowed object is float
        '''
        assert type(value)==float
        self.java_r.setWeight(value)

    def __str__(self):
        '''
        Returns a String object representing this object
        :return: possible object is String
        '''
        return self.java_r.toString()


