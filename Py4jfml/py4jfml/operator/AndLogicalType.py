from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
from py4jfml.operator.OrLogicalType import *

class AndLogicalType:
    '''
    Python class for andLogicalType complex type
    '''
    def __init__(self,term1,term2,tNorm):
        '''
        Constructor of class AndLogicalType
        :param term1: AndLogicalType or OrLogicalType or String with the name of term1
        :param term2: AndLogicalType or OrLogicalType or String with the name of term2
        :param tNorm: String with AND operator StandardAndMethodType
        '''

        #Calling java default constructor
        if term1==None and term2==None and tNorm==None:
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType()

        #Calling java And constructor using default t-norm = MIN
        if term1!=None and term2!=None and tNorm==None and type(term1)==AndLogicalType and type(term2)==AndLogicalType:
            assert type(term1)==AndLogicalType and type(term2)==AndLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(term1.java_lt,term2.java_lt)

        #Calling java And constructor using default t-norm = MIN
        if term1!=None and term2!=None and tNorm==None and type(term1)==AndLogicalType and type(term2)==OrLogicalType:
            assert type(term1)==AndLogicalType and type(term2)==OrLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(term1.java_lt,term2.java_lt)

        #Calling java And constructor using default t-norm = MIN
        if term1!=None and term2!=None and tNorm==None and type(term1)==OrLogicalType and type(term2)==AndLogicalType:
            assert type(term1)==OrLogicalType and type(term2)==AndLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(term1.java_lt,term2.java_lt)

        #Calling java And constructor using default t-norm = MIN
        if term1!=None and term2!=None and tNorm==None and type(term1)==OrLogicalType and type(term2)==OrLogicalType:
            assert type(term1)==OrLogicalType and type(term2)==OrLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(term1.java_lt,term2.java_lt)

        #Calling java And constructor using default t-norm = MIN
        if term1!=None and term2!=None and tNorm==None and type(term1)==str and type(term2)==AndLogicalType:
            assert type(term1)==str and type(term2)==AndLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(str(term1),term2.java_lt)

        #Calling java And constructor using default t-norm = MIN
        if term1!=None and term2!=None and tNorm==None and type(term1)==str and type(term2)==OrLogicalType:
            assert type(term1)==str and type(term2)==OrLogicalType
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(str(term1),term2.java_lt)

        #Calling java And constructor using default t-norm = MIN
        if term1!=None and term2!=None and tNorm==None and type(term1)==str and type(term2)==str:
            assert type(term1)==str and type(term2)==str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(str(term1),str(term2))

        #Calling java And constructor using t-norm as method for and operator
        if term1!=None and term2!=None and tNorm!=None and type(term1)==AndLogicalType and type(term2)==AndLogicalType and type(tNorm)==str:
            assert type(term1)==AndLogicalType and type(term2)==AndLogicalType and type(tNorm)==str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(term1.java_lt,term2.java_lt,str(tNorm))

        #Calling java And constructor using t-norm as method for and operator
        if term1!=None and term2!=None and tNorm!=None and type(term1)==AndLogicalType and type(term2)==OrLogicalType and type(tNorm)==str:
            assert type(term1)==AndLogicalType and type(term2)==OrLogicalType and type(tNorm)==str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(term1.java_lt,term2.java_lt,str(tNorm))

        #Calling java And constructor using t-norm as method for and operator
        if term1!=None and term2!=None and tNorm!=None and type(term1)==OrLogicalType and type(term2)==AndLogicalType and type(tNorm)==str:
            assert type(term1)==OrLogicalType and type(term2)==AndLogicalType and type(tNorm)==str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(term1.java_lt,term2.java_lt,str(tNorm))

        #Calling java And constructor using t-norm as method for and operator
        if term1!=None and term2!=None and tNorm!=None and type(term1)==OrLogicalType and type(term2)==OrLogicalType and type(tNorm)==str:
            assert type(term1)==OrLogicalType and type(term2)==OrLogicalType and type(tNorm)==str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(term1.java_lt,term2.java_lt,str(tNorm))

        #Calling java And constructor using t-norm as method for and operator
        if term1!=None and term2!=None and tNorm!=None and type(term1)==str and type(term2)==AndLogicalType and type(tNorm)==str:
            assert type(term1)==str and type(term2)==AndLogicalType and type(tNorm)==str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(str(term1),term2.java_lt,str(tNorm))

        #Calling java And constructor using t-norm as method for and operator
        if term1!=None and term2!=None and tNorm!=None and type(term1)==str and type(term2)==OrLogicalType and type(tNorm)==str:
            assert type(term1)==str and type(term2)==OrLogicalType and type(tNorm)==str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(str(term1),term2.java_lt,str(tNorm))

        #Calling java And constructor using t-norm as method for and operator
        if term1!=None and term2!=None and tNorm!=None and type(term1)==str and type(term2)==str and type(tNorm)==str:
            assert type(term1)==str and type(term2)==str and type(tNorm)==str
            self.java_lt = gateway.entry_point.getJFMLOperator_Factory().createAndLogicalType(str(term1),str(term2),str(tNorm))

    def operate(self,x,y):
        '''
        - MIN for implementing the operator and with the minimum as defined from Equation (A.14);
        - PROD for implementing the operator and with the product as defined from from Equation (A.15);
        - BDIF for implementing the operator and with bounded difference as defined from from Equation (A.16);
        - DRP for implementing the operator and with the drastic product as defined from from Equation (A.17);
        - EPROD for implementing the operator and with the Einstein product as defined from from Equation (A.18);
        - HPROD for implementing the operator and with the Hamacher product as defined from from Equation (A.19);
        - NILMIN for implementing the operator and with the Nilpotent minimum as defined from from Equation (A.20);
        - custom_\S* for a custom method for operator and.
        :param x: degree1
        :param y: degree2
        :return: The t-norm
        '''
        assert type(x)==float and type(y)==float
        return self.java_lt.operate(x,y)

    def setTNorm(self,value):
        '''
        Sets the value of the property tNorm
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_lt.setTNorm(value)

    ''' IMPLEMENTARE
    def getContent(self):
    '''

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

    def getTNorm(self):
        '''
        Gets the value of the property tNorm
        :return: possible object is String
        '''
        return self.java_lt.getTNorm()