from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class OneParamType:
    '''
    Python class for the oneParamType complex type
    '''
    def __init__(self):
        '''
        Constructor of class OneParamType
        '''
        self.java_p = gateway.entry_point.getJFMLParameter_Factory().createOneParamType()

    def setParam1(self,value):
        '''
        Sets the value for the attribute param1
        :param value: float value
        '''
        assert type(value)==float
        self.java_psetParam1(float(value))

    def getParam1(self):
        '''
        Gets the value of the attribute param1
        :return: the value of the attribute param1
        '''
        return self.java_p.getParam1()

    def getParameterLength(self):
        '''
        Return the number of parameters
        :return: the number of parameters
        '''
        return self.java_p.getParameterLength()

    def getParameter(self,i):
        '''
        return the i-th parameter.
        :param i: i - the i-th parameter. Starts with 1. Parameter 1 --> i=1
        :return: the value of the i-th parameter. If i is not in the range, returns -1
        '''
        assert type(i)==int
        return self.java_p.getParameter(int(i))