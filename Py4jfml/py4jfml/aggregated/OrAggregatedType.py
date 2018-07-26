from py4j.java_gateway import JavaGateway
from py4jfml.aggregated import AndAggregatedType as aat
from py4jfml.rule.ClauseType import ClauseType

gateway = JavaGateway()

class OrAggregatedType:
    '''
    Python class for OrAggregatedType complex type
    '''
    def __init__(self,term1=None,term2=None,c1=None,c2=None,tConorm=None):
        '''
        Constructor of class AndAggregatedType
        :param term1: AndAggregatedType or OrAggregatedType with the name of term1
        :param term2: AndAggregatedType or OrAggregatedType with the name of term2
        :param c1: ClauseType
        :param c2: ClauseType
        :param tConorm: String with OR operator StandardOrMethodType
        '''

        #Calling java default constructor
        if term1==None and term2==None and c1==None and c2==None and tConorm==None:
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType()

        #Calling java Or constructor using default tConorm = MAX
        elif term1!=None and term2!=None and c1==None and c2==None and tConorm==None:
            assert type(term1)==aat.AndAggregatedType and type(term2)==aat.AndAggregatedType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term1.java_at,term2.java_at)

        #Calling java Or constructor using default tConorm = MAX
        elif term1!=None and term2!=None and c1==None and c2==None and tConorm==None:
            assert type(term1)==aat.AndAggregatedType and type(term2)==OrAggregatedType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term1.java_at,term2.java_at)

        #Calling java Or constructor using default tConorm = MAX
        elif term1!=None and term2!=None and c1==None and c2==None and tConorm==None:
            assert type(term1)==OrAggregatedType and type(term2)==aat.AndAggregatedType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term1.java_at,term2.java_at)

        #Calling java Or constructor using default tConorm = MAX
        elif term1!=None and term2!=None and c1==None and c2==None and tConorm==None:
            assert type(term1)==OrAggregatedType and type(term2)==OrAggregatedType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term1.java_at,term2.java_at)

        #Calling java Or constructor using default tConorm = MAX
        elif term1==None and term2!=None and c1!=None and c2==None and tConorm==None:
            assert type(term2)==aat.AndAggregatedType and type(c1)==ClauseType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term2.java_at,c1.java_ct)

        #Calling java Or constructor using default tConorm = MAX
        elif term1==None and term2!=None and c1!=None and c2==None and tConorm==None:
            assert type(term2)==OrAggregatedType and type(c1)==ClauseType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term2.java_at,c1.java_ct)

        #Calling java Or constructor using default tConorm = MAX
        elif term1==None and term2==None and c1!=None and c2!=None and tConorm==None:
            assert type(c1) == ClauseType and type(c2) == ClauseType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(c1.java_ct,c2.java_ct)

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and c1==None and c2==None and tConorm!=None:
            assert type(term1)==aat.AndAggregatedType and type(term2)==aat.AndAggregatedType and type(tConorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tConorm,term1.java_at,term2.java_at)

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and c1==None and c2==None and tConorm!=None:
            assert type(term1)==aat.AndAggregatedType and type(term2)==OrAggregatedType and type(tConorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tConorm,term1.java_at,term2.java_at)

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and c1==None and c2==None and tConorm!=None:
            assert type(term1)==OrAggregatedType and type(term2)==aat.AndAggregatedType and type(tConorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tConorm,term1.java_at,term2.java_at)

        #Calling java Or constructor using tConorm as method for or operator
        elif term1!=None and term2!=None and c1==None and c2==None and tConorm!=None:
            assert type(term1)==OrAggregatedType and type(term2)==OrAggregatedType and type(tConorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tConorm,term1.java_at,term2.java_at)

        #Calling java Or constructor using tConorm as method for or operator
        elif term1==None and term2!=None and c1!=None and c2==None and tConorm!=None:
            assert type(term2)==aat.AndAggregatedType and type(c1)==ClauseType and type(tConorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tConorm,c1.java_ct,term2.java_at)

        #Calling java Or constructor using tConorm as method for or operator
        elif term1==None and term2!=None and c1!=None and c2==None and tConorm!=None:
            assert type(term2)==OrAggregatedType and type(c1)==ClauseType and type(tConorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tConorm,c1.java_ct,term2.java_at)

        #Calling java Or constructor using tConorm as method for or operator
        elif term1==None and term2==None and c1!=None and c2!=None and tConorm!=None:
            assert type(c1)==ClauseType and type(c2)==ClauseType and type(tConorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tConorm,c1.java_ct,c2.java_ct)

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
        return self.java_at.operate(x,y)

    def setTConorm(self,value):
        '''
        Sets the value of the property tConorm
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_at.setTConorm(value)

    def getContent(self):
        '''
        Objects of the following type(s) are allowed in the list JAXBElement<ClauseType> JAXBElement<AndAggregatedType> JAXBElement<OrAggregatedType>
        :return: allowed object is a list of JAXBElement
        '''
        return self.java_at.getContent()

    def getContent(self,i):
        '''
        Gets the i-th element of the Aggregation Both the element AND and the element OR contain two elements,
        clause or an element AND followed by an element clause or an element OR followed by an element clause.
        The element clause represents the clause to be used in the fuzzy expression of the aggregated fuzzy term under definition.
        :param i: 0=first element, 1=last element
        :return: the content of the i-th part i of the Aggregation
        '''
        assert type(i)==int
        return self.java_at.getContent(i)

    def getOperator(self):
        '''
        Get the method for operator AND / OR
        :return: the method for operator AND / OR
        '''
        return self.java_at.getOperator()

    def getTConorm(self):
        '''
        Gets the value of the property tConorm
        :return: possible object is String
        '''
        return self.java_at.getTConorm()