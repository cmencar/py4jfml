from py4j.java_gateway import JavaGateway
from py4jfml.knowledgebasevariable import TskVariableType as tskvt
from py4jfml.term import TskTermType as tsktt

gateway = JavaGateway()


class TskClauseType:
    '''
    Python class for tskClauseType complex type
    '''

    def __init__(self, variable=None, term=None):
        '''
        :param variable: possible object is TskVariableType
        :param term: possible object is TskTermType
        '''
        if variable==None and term==None:
            self.java_tskct = gateway.entry_point.getJFMLRule_Factory().createTskClauseType()
        elif variable!=None and term!=None:
            assert type(variable)==tskvt.TskVariableType
            assert type(term)==tsktt.TskTermType
            self.java_tskct = gateway.entry_point.getJFMLRule_Factory().createTskClauseType(variable.java_kbv, term.java_t)


    def getTerm(self):
        '''
        Gets the value of the property term
        :return: possible object is Object
        '''
        return self.java_tskct.getTerm()

    def getVariable(self):
        '''
        Gets the value of the property variable
        :return: possible object is Object
        '''
        return self.java_tskct.getVariable()

    def setTerm(self, value):
        '''
        Sets the value of the property term
        :param value: allowed object is TskTermType
        '''
        assert type(value)==tsktt.TskTermType
        self.java_tskct.setTerm(value.java_t)


    def setVariable(self, value):
        '''
        Sets the value of the property variable
        :param value: allowed object is TskVariableType
        '''
        assert type(value)==tskvt.TskVariableType
        self.java_tskct.setVariable(value.java_kbv)