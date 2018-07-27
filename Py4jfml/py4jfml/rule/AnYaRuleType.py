from py4j.java_gateway import JavaGateway
from py4jfml.rule import AnYaAntecedentType as aat
from py4jfml.rule import ConsequentType as ct
from py4jfml.rule import TskConsequentType as tskct

gateway = JavaGateway()

class AnYaRuleType:
    '''
    Python class for anYaRuleType complex type.
    '''

    def __init__(self, name=None, ant=None, con=None, weight=None):
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
            assert type(name)==str and type(ant)==aat.AnYaAntecedentType
            assert type(con)==ct.ConsequentType or type(con)==tskct.TskConsequentType
            if type(con)==ct.ConsequentType:
                self.java_r = gateway.entry_point.getJFMLRule_Factory().createAnYaRuleType(name, ant.java_aat, con.java_ct)
            else:
                self.java_r = gateway.entry_point.getJFMLRule_Factory().createAnYaRuleType(name, ant.java_aat, con.java_tskct)
        elif name!=None and ant==None and con==None and weight!=None:
            assert type(name)==str and type(weight)==float
            self.java_r = gateway.entry_point.getJFMLRule_Factory().createAnYaRuleType(name, weight)


    # 5 methods from class Rule

    def andFunction(self, degrees, andMethod=None):
        '''
        :param degrees: array of degrees
        :param andMethod: and method
         MIN for implementing the operator and with the minimum as defined from Equation (A.14);
         PROD for implementing the operator and with the product as defined from Equation (A.15);
         BDIF for implementing the operator and with bounded difference as defined from Equation (A.16);
         DRP for implementing the operator and with the drastic product as defined from Equation (A.17);
         EPROD for implementing the operator and with the Einstein product as defined from Equation (A.18);
         HPROD for implementing the operator and with the Hamacher product as defined from Equation (A.19);
         NILMIN for implementing the operator and with the Nilpotent minimum as defined from Equation (A.20);
         custom_\S* for a custom method for operator and.
        :return: if andMethod is None returns the and algorithm by default: MIN
        '''
        assert type(degrees)==list
        javaarray_degrees = gateway.new_array(gateway.jvm.float, len(degrees))
        for d in degrees:
            javaarray_degrees[degrees.index(d)] = d
        if andMethod==None:
            return self.java_r.andFunction(javaarray_degrees)
        else:
            assert type(andMethod)==str
            return self.java_r.andFunction(andMethod, javaarray_degrees)

    def getEvaluation(self):
        '''
        Gets the evaluation
        :return: possible object is float
        '''
        return self.java_r.getEvaluation()

    def orFunction(self, degrees, orMethod=None):
        '''
        :param degrees:
        :param orMethod: or method
            MAX for implementing the connector or with the maximum as defined from Equation (A.21);
            PROBOR for implementing the connector or with the probabilistic sum as defined from Equation (A.22);
            BSUM for implementing the operator or with the bounded sum as defined from Equation (A.23);
            DRS for implementing the operator or with the drastic sum as defined from Equation (A.24);
            ESUM for implementing the operator or with the Einstein sum as defined from Equation (A.25);
            HSUM for implementing the operator or with the Hamacher sum as defined from Equation (A.26);
            NILMAX for implementing the operator or with the Nilpotent maximum as defined from Equation (A.27);
            custom_\S* for a custom method for implementing the connector or.
        :return: if orMethod is None, returns the or algorithm by default: MAX
        '''
        assert type(degrees)==list
        javaarray_degrees = gateway.new_array(gateway.jvm.float, len(degrees))
        for d in degrees:
            javaarray_degrees[degrees.index(d)] = d
        if orMethod == None:
            return self.java_r.orFunction(javaarray_degrees)
        else:
            assert type(orMethod) == str
            return self.java_r.orFunction(orMethod, javaarray_degrees)

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
        javaarray_degrees = gateway.new_array(gateway.jvm.float, len(degrees))
        for d in degrees:
            javaarray_degrees[degrees.index(d)] = d
        return self.java_r.aggregation(javaarray_degrees)

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
        assert type(value)==aat.AnYaAntecedentType
        self.java_r.setAnYaAntecedent(value.java_aat)

    def setConsequent(self, value):
        '''
        Sets the value of the property consequent
        :param value: allowed object is ConsequentType
        '''
        assert type(value)==ct.ConsequentType
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
        assert type(value)==tskct.TskConsequentType
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


