import cProfile

from py4jfml.Py4Jfml import Py4jfml
from py4jfml.defuzzifier.DefuzzifierCenterOfArea import DefuzzifierCenterOfArea
from py4jfml.defuzzifier.DefuzzifierCenterOfGravity import DefuzzifierCenterOfGravity
from py4jfml.defuzzifier.DefuzzifierCenterOfGravitySingletons import DefuzzifierCenterOfGravitySingletons
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
from py4jfml.term.FuzzyTermType import FuzzyTermType

cProfile.run("f = DefuzzifierCenterOfArea(0.,10.,[FuzzyTermType()])")


cProfile.run("f=DefuzzifierCenterOfGravity(0.,10.,[FuzzyTermType()])")
cProfile.run("f=DefuzzifierCenterOfGravitySingletons(0.,10.)")
cProfile.run("f=DefuzzifierLeftMostMax(0.,10.,[FuzzyTermType()])")
cProfile.run("f=DefuzzifierMeanMax(0.,10.,[FuzzyTermType()])")
cProfile.run("f=DefuzzifierRightMostMax(0.,10.,[FuzzyTermType()])")

cProfile.run("f=FuzzySystemType()")
cProfile.run("f=ObjectFactory()")
cProfile.run("f=KnowledgeBaseType()")
cProfile.run("f=AggregatedFuzzyVariableType()")
cProfile.run("f=AnYaDataCloudType()")
cProfile.run("f=FuzzyVariableType()")
cProfile.run("f=TskVariableType()")
cProfile.run("f=TsukamotoVariableType()")
cProfile.run("f=WZ(0.,10.)")

cProfile.run("f=AntecedentType()")
cProfile.run("f=AnYaAntecedentType()")
cProfile.run("f=AnYaRuleType()")
cProfile.run("f=ClauseType()")
cProfile.run("f=ConsequentClausesType()")
cProfile.run("f=ConsequentType()")
cProfile.run("f=FuzzyRuleType()")
cProfile.run("f=TskClauseType()")
cProfile.run("f=TskConsequentClausesType()")
cProfile.run("f=TskConsequentType()")
cProfile.run("f=TskFuzzyRuleType()")

cProfile.run("f=AnYaRuleBaseType()")
cProfile.run("f=FuzzySystemRuleBase()")
cProfile.run("f=MamdaniRuleBaseType()")
cProfile.run("f=RuleBaseType()")
cProfile.run("f=TskRuleBaseType()")

cProfile.run("f=TsukamotoRuleBaseType()")