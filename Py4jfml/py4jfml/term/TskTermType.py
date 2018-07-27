from py4j.java_gateway import JavaGateway
from py4j.java_collections import ListConverter

gateway = JavaGateway()

class TskTermType:
    '''
    Python class for tskTermType complex type
    '''
    def __init__(self,name=None,order=None,coeff=None):
        '''
        Constructor of class TskTermType
        :param name: the name of the TSK term
        :param order: the order of the TSK term (0 or 1)
        :param coeff: a list of coefficients (c, a, b, ...) : z = c + av1 + bv2 + ... mvn
        '''

        #Calling java default constructor
        if name==None and order==None and coeff==None:
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createTskTermType()

        #Call of the java constructor using the name, the order and a list of coefficients (c, a, b, ...)
        elif name!=None and order!=None and coeff!=None:
            assert type(name)==None and type(order)==int and type(coeff)==list
            java_coeff_list = ListConverter().convert(coeff, gateway._gateway_client)
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createTskTermType(name,order,java_coeff_list)

    def copy(self):
        '''
        Creates a copy of the term
        :return: a copy of the term
        '''
        return self.java_t.copy()

    def evaluateTskTerm(self,listVar):
        '''
        Evalutates the TSKterm considering the list of variables of the KnowledgeBase
        :param listVar: list of variables of the KnowledgeBase
        '''
        assert type(listVar)==list
        java_listVar = ListConverter().convert(listVar, gateway._gateway_client)
        self.java_t.evaluateTskTerm(java_listVar)

    def setName(self,value):
        '''
        Sets the value of the property name
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_t.setName(str(value))

    def setOrder(self,value):
        '''
        Sets the value of the property order
        :param value: value is an int
        '''
        assert type(value)==int
        self.java_t.setOrder(int(value))

    def getMembershipValue(self,x):
        '''
        Gets the membership degree by calculating the membership value of the parameter x to this term
        :param x: float value x
        :return: the membership value of the parameter x to this term
        '''
        assert type(x)==float
        return self.java_t.getMembershipValue(float(x))

    def getName(self):
        '''
        Gets the value of the property name
        :return: possible object is String
        '''
        return self.java_t.getName()

    def getOrder(self):
        '''
        Gets the value of the property order
        :return: int value
        '''
        return self.java_t.getOrder()

    def getTskValue(self):
        '''
        Gets the value of the tskValue property
        :return: Objects of the following type(s) are allowed in the list Float
        '''
        return self.java_t.getTskValue()

    def __str__(self):
        '''
        Gets the object as a string
        :return: possible object is string
        '''
        return self.java_t.toString()

    #Methods inherited from abstract class jfml.term.TskTerm

    def setEvaluation(self,z):
        '''
        Sets the evaluation value
        :param z: float value z
        '''
        assert type(z)==float
        self.java_t.setEvaluation(float(z))

    def getEvaluation(self):
        '''
        Gets the evaluation value
        :return: the evaluation float value
        '''
        return self.java_t.getEvaluation()

    def reset(self):
        '''
        Reset the evaluation value
        '''
        self.java_t.reset()