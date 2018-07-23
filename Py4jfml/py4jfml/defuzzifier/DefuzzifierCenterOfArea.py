from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class DefuzzifierCenterOfArea:

    def __init__(self, domainLeft, domainRight, terms):
        '''
        :param domainLeft:
        :param domainRight:
        :param terms:
        '''
        assert type(domainLeft)==float and type(domainRight)==float and type(terms)==list
        self.java_d = gateway.entry_point.getJFMLDefuzzifier_Factory().createDefuzzifierCenterOfArea(domainLeft, domainRight, terms)


    # 2 Methods from Java abstract class Defuzzifier

    def getName(self):
        '''
        Gets the defuzzifier name
        :return: possible object is string
        '''
        return self.java_d.getName()

    def __str__(self):
        '''
        Returns a String object representing this object
        :return: a string
        '''
        return self.java_d.toString()


    # 16 Methods from Java abstract class DefuzzifierContinuous

    def getArea(self):
        '''
        Gets the area
        :return: possible object is float
        '''
        return self.java_d.getArea()

    def getLength(self):
        '''
        Gets the length
        :return: possible object is int
        '''
        return self.java_d.getLength()

    def getMax(self):
        '''
        Gets the max
        :return: possible object is float
        '''
        return self.java_d.getMax()

    def getMin(self):
        '''
        Gets the min
        :return: possible object is float
        '''
        return self.java_d.getMin()

    def getStepSize(self):
        '''
        Gets the step size
        :return: possible object is float
        '''
        return self.java_d.getStepSize()

    def getValueY(self, x):
        '''
        Gets the min
        :param x: the value of x
        :return: possible object is float
        '''
        assert type(x)==float
        return self.java_d.getValueY()

    def isDiscrete(self):
        '''
        Gets if the defuzzifier is continuous or discrete
        :return: true if the defuzzifier is discrete or false otherwise
        '''
        return self.java_d.isDiscrete()

    def iterator(self):
        '''
        Get an iterator
        :return: an iterator
        '''
        return self.java_d.iterator()

    def reset(self):
        '''
        Reset values
        '''
        self.java_d.reset()

    def setDiscrete(self, discrete):
        '''
        Sets if the defuzzifier is continuous or discrete
        :param discrete: allowed object is boolean
        '''
        assert type(discrete)==bool
        self.java_d.setDiscrete(discrete)

    def setMax(self, max):
        '''
        Sets the max
        :param max: allowed object is float
        '''
        assert type(max)==float
        self.java_d.setMax(max)

    def setMin(self, min):
        '''
        Sets the min
        :param min: allowed object is float
        '''
        assert type(min) == float
        self.java_d.setMin(min)

    def setPoint(self, x, y):
        '''
        Set a point
        :param x: the value x
        :param y: the value y
        '''
        assert type(x)==float and type(y)==float
        self.java_d.setPoint(x, y)

    def setStepSize(self, stepsize):
        '''
        Sets the stepsize
        :param stepsize: allowed object is float
        '''
        assert type(stepsize) == float
        self.java_d.setStepSize(stepsize)

    def setValue(self, valuex, valuey):
        '''
        Set a point
        :param valuex: the value x
        :param valuey: the value y
        '''
        assert type(valuex)==float and type(valuey)==float
        self.java_d.setValue(valuex, valuey)

    def size(self):
        '''
        How many points are there in this defuzzifier
        :return: possible object is int
        '''
        return self.java_d.size()



    def defuzzify(self):
        '''
        Method to defuzzify
        :return: possible object is float or NaN if no rule inferred this variable
        '''
        return self.java_d.defuzzify()


