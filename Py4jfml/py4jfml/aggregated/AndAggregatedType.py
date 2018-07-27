from py4j.java_gateway import JavaGateway
from py4jfml.aggregated import OrAggregatedType as oat
from py4jfml.rule import ClauseType as ct

gateway = JavaGateway()

class AndAggregatedType:
    '''
    Python class for andAggregatedType complex type
    '''
    def __init__(self,term1=None,term2=None,c1=None,c2=None,tNorm=None):
        '''
        Constructor of class AndAggregatedType
        :param term1: AndAggregatedType or OrAggregatedType with the name of term1
        :param term2: AndAggregatedType or OrAggregatedType with the name of term2
        :param c1: ClauseType
        :param c2: ClauseType
        :param tNorm: String with AND operator StandardAndMethodType
        '''

        #Calling java default constructor
        if term1==None and term2==None and c1==None and c2==None and tNorm==None:
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType()

        #Calling java And constructor using default t-norm = MIN
        elif term1!=None and term2!=None and c1==None and c2==None and tNorm==None:
            assert type(term1)==AndAggregatedType and type(term2)==AndAggregatedType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term1.java_at,term2.java_at)

        #Calling java And constructor using default t-norm = MIN
        elif term1!=None and term2!=None and c1==None and c2==None and tNorm==None:
            assert type(term1)==AndAggregatedType and type(term2)==oat.OrAggregatedType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term1.java_at,term2.java_at)

        #Calling java And constructor using default t-norm = MIN
        elif term1!=None and term2!=None and c1==None and c2==None and tNorm==None:
            assert type(term1)==oat.OrAggregatedType and type(term2)==AndAggregatedType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term1.java_at,term2.java_at)

        #Calling java And constructor using default t-norm = MIN
        elif term1!=None and term2!=None and c1==None and c2==None and tNorm==None:
            assert type(term1)==oat.OrAggregatedType and type(term2)==oat.OrAggregatedType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term1.java_at,term2.java_at)

        #Calling java And constructor using default t-norm = MIN
        elif term1==None and term2!=None and c1!=None and c2==None and tNorm==None:
            assert type(term2)==AndAggregatedType and type(c1)==ct.ClauseType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term2.java_at,c1.java_ct)

        #Calling java And constructor using default t-norm = MIN
        elif term1==None and term2!=None and c1!=None and c2==None and tNorm==None:
            assert type(term2)==oat.OrAggregatedType and type(c1)==ct.ClauseType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(term2.java_at,c1.java_ct)

        #Calling java And constructor using default t-norm = MIN
        elif term1==None and term2==None and c1!=None and c2!=None and tNorm==None:
            assert type(c1)==ct.ClauseType and type(c2)==ct.ClauseType
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(c1.java_ct,c2.java_ct)

        #Calling java  And constructor using t-norm as method for and operator
        elif term1!=None and term2!=None and c1==None and c2==None and tNorm!=None:
            assert type(term1)==AndAggregatedType and type(term2)==AndAggregatedType and type(tNorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tNorm,term1.java_at,term2.java_at)

        #Calling java  And constructor using t-norm as method for and operator
        elif term1!=None and term2!=None and c1==None and c2==None and tNorm!=None:
            assert type(term1)==AndAggregatedType and type(term2)==oat.OrAggregatedType and type(tNorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tNorm,term1.java_at,term2.java_at)

        #Calling java  And constructor using t-norm as method for and operator
        elif term1!=None and term2!=None and c1==None and c2==None and tNorm!=None:
            assert type(term1)==oat.OrAggregatedType and type(term2)==AndAggregatedType and type(tNorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tNorm,term1.java_at,term2.java_at)

        #Calling java  And constructor using t-norm as method for and operator
        elif term1!=None and term2!=None and c1==None and c2==None and tNorm!=None:
            assert type(term1)==oat.OrAggregatedType and type(term2)==oat.OrAggregatedType and type(tNorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tNorm,term1.java_at,term2.java_at)

        #Calling java  And constructor using t-norm as method for and operator
        elif term1==None and term2!=None and c1!=None and c2==None and tNorm!=None:
            assert type(term2)==AndAggregatedType and type(c1)==ct.ClauseType and type(tNorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tNorm,c1.java_ct,term2.java_at)

        #Calling java  And constructor using t-norm as method for and operator
        elif term1==None and term2!=None and c1!=None and c2==None and tNorm!=None:
            assert type(term2)==oat.OrAggregatedType and type(c1)==ct.ClauseType and type(tNorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tNorm,c1.java_ct,term2.java_at)

        #Calling java  And constructor using t-norm as method for and operator
        elif term1==None and term2==None and c1!=None and c2!=None and tNorm!=None:
            assert type(c1)==ct.ClauseType and type(c2)==ct.ClauseType and type(tNorm)==str
            self.java_at = gateway.entry_point.getJFMLAggregated_Factory().createAndAggregatedType(tNorm,c1.java_ct,c2.java_ct)

    def operate(self,degree1,degree2):
        '''
        Gets the aggregation depending on the operator AND / OR
        :param degree1: the degree1
        :param degree2: the degree2
        :return: the aggregation result
        '''
        assert type(degree1)==float and type(degree2)==float
        return self.java_at.operate(degree1,degree2)

    def setTNorm(self,value):
        '''
        Sets the value of the property tNorm.
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_at.setTNorm(str(value))

    def getContent(self,i=None):
        '''
        Objects of the following type(s) are allowed in the list JAXBElement<OrAggregatedType> JAXBElement<ClauseType> JAXBElement<AndAggregatedType>
        Or gets the i-th element of the Aggregation Both the element AND and the element OR contain two elements,
        clause or an element AND followed by an element clause or an element OR followed by an element clause.
        The element clause represents the clause to be used in the fuzzy expression of the aggregated fuzzy term under definition
        :param i: 0=first element, 1=last element
        :return: allowed object is a list of JAXBElement or the content of the i-th part i of the Aggregation
        '''
        if i==None:
            return self.java_at.getContent()
        elif i!=None:
            assert type(i) == int
            return self.java_at.getContent(i)

    def getOperator(self):
        '''
        Get the method for operator AND / OR
        :return: the method for operator AND / OR
        '''
        return self.java_at.getOperator()

    def getTNorm(self):
        '''
        Gets the value of the property tNorm
        :return: possible object is String
        '''
        return self.java_at.getTNorm()