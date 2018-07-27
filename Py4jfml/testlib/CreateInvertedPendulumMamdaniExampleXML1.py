from py4jfml.FuzzyInferenceSystem import FuzzyInferenceSystem
from py4jfml.knowledgebase.KnowledgeBaseType import KnowledgeBaseType
from py4jfml.knowledgebasevariable.FuzzyVariableType import FuzzyVariableType
from py4jfml.term.FuzzyTermType import FuzzyTermType

invertedPendulum = FuzzyInferenceSystem("invertedPendulum - MAMDANI")

kb = KnowledgeBaseType()
invertedPendulum.setKnowledgeBase(kb)

ang = FuzzyVariableType("Angle", 0.0, 255.0)

print(invertedPendulum)

ang_vneg = FuzzyTermType("very negative", FuzzyTermType.TYPE_trapezoidShape,[0.0, 0.0, 48.0, 88.0])

print(ang_vneg)

#continuare...