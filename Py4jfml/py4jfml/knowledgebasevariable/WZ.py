from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

class WZ:
    '''
    Python class for representing the values w and z in the tsukamotoVariableType
    '''

    def __init__(self, w, z):
        '''
        :param w:
        :param z:
        '''
        assert type(w)==float and type(z)==float
        self.java_wz = gateway.entry_point.getJFMLKnowledgebaseVariable_Factory().createWZ(w, z)

    def getW(self):
        return self.java_wz.getW()

    def getZ(self):
        return self.java_wz.getZ()

    def setW(self, w):
        assert type(w)==float
        self.java_wz.setW(w)

    def setZ(self, z):
        assert type(z)==float
        self.java_wz.setZ(z)

    def __str__(self):
        '''
        Returns a String object representing this object
        :return: a String object representing this object
        '''
        return self.java_wz.toString()
