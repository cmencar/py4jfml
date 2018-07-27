from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class CircularTermType:
    '''
    Python class for circularTermType complex type
    '''
    def __init__(self,name=None):
        '''
        Constructor of class FuzzyTermType
        :param name: the name of the circular term
        '''

        #Calling java default constructor
        if name==None:
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createCircularTermType()

        #Call of the java constructor using the name
        elif name!=None:
            assert type(name)==str
            self.java_t = gateway.entry_point.getJFMLTerm_Factory().createCircularTermType(name)

    def setComplement(self,value):
        '''
        Sets the value of the property complement
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_t.setComplement(str(value))

    def getComplement(self):
        '''
        Gets the value of the property complement
        :return: possible object is String
        '''
        return self.java_t.getComplement()

    def getValue(self):
        '''
        Gets the value of the property value
        :return: possible object is String
        '''
        return self.java_t.getValue()