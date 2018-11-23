from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class CustomShapeType:
    '''
    Python class for customShapeType complex type
    '''
    def __init__(self):
        '''
        Constructor of class FuzzyTermType CustomShapeType
        '''
        self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createCustomShapeType()

    def copy(self):
        '''
        Creates a copy of the custom shape
        :return: possible object is PointSetShapeType
        '''
        return self.java_mf.copy()

    def setName(self,value):
        '''
        Sets the value of the property name
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_mf.setName(str(value))

    def getName(self):
        '''
        Gets the value of the property name
        :return: possible object is String
        '''
        return self.java_mf.getName()

    def getParameter(self):
        '''
        Gets the value of the parameter property
        :return: Objects of the following type(s) are allowed in the list ParameterType
        '''
        return self.java_mf.getParameter()