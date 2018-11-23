import pydoc

from py4jfml.Py4Jfml import Py4jfml
from py4jfml.defuzzifier import DefuzzifierCenterOfGravitySingletons
from py4jfml.defuzzifier.DefuzzifierCenterOfArea import DefuzzifierCenterOfArea
from py4jfml.defuzzifier.DefuzzifierCenterOfGravity import DefuzzifierCenterOfGravity
from py4jfml.defuzzifier.DefuzzifierLeftMostMax import DefuzzifierLeftMostMax
from py4jfml.defuzzifier.DefuzzifierMeanMax import DefuzzifierMeanMax
from py4jfml.defuzzifier.DefuzzifierRightMostMax import DefuzzifierRightMostMax
from py4jfml.jaxb.FuzzySystemType import FuzzySystemType
from py4jfml.jaxb.ObjectFactory import ObjectFactory
from py4jfml.knowledgebase.KnowledgeBaseType import KnowledgeBaseType
from py4jfml.knowledgebasevariable.AggregatedFuzzyVariableType import AggregatedFuzzyVariableType
from py4jfml.knowledgebasevariable.AnYaDataCloudType import AnYaDataCloudType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.knowledgebasevariable.TskVariableType import TskVariableType
from py4jfml.knowledgebasevariable.TsukamotoVariableType import TsukamotoVariableType
from py4jfml.knowledgebasevariable.WZ import WZ
from py4jfml.rule.AnYaAntecedentType import AnYaAntecedentType
from py4jfml.rule.AnYaRuleType import AnYaRuleType
from py4jfml.rule.AntecedentType import AntecedentType
from py4jfml.rule.ClauseType import ClauseType
from py4jfml.rule.ConsequentClausesType import ConsequentClausesType
from py4jfml.rule.ConsequentType import ConsequentType
from py4jfml.rule.FuzzyRuleType import FuzzyRuleType
from py4jfml.rule.TskClauseType import TskClauseType
from py4jfml.rule.TskConsequentClausesType import TskConsequentClausesType
from py4jfml.rule.TskConsequentType import TskConsequentType
from py4jfml.rule.TskFuzzyRuleType import TskFuzzyRuleType
from py4jfml.rulebase.AnYaRuleBaseType import AnYaRuleBaseType
from py4jfml.rulebase.FuzzySystemRuleBase import FuzzySystemRuleBase
from py4jfml.rulebase.MamdaniRuleBaseType import MamdaniRuleBaseType
from py4jfml.rulebase.RuleBaseType import RuleBaseType
from py4jfml.rulebase.TskRuleBaseType import TskRuleBaseType
from py4jfml.rulebase.TsukamotoRuleBaseType import TsukamotoRuleBaseType

pydoc.help(DefuzzifierCenterOfArea)
pydoc.help(DefuzzifierCenterOfGravity)
pydoc.help(DefuzzifierCenterOfGravitySingletons)
pydoc.help(DefuzzifierLeftMostMax)
pydoc.help(DefuzzifierMeanMax)
pydoc.help(DefuzzifierRightMostMax)

pydoc.help(FuzzySystemType)
pydoc.help(ObjectFactory)
pydoc.help(KnowledgeBaseType)
pydoc.help(AggregatedFuzzyVariableType)
pydoc.help(AnYaDataCloudType)
pydoc.help(FuzzyVariableType)
pydoc.help(TskVariableType)
pydoc.help(TsukamotoVariableType)
pydoc.help(WZ)

pydoc.help(AntecedentType)
pydoc.help(AnYaAntecedentType)
pydoc.help(AnYaRuleType)
pydoc.help(ClauseType)
pydoc.help(ConsequentClausesType)
pydoc.help(ConsequentType)
pydoc.help(FuzzyRuleType)
pydoc.help(TskClauseType)
pydoc.help(TskConsequentClausesType)
pydoc.help(TskConsequentType)
pydoc.help(TskFuzzyRuleType)

pydoc.help(AnYaRuleBaseType)
pydoc.help(FuzzySystemRuleBase)
pydoc.help(MamdaniRuleBaseType)
pydoc.help(RuleBaseType)
pydoc.help(TskRuleBaseType)

pydoc.help(TsukamotoRuleBaseType)


Py4jfml.kill()
