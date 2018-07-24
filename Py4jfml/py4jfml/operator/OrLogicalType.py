from py4jfml.operator import AndLogicalType
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()


class OrLogicalType:
    '''
    Python class for orLogicalType complex type
    '''
    def __init__(self, term1, term2, tConorm):
        '''
        Constructor of class OrLogicalType
        :param term1: AndLogicalType or OrLogicalType or String with the name of term1
        :param term2: AndLogicalType or OrLogicalType or String with the name of term2
        :param tConorm: String with AND operator StandardAndMethodType
        '''

        #Calling java default constructor
        if term1==None and term2==None and tConorm==None:
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType()

        #Calling java Or constructor using default tConorm = MAX
        elif term1!=None and term2!=None and tConorm==None and type(term1)==AndLogicalType and type(term2)==AndLogicalType:
            assert type(term1)==AndLogicalType and type(term2)==AndLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(term1.java_lt,term2.java_lt)

        #Calling java Or constructor using default tConorm = MAX
        elif term1!=None and term2!=None and tConorm==None and type(term1)==AndLogicalType and type(term2)==OrLogicalType:
            assert type(term1)==AndLogicalType and type(term2)==OrLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(term1.java_lt,term2.java_lt)

        #Calling java Or constructor using default tConorm = MAX
        elif term1!=None and term2!=None and tConorm==None and type(term1)==OrLogicalType and type(term2)==AndLogicalType:
            assert type(term1)==OrLogicalType and type(term2)==AndLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(term1.java_lt,term2.java_lt)

        #Calling java Or constructor using default tConorm = MAX
        elif term1!=None and term2!=None and tConorm==None and type(term1)==OrLogicalType and type(term2)==OrLogicalType:
            assert type(term1)==OrLogicalType and type(term2)==OrLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(term1.java_lt,term2.java_lt)

        #Calling javaOr constructor using default tConorm = MAX
        elif term1!=None and term2!=None and tConorm==None and type(term1)==str and type(term2)==AndLogicalType:
            assert type(term1)==str and type(term2)==AndLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(str(term1),term2.java_lt)

        #Calling java Or constructor using default tConorm = MAX
        elif term1!=None and term2!=None and tConorm==None and type(term1)==str and type(term2)==OrLogicalType:
            assert type(term1)==str and type(term2)==OrLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(str(term1),term2.java_lt)

        #Calling java Or constructor using default tConorm = MAX
        elif term1!=None and term2!=None and tConorm==None and type(term1)==str and type(term2)==str:
            assert type(term1)==str and type(term2)==str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(str(term1),str(term2))

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and tConorm!=None and type(term1)==AndLogicalType and type(term2)==AndLogicalType and type(tConorm)==str:
            assert type(term1) == AndLogicalType and type(term2) == AndLogicalType and type(tConorm) == str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(term1.java_lt, term2.java_lt, str(tConorm))

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and tConorm!=None and type(term1)==AndLogicalType and type(term2)==OrLogicalType and type(tConorm)==str:
            assert type(term1) == AndLogicalType and type(term2) == OrLogicalType and type(tConorm) == str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(term1.java_lt, term2.java_lt, str(tConorm))

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and tConorm!=None and type(term1)==OrLogicalType and type(term2)==AndLogicalType and type(tConorm)==str:
            assert type(term1) == OrLogicalType and type(term2) == AndLogicalType and type(tConorm) == str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(term1.java_lt, term2.java_lt, str(tConorm))

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and tConorm!=None and type(term1)==OrLogicalType and type(term2)==OrLogicalType and type(tConorm)==str:
            assert type(term1) == OrLogicalType and type(term2) == OrLogicalType and type(tConorm) == str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(term1.java_lt, term2.java_lt, str(tConorm))

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and tConorm!=None and type(term1)==str and type(term2)==AndLogicalType and type(tConorm)==str:
            assert type(term1) == str and type(term2) == AndLogicalType and type(tConorm) == str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(str(term1), term2.java_lt, str(tConorm))

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and tConorm!=None and type(term1)==str and type(term2)==OrLogicalType and type(tConorm)==str:
            assert type(term1) == str and type(term2) == OrLogicalType and type(tConorm) == str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(str(term1), term2.java_lt, str(tConorm))

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and tConorm!=None and type(term1)==str and type(term2)==str and type(tConorm)==str:
            assert type(term1) == str and type(term2) == str and type(tConorm) == str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createOrLogicalType(str(term1), str(term2), str(tConorm))

    def operate(self,x,y):
        '''
        Gets the aggregation depending on the operator AND / OR
        - MAX for implementing the connector or with the maximum as defined from Equation (A.21);
        - PROBOR for implementing the connector or with the probabilistic sum as defined from Equation (A.22);
        - BSUM for implementing the operator or with the bounded sum as defined from Equation (A.23);
        - DRS for implementing the operator or with the drastic sum as defined from Equation (A.24);
        - ESUM for implementing the operator or with the Einstein sum as defined from Equation (A.25);
        - HSUM for implementing the operator or with the Hamacher sum as defined from Equation (A.26);
        - NILMAX for implementing the operator or with the Nilpotent maximum as defined from Equation (A.27);
        - custom_\S* for a custom method for implementing the connector or.
        :param x: value1
        :param y: value2
        :return: result of orMethod
        '''
        assert type(x)==float and type(y)==float
        return self.java_lt.operate(x,y)

    def setTConorm(self,value):
        '''
        Sets the value of the property tConorm
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_lt.setTConorm(str(value))

    def getContent(self):
        '''
        Objects of the following type(s) are allowed in the list JAXBElement<OrLogicalType> JAXBElement<CircularTermType> JAXBElement<AndLogicalType>
        :return: allowed object is a list of JAXBElement
        '''
        return self.java_lt.getContent()

    def getContent(self,i):
        '''
        Gets the i-th element of the Aggregation Both the element AND and the element OR contain two elements,
        clause or an element AND followed by an element clause or an element OR followed by an element clause.
        The element clause represents the clause to be used in the fuzzy expression of the aggregated fuzzy term under definition.
        :param i: 0=first element, 1=last element
        :return: the content of the i-th part i of the Aggregation
        '''
        assert type(i)==int
        return self.java_lt.getContent(int(i))

    def getOperator(self):
        '''
        Get the method for operator AND / OR
        :return: possible object is String
        '''
        return self.java_lt.getOperator()

    def getTConorm(self):
        '''
        Gets the value of the property tConorm
        :return: possible object is String
        '''
        return self.java_lt.getTConorm()
