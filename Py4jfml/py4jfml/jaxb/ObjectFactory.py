from py4j.java_gateway import JavaGateway

from py4jfml.aggregated.AndAggregatedType import AndAggregatedType
from py4jfml.aggregated.OrAggregatedType import OrAggregatedType
from py4jfml.jaxb.FuzzySystemType import FuzzySystemType
from py4jfml.knowledgebasevariable.AggregatedFuzzyVariableType import AggregatedFuzzyVariableType
from py4jfml.knowledgebasevariable.AnYaDataCloudType import AnYaDataCloudType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.knowledgebasevariable.TskVariableType import TskVariableType
from py4jfml.knowledgebasevariable.TsukamotoVariableType import TsukamotoVariableType
from py4jfml.operator.AndLogicalType import AndLogicalType
from py4jfml.operator.OrLogicalType import OrLogicalType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.rulebase.AnYaRuleBaseType import AnYaRuleBaseType
from py4jfml.rulebase.RuleBaseType import RuleBaseType
from py4jfml.rulebase.TskRuleBaseType import TskRuleBaseType
from py4jfml.term.CircularTermType import CircularTermType

gateway = JavaGateway()

class ObjectFactory:
    '''
    This object contains factory methods for each Java content interface and Java element interface generated in the jfml package.
    '''

    def __init__(self):
        '''
        Create a new ObjectFactory that can be used to create new instances of schema derived classes for project jfml
        '''
        self.java_of = gateway.entry_point.getJFMLjaxb_Factory().createObjectFactory()

    def createAggregatedFuzzyTermType(self):
        '''
        Create an instance of AggregatedFuzzyTermType
        :return: an instance of AggregatedFuzzyTermType
        '''
        return self.java_of.createAggregatedFuzzyTermType()

    def createAggregatedFuzzyVariableType(self):
        '''
        Create an instance of AggregatedFuzzyVariableType
        :return: an instance of AggregatedFuzzyVariableType
        '''
        return self.java_of.createAggregatedFuzzyVariableType()

    def createAndAggregatedType(self):
        '''
        Create an instance of AndAggregatedType
        :return: an instance of AndAggregatedType
        '''
        return self.java_of.createAndAggregatedType()

    def createAndAggregatedTypeAnd(self, value):
        '''
        Create an instance of JAXBElement<AndAggregatedType>
        :param value: allowed object is AndAggregatedType
        :return: an instance of JAXBElement<AndAggregatedType>
        '''
        assert type(value)==AndAggregatedType
        return self.java_of.createAndAggregatedTypeAnd(value.java_at)

    def createAndAggregatedTypeClause(self, value):
        '''
        Create an instance of JAXBElement<ClauseType>
        :param value: allowed object is ClauseType
        :return: an instance of JAXBElement<ClauseType>
        '''
        assert type(value)==ClauseType
        return self.java_of.createAndAggregatedTypeClause(value.java_ct)

    def createAndAggregatedTypeOr(self, value):
        '''
        Create an instance of JAXBElement<OrAggregatedType>
        :param value: allowed object is OrAggregatedType
        :return: an instance of JAXBElement<OrAggregatedType>
        '''
        assert type(value)==OrAggregatedType
        return self.java_of.createAndAggregatedTypeOr(value.java_at)

    def createAndLogicalType(self):
        '''
        Create an instance of AndLogicalType
        :return: an instance of AndLogicalType
        '''
        return self.java_of.createAndLogicalType()

    def createAndLogicalTypeAnd(self, value):
        '''
        Create an instance of JAXBElement<AndLogicalType>
        :param value: allowed object is AndLogicalType
        :return: an instance of JAXBElement<AndLogicalType>
        '''
        assert type(value)==AndLogicalType
        return self.java_of.createAndLogicalTypeAnd(value.java_lt)

    def createAndLogicalTypeOr(self, value):
        '''
        Create an instance of JAXBElement<OrLogicalType>
        :param value: allowed object is OrLogicalType
        :return: an instance of JAXBElement<OrLogicalType>
        '''
        assert type(value)==OrLogicalType
        return self.java_of.createAndLogicalTypeOr(value.java_lt)

    def createAndLogicalTypeTermName(self, value):
        '''
        Create an instance of JAXBElement<CircularTermType>
        :param value: allowed object is CircularTermType
        :return: an instance of JAXBElement<CircularTermType>
        '''
        assert type(value)==CircularTermType
        return self.java_of.createAndLogicalTypeTermName(value.java_t)

    def createAntecedentType(self):
        '''
        Create an instance of AntecedentType
        :return: an instance of AntecedentType
        '''
        return self.java_of.createAntecedentType()

    def createAnYaAntecedentType(self):
        '''
        Create an instance of AnYaAntecedentType
        :return: an instance of AnYaAntecedentType
        '''
        return self.java_of.createAnYaAntecedentType()

    def createAnYaDataCloudType(self):
        '''
        Create an instance of AnYaDataCloudType
        :return: an instance of AnYaDataCloudType
        '''
        return self.java_of.createAnYaDataCloudType()

    def createAnYaRuleBaseType(self):
        '''
        Create an instance of AnYaRuleBaseType
        :return: an instance of AnYaRuleBaseType
        '''
        return self.java_of.createAnYaRuleBaseType()

    def createAnYaRuleType(self):
        '''
        Create an instance of AnYaRuleType
        :return: an instance of AnYaRuleType
        '''
        return self.java_of.createAnYaRuleType()

    def createCircularDefinitionType(self):
        '''
        Create an instance of CircularDefinitionType
        :return: an instance of CircularDefinitionType
        '''
        return self.java_of.createCircularDefinitionType()

    def createCircularTermType(self):
        '''
        Create an instance of CircularTermType
        :return: an instance of CircularTermType
        '''
        return self.java_of.createCircularTermType()

    def createClauseType(self):
        '''
        Create an instance of ClauseType
        :return: an instance of ClauseType
        '''
        return self.java_of.createClauseType()

    def createConsequentClausesType(self):
        '''
        Create an instance of ConsequentClausesType
        :return: an instance of ConsequentClausesType
        '''
        return self.java_of.createConsequentClausesType()

    def createConsequentType(self):
        '''
        Create an instance of ConsequentType
        :return: an instance of ConsequentType
        '''
        return self.java_of.createConsequentType()

    def createCustomShapeType(self):
        '''
        Create an instance of CustomShapeType
        :return: an instance of CustomShapeType
        '''
        return self.java_of.createCustomShapeType()

    def createFourParamType(self):
        '''
        Create an instance of FourParamType
        :return: an instance of FourParamType
        '''
        return self.java_of.createFourParamType()

    def createFuzzyRuleType(self):
        '''
        Create an instance of FuzzyRuleType
        :return: an instance of FuzzyRuleType
        '''
        return self.java_of.createFuzzyRuleType()

    def createFuzzySystem(self, value):
        '''
        Create an instance of JAXBElement<FuzzySystemType>
        :param value: allowed object is FuzzySystemType
        :return: an instance of JAXBElement<FuzzySystemType>
        '''
        assert type(value)==FuzzySystemType
        return self.java_of.createFuzzySystem(value.java_fst)

    def createFuzzySystemType(self):
        '''
        Create an instance of FuzzySystemType
        :return: an instance of FuzzySystemType
        '''
        return self.java_of.createFuzzySystemType()

    def createFuzzySystemTypeAnYaRuleBase(self, value):
        '''
        Create an instance of JAXBElement<AnYaRuleBaseType>
        :param value: allowed object is AnYaRuleBaseType
        :return: an instance of JAXBElement<AnYaRuleBaseType>
        '''
        assert type(value)==AnYaRuleBaseType
        return self.java_of.createFuzzySystemTypeAnYaRuleBase(value.java_fsrb)

    def createFuzzySystemTypeMamdaniRuleBase(self, value):
        '''
        Create an instance of JAXBElement<RuleBaseType>
        :param value: allowed object is RuleBaseType
        :return: an instance of JAXBElement<RuleBaseType>
        '''
        assert type(value)==RuleBaseType
        return self.java_of.createFuzzySystemTypeMamdaniRuleBase(value.java_fsrb)

    def createFuzzySystemTypeTskRuleBase(self, value):
        '''
        Create an instance of JAXBElement<TskRuleBaseType>
        :param value: allowed object is TskRuleBaseType
        :return: an instance of JAXBElement<TskRuleBaseType>
        '''
        assert type(value)==TskRuleBaseType
        return self.java_of.createFuzzySystemTypeTskRuleBase(value.java_fsrb)

    def createFuzzySystemTypeTsukamotoRuleBase(self, value):
        '''
        Create an instance of JAXBElement<RuleBaseType>
        :param value: allowed object is RuleBaseType
        :return: an instance of JAXBElement<RuleBaseType>
        '''
        assert type(value)==RuleBaseType
        return self.java_of.createFuzzySystemTypeTsukamotoRuleBase(value.java_fsrb)

    def createFuzzyTermType(self):
        '''
        Create an instance of FuzzyTermType
        :return: an instance of FuzzyTermType
        '''
        return self.java_of.createFuzzyTermType()

    def createFuzzyVariableType(self):
        '''
        Create an instance of FuzzyVariableType
        :return: an instance of FuzzyVariableType
        '''
        return self.java_of.createFuzzyVariableType()

    def createKnowledgeBaseType(self):
        '''
        Create an instance of KnowledgeBaseType
        :return: an instance of KnowledgeBaseType
        '''
        return self.java_of.createKnowledgeBaseType()

    def createKnowledgeBaseTypeAggregatedFuzzyVariable(self, value):
        '''
        Create an instance of JAXBElement<AggregatedFuzzyVariableType>
        :param value: allowed object is AggregatedFuzzyVariableType
        :return: an instance of JAXBElement<AggregatedFuzzyVariableType>
        '''
        assert type(value)==AggregatedFuzzyVariableType
        return self.java_of.createKnowledgeBaseTypeAggregatedFuzzyVariable(value.java_kbv)

    def createKnowledgeBaseTypeAnYaDataCloud(self, value):
        '''
        Create an instance of JAXBElement<AnYaDataCloudType>
        :param value: allowed object is AnYaDataCloudType
        :return: an instance of JAXBElement<AnYaDataCloudType>
        '''
        assert type(value)==AnYaDataCloudType
        return self.java_of.createKnowledgeBaseTypeAnYaDataCloud(value.java_kbv)

    def createKnowledgeBaseTypeFuzzyVariable(self, value):
        '''
        Create an instance of JAXBElement<FuzzyVariableType>
        :param value: allowed object is FuzzyVariableType
        :return: an instance of JAXBElement<FuzzyVariableType>
        '''
        assert type(value)==FuzzyVariableType
        return self.java_of.createKnowledgeBaseTypeFuzzyVariable(value.java_kbv)

    def createKnowledgeBaseTypeTskVariable(self, value):
        '''
        Create an instance of JAXBElement<TskVariableType>
        :param value: allowed object is TskVariableType
        :return: an instance of JAXBElement<TskVariableType>
        '''
        assert type(value)==TskVariableType
        return self.java_of.createKnowledgeBaseTypeTskVariable(value.java_kbv)

    def createKnowledgeBaseTypeTsukamotoVariable(self, value):
        '''
        Create an instance of JAXBElement<TsukamotoVariableType >
        :param value: allowed object is TsukamotoVariableType
        :return: an instance of JAXBElement<TsukamotoVariableType >
        '''
        assert type(value)==TsukamotoVariableType
        return self.java_of.createKnowledgeBaseTypeTsukamotoVariable(value.java_kbv)





