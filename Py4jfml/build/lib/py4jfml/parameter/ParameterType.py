from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class ParameterType:
    '''
    Python class for parameterType complex type
    '''
    def __init__(self):
        '''
        Constructor of class ParameterType
        '''
        self.java_p = gateway.entry_point.getJFMLParameter_Factory().createParameterType()

    def setValue(self,value):
        '''
        Sets the value of the property value
        :param value: allowed object is String
        '''
        assert type(value)==str
        self.java_p.setValue(str(value))

    def getValue(self):
        '''
        Gets the value of the property value
        :return: possible object is String
        '''
        return self.java_p.getValue()