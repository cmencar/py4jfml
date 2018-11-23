from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

class PointType:
    '''
    Python class for pointType complex type
    '''
    def __init__(self,x=None,y=None):
        '''
        Constructor of class PointType
        :param x: parameter x
        :param y: parameter y
        '''

        #Calling java default constructor
        if x==None and y==None:
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createPointType()

        #Call of the java constructor with the two parameters x and y
        elif x!=None and y!=None:
            assert type(x)==float and type(y)==float
            self.java_mf = gateway.entry_point.getJFMLMembershipfunction_Factory().createPointType(x,y)

    def compare(self,o1,o2):
        '''
        Compares its two arguments for order. Returns a negative integer, zero, or a positive integer as the first argument is less than, equal to, or greater than the second
        :param o1: the first PointType to be compared
        :param o2: the second PointType to be compared
        :return: a negative integer, zero, or a positive integer as the first argument is less than, equal to, or greater than the second
        '''
        assert type(o1)==PointType and type(o2)==PointType
        return self.java_mf.compare(o1.java_mf,o2.java_mf)

    def setX(self,value):
        '''
        Sets the value of the property x
        :param value: float value
        '''
        assert type(value)==float
        self.java_mf.setX(value)

    def setY(self,value):
        '''
        Sets the value of the property y
        :param value: float value
        '''
        assert type(value)==float
        self.java_mf.setY(value)

    def getX(self):
        '''
        Gets the value of the property x
        :return: float value
        '''
        return self.java_mf.getX()

    def getY(self):
        '''
        Gets the value of the property y
        :return: float value
        '''
        return self.java_mf.getY()

    def __str__(self):
        '''
        Gets the object as a string
        :return: possible object is string
        '''
        return self.java_mf.toString()