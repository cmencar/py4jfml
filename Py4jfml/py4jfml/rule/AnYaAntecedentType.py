from py4j.java_gateway import JavaGateway

from py4jfml.knowledgebasevariable import AnYaDataCloudType

gateway = JavaGateway()

class AnYaAntecedentType:
    '''
    Python class for anYaAntecedentType complex type.
    '''

    def __init__(self, dataCloud=None):
        '''
        :param dataCloud: the cloud AnYaDataCloudType
        '''
        if dataCloud==None:
            self.java_aat = gateway.entry_point.getJFMLRule_Factory().createAnYaAntecedentType()
        else:
            assert type(dataCloud)==AnYaDataCloudType
            self.java_aat = gateway.entry_point.getJFMLRule_Factory().createAnYaAntecedentType(dataCloud.java_kbv)

    def getDataCloudName(self):
        '''
        Gets the value of the property dataCloudName
        :return: possible object is Object
        '''
        return self.java_aat.getDataCloudName()

    def setDataCloudName(self, value):
        '''
        Sets the value of the property dataCloudName
        :param value:
        '''
        self.java_aat.setDataCloudName(value)

    def __str__(self):
        '''
        Returns a String object representing this object
        :return: possible object is String
        '''
        return self.java_aat.toString()