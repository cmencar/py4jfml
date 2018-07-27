from py4j.java_collections import ListConverter
from py4j.java_gateway import JavaGateway
from py4jfml.rule.AntecedentType import AntecedentType
from py4jfml.rule.TskConsequentType import TskConsequentType

gateway = JavaGateway()


class TskFuzzyRuleType:
    '''
    Python class for tskFuzzyRuleType complex type
    '''

    def __init__(self, name=None, ant=None, con=None, connector=None, connectorMethod=None, andMethod=None, orMethod=None, weight=None):
        '''
        :param name: name of the TSK Fuzzy Rule
        :param ant: the Antecedent AntecedentType
        :param con: the Consequent TskConsequentType
        :param connector: the connector used to define the logical operator aimed at connecting the different clauses in antecedent part (and/or)
        :param connectorMethod: the and algorithm to be used if the chosen connector is and or the or algorithm to be used if the chosen connector is or
        :param andMethod:the attribute andMethod is used to define the and algorithm to be used if the chosen connector is and
        :param orMethod: the attribute orMethod is used to define the or algorithm to be used if the chosen connector is or
        :param weight: the attribute weight is used to define the importance of the rule to be used by the inference engine
        '''
        if name==None and ant==None and con==None and connector==None and connectorMethod==None and andMethod==None and orMethod==None and weight==None:
            self.java_r = gateway.entry_point.getJFMLRule_Factory().createTskFuzzyRuleType()
        elif name!=None and ant==None and con==None and connector==None and connectorMethod==None and andMethod==None and orMethod==None and weight==None:
            assert type(name)==str
            self.java_r = gateway.entry_point.getJFMLRule_Factory().createTskFuzzyRuleType(name)
        elif name!=None and ant!=None and con!=None and connector==None and connectorMethod==None and andMethod==None and orMethod==None and weight==None:
            assert type(name)==str and type(ant)==AntecedentType and type(con)==TskConsequentType
            self.java_r = gateway.entry_point.getJFMLRule_Factory().createTskFuzzyRuleType(name, ant.java_at, con.java_tskct)
        elif name!=None and ant==None and con==None and connector==None and connectorMethod==None and andMethod==None and orMethod==None and weight!=None:
            assert type(name)==str and type(weight)==float
            self.java_r = gateway.entry_point.getJFMLRule_Factory().createTskFuzzyRuleType(name, weight)
        elif name!=None and ant==None and con==None and connector!=None and connectorMethod!=None and andMethod==None and orMethod==None and weight!=None:
            assert type(name)==str and type(weight)==float and type(connector)==str and type(connectorMethod)==str
            self.java_r = gateway.entry_point.getJFMLRule_Factory().createTskFuzzyRuleType(name, connector, connectorMethod, weight)
        elif name!=None and ant==None and con==None and connector!=None and connectorMethod==None and andMethod!=None and orMethod!=None and weight!=None:
            assert type(name)==str and type(weight)==float and type(connector)==str and type(andMethod)==str and type(orMethod)==str
            self.java_r = gateway.entry_point.getJFMLRule_Factory().createTskFuzzyRuleType(name, connector, andMethod, orMethod, weight)


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

    def getAndMethod(self):
        '''
        Gets the value of the property andMethod
        :return: possible object is String
        '''
        return self.java_r.getAndMethod()

    def getAntecedent(self):
        '''
        Gets the value of the property antecedent
        :return: possible object is AntecedentType
        '''
        return self.java_r.getAntecedent()

    def getConnector(self):
        '''
        Gets the value of the property connector
        :return: possible object is string
        '''
        return self.java_r.getConnector()

    def getName(self):
        '''
        Gets the value of the property name
        :return: possible object is string
        '''
        return self.java_r.getName()

    def getNetworkAddress(self):
        '''
        Gets the value of the property networkAddress
        :return: possible object is string
        '''
        return self.java_r.getNetworkAddress()

    def getOrMethod(self):
        '''
        Gets the value of the property orMethod
        :return: possible object is string
        '''
        return self.java_r.getOrMethod()

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

    def isAndMethodDefined(self):
        '''
        Return true if the And method is defined; false otherwise
        :return: true if the And method is defined; false otherwise
        '''
        return self.java_r.isAndMethodDefined()

    def isOrMethodDefined(self):
        '''
        Return true if the Or method is defined; false otherwise
        :return: true if the Or method is defined; false otherwise
        '''
        return self.java_r.isOrMethodDefined()

    def setAndMethod(self, value):
        '''
        Sets the value of the property andMethod
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_r.setAndMethod(value)

    def setAntecedent(self, value):
        '''
        Sets the value of the property antecedent
        :param value: allowed object is AntecedentType
        '''
        assert type(value)==AntecedentType
        self.java_r.setAntecedent(value.java_at)

    def setConnector(self, value):
        '''
        Sets the value of the property connector
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_r.	setConnector(value)

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

    def setOrMethod(self, value):
        '''
        Sets the value of the property orMethod
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_r.setOrMethod(value)

    def setTskConsequent(self, value):
        '''
        Sets the value of the property tskConsequent
        :param value: allowed object is TskConsequentType
        '''
        assert type(value)==TskConsequentType
        self.java_r.setTskConsequent(value.java_tskct)

    def setWeight(self, value):
        '''
        Sets the value of the property weight
        :param value: allowed object is float
        '''
        assert type(value)==float
        self.java_r.setWeight(value)

    def __str__(self):
        '''
        Returns a String object representing this object
        :return: possible object is String
        '''
        return self.java_r.toString()









