from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class DefuzzifierCenterOfGravitySingletons:

    def __init__(self, leftDomain, rightDomain):
        '''
        :param leftDomain:
        :param rightDomain:
        '''
        assert type(leftDomain)==float and type(rightDomain)==float
        self.java_d = gateway.entry_point.getJFMLDefuzzifier_Factory().createDefuzzifierCenterOfGravitySingletons(leftDomain, rightDomain)


    # 4 Methods from Java abstract class Defuzzifier

    def getName(self):
        '''
        Gets the defuzzifier name
        :return: possible object is string
        '''
        return self.java_d.getName()

    def isDiscrete(self):
        '''
        Gets if the defuzzifier is continuous or discrete
        :return: true if the defuzzifier is discrete or false otherwise
        '''
        return self.java_d.isDiscrete()

    def setDiscrete(self, discrete):
        '''
        Sets if the defuzzifier is continuous or discrete
        :param discrete: allowed object is boolean
        '''
        assert type(discrete)==bool
        self.java_d.setDiscrete(discrete)

    def __str__(self):
        '''
        Returns a String object representing this object
        :return: a string
        '''
        return self.java_d.toString()



    # 5 Methods from java abstract class DefuzzifierDiscrete

    def getDiscreteValue(self, x):
        '''
        Get a point's 'y' value
        :param x: the value x
        :return: a point's 'y' value
        '''
        assert type(x)==float
        return self.java_d.getDiscreteValue(x)

    def iterator(self):
        '''
        Get an iterator (on discreteValues' keys)
        :return: an iterator
        '''
        return self.java_d.iterator()

    def reset(self):
        '''
        Reset values
        '''
        self.java_d.reset()

    def setPoint(self, x, y):
        '''
        Set a point
        :param x: the value x
        :param y: the value y
        '''
        assert type(x)==float and type(y)==float
        self.java_d.setPoint(x, y)

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