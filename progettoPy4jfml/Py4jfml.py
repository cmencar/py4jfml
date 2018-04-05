from py4j.java_gateway import JavaGateway
from py4j.java_collections import ListConverter
gateway = JavaGateway()


class PY4JFML:
    """
    La classe PY4JFML permette di caricare o scirvere un file xml contenente un sistema fuzzy
    """

    @staticmethod
    def load(xml_fileName):
        """
        il metodo load permette di caricare un file xml
        :param xml_fileName: contiene il percorso del file
        :param JFML: crea una istanza vuota della classe scritta in java
        :param xml: contiene il file xml
        :param java_fis: è la variabile che si collega alla libreria JFML
        :param fuzzyInferenceSystem: è la variabile che contiene il file appena caricato
        :return: fuzzyInferenceSystem
        """
        assert type(xml_fileName) == str
        JFML = gateway.entry_point.createJFML()
        xml = gateway.jvm.java.io.File(str(xml_fileName))
        java_fis = JFML.load(xml)
        fuzzyInferenceSystem = FuzzyInferenceSystem(java_fis)
        return fuzzyInferenceSystem

    @staticmethod
    def writeFSTtoXML(fst, str_output):
        """"
        il metodo writeFSTtoXML permette di scrivere un file xml
        :param fst: contiene il sistema fuzzy
        :param str_output: contiene il percorso del file
        :param JFML: crea una istanza vuota della classe scritta in java
        :param xmlOutput: contiene il file xml
        :return: JFML.writeFSTtoXML(fst.java_fis, xmlOutput)
                """
        assert type(fst) == FuzzyInferenceSystem and type(str_output) == str
        JFML = gateway.entry_point.createJFML()
        xmlOutput = gateway.jvm.java.io.File(str(str_output))
        return JFML.writeFSTtoXML(fst.java_fis, xmlOutput)


class FuzzyTerm:
    """
    La classe FuzzyTerm contiene i tipi a cui fanno riferimento i grafici
    :param TYPE_rightLinearShape: contiene il riferimento alla linea destra
    :param TYPE_leftLinearShape: contiene il riferimento alla linea sinistra
    :param  TYPE_piShape: contiene il riferimento al piShape
    :param TYPE_triangularShape: contiene il riferimento al triangolo
    :param TYPE_gaussianShape: contiene il riferimento alla gaussiana
    :param TYPE_rightGaussianShape: contiene il riferimento alla gaussiana destra
    :param  TYPE_leftGaussianShape: contiene il riferimento alla gaussiana sinistra
    :param TYPE_trapezoidShape: contiene il riferimento al trapezio
    :param TYPE_singletonShape: contiene il riferimento alla linea
    :param TYPE_rectangularShape: contiene il riferimento al rettangolo
    :param TYPE_zShape: contiene il riferimento alla Z shape
    :param TYPE_sShape: contiene il riferimento alla S shape
    :param TYPE_pointSetShape: contiene il riferimento al punto
    :param TYPE_pointSetMonotonicShape: contiene il riferimento al pointSetMonotonicShape
    :param TYPE_circularDefinition: contiene il riferimento al circularDefinition
    :param TYPE_customShape: contiene il riferimento al customShape
    :param TYPE_customMonotonicShape: contiene il riferimento al customMonotonicShape
    """
    TYPE_rightLinearShape = 0
    TYPE_leftLinearShape = 1
    TYPE_piShape = 2
    TYPE_triangularShape = 3
    TYPE_gaussianShape = 4
    TYPE_rightGaussianShape = 5
    TYPE_leftGaussianShape = 6
    TYPE_trapezoidShape = 7
    TYPE_singletonShape = 8
    TYPE_rectangularShape = 9
    TYPE_zShape = 10
    TYPE_sShape = 11
    TYPE_pointSetShape = 12
    TYPE_pointSetMonotonicShape = 13
    TYPE_circularDefinition = 14
    TYPE_customShape = 15
    TYPE_customMonotonicShape = 16


class FuzzyInferenceSystem:
    """
    La classe FuzzyInferenceSystem crea il sistema fuzzy
    """

    def __init__(self,name=None):
        """
        Costruttori del FuzzyInferenceSystem
        :param name: nome del sistema fuzzy
        :param java_fis: colleggamento alla JFML
        """
        if name==None:
            self.java_fis = gateway.entry_point.createFuzzyInferenceSystem()
        elif type(name) == str:
            assert type(name) == str
            self.java_fis = gateway.entry_point.createFuzzyInferenceSystem(str(name))
        elif(type(name)== FuzzyInferenceSystem):
            self.java_fis = name.fuzzyInferenceSystem
        else:
            self.java_fis = name

    def setKnowledgeBase(self, value):
        """
        Imposta il valore della conoscenza di base
        :param value: variabile contenete il valore
        """
        assert type(value) == KnowledgeBaseType
        self.java_fis.setKnowledgeBase(value.java_kb)

    def addRuleBase(self,r):
        """
        Aggiunge le regole base
        :param r: variabile contenete la regola
        """
        assert type(r) == MamdaniRuleBaseType
        self.java_fis.addRuleBase(r.java_mrbt)

    def getVariable(self,name):
        """
        Ottiene il nome della variabile
        :param name: contiene il nome della variabile
        """
        assert type(name) == str
        return FuzzyVariableType(self.java_fis.getVariable(str(name)))

    def evaluate(self):
        """
        Valuta il sistema fuzzy
        """
        self.java_fis.evaluate()

    def __str__(self):
        """
        Stampa su console il sistema fuzzy
        """
        return self.java_fis.toString()


class KnowledgeBaseType:
    """
    Conoscenza di base del sistema fuzzy
    """
    def __init__(self):
        """
        Costruttore della conoscenza di base
        """
        self.java_kb = gateway.entry_point.createKnowledgeBaseType()

    def addVariable(self,var):
        """
        Aggiunge la variabile alla conoscenza base
        :param var: contiene la variabile da aggiungere
        """
        assert type(var) == FuzzyVariableType
        self.java_kb.addVariable(var.java_fvt)


class FuzzyVariableType:
    """
    Definisce i tipi di variabile fuzzy
    """

    def __init__(self,name=None,domainLeft=None,domainRight=None):
        """
        Costruttori dei tipi di variabile fuzzy
        :param name: nome della regola
        :param domainLeft: dominio sinistro
        :param domainRight: dominio destro
        :param java_fvt: contiene il collegamento con JFML
        """
        if(name==None):
            self.java_fvt = gateway.entry_point.createFuzzyVariableType()
        elif(type(name) == str and type(domainRight)== float and type(domainLeft)==float):
            assert type(name) == str and type(domainRight)== float and type(domainLeft)==float
            self.java_fvt = gateway.entry_point.createFuzzyVariableType(str(name),float(domainLeft) ,float(domainRight))
        else:
            self.java_fvt = name

    def addFuzzyTerm(self, ft):
        """
        Aggiunge la regola al sistema fuzzy
        :param ft: regola fuzzy
        """
        assert  type(ft) == FuzzyTermType
        self.java_fvt.addFuzzyTerm(ft.java_ftt)

    def setValue(self, x):
        """
        Imposta il valore alle regole fuzzy
        :param x: contiene il valore
        """
        assert type(x) == float
        self.java_fvt.setValue(float(x))

    def getValue(self):
        """
        Ottiene il valore delle regole fuzzy
        :return: restituisce il valore
        """
        return self.java_fvt.getValue()

    def getName(self):
        """
        Ottiene il nome delle regole fuzzy
        :return: restituisce il nome delle regole fuzzy
        """
        return self.java_fvt.getName()

    def setDefaultValue(self, value):
        """
        Imposta i valori di default
        :param value: valore di default
        """
        assert type(value) == float
        self.java_fvt.setDefaultValue(float(value))

    def setAccumulation(self, value):
        """
        Imposta il valore di accumulazione
        :param value: valore di accumulazione
        :return: restituisce il valore di accumulazione
        """
        assert type(value) == str
        self.java_fvt.setAccumulation(str(value))

    def setDefuzzifierName(self, value):
        """
        Imposta il nome del defuzzifier
        :param value: nome deffuzifier
        :return: restituisce il nome
        """
        assert type(value) == str
        self.java_fvt.setDefuzzifierName(str(value))

    def setType(self, value):
        """
        Imposta il tipo delle regole fuzzy
        :param value: tipo
        """
        assert  type(value) == str
        self.java_fvt.setType(str(value))


class FuzzyTermType:
    """
    Definisce i termini del sistema fuzzy
    """

    def __init__(self, name, type_java, param):
        """
        Costruttore FuzzyTermType
        :param name: contiene il nome dei termini
        :param type_java: contiene i tipi descritti nella classe FuzzyTerm
        :param param: è un array di numeri float che indicano i parametri dei grafici
        :param java_ftt: contiene il collegamento con JFML
        """
        assert type(name) == str and type(type_java) == int and type(param) == list
        java_list = ListConverter().convert(param, gateway._gateway_client)
        self.java_ftt = gateway.entry_point.createFuzzyTermType(str(name), int(type_java), java_list)

    def setComplement(self, value):
        """
        Imposta i valori dei complementi
        :param value: contiene il complemento
        """
        assert type(value) == str
        self.java_ftt.setComplement(str(value))



class MamdaniRuleBaseType:
    """
    Definisce le regole di base Mamdani del sistema fuzzy
    """

    def __init__(self,name):
        """
        Costruttore Mamdani
        :param name: contiene il nome delle regole base Mamdani
        :param java_mrbt: contiene il collegamento con JFML
        """
        assert type(name) == str
        self.java_mrbt= gateway.entry_point.createMamdaniRuleBaseType(str(name))

    def addRule(self, rule):
        """
        Aggiunge una lista di regole Mamdani
        :param rule: contiene una lista di regole Mamdani
        """
        assert type(rule == FuzzyRuleType)
        self.java_mrbt.addRule(rule.java_frt)


class FuzzyRuleType:
    """
    Definisce il tipo di regole fuzzy
    """

    def __init__(self, name=None, connector=None, connectorMethod=None, weight=0.):
        """
        Costruttore FuzzyRuleType
        :param name: contiene il nome delle regole fuzzy
        :param connector: contiene il connettore che collega le diverse clausole nella parte antecedente (e/o)
        :param connectorMethod: contiene l'algoritmo da utilizzare se il connettore scelto è e od o.
        :param weight: contiene il peso della regola da utilizzare
        :param java_frt contiene il collegamento con JFML
        """
        if name==None:
            self.java_frt = gateway.entry_point.createFuzzyRuleType()
        else:
            assert type(name) == str and type(connector) == str and type(connectorMethod) == str and type(weight) == float
            self.java_frt= gateway.entry_point.createFuzzyRuleType(str(name), str(connector), str(connectorMethod), float(weight))

    def setAntecedent(self, value):
        """
        Imposta il valore antecedente alle regole
        :param value: contiene il valore antecedente alle regole
        """
        assert  type(value) == AntecedentType
        self.java_frt.setAntecedent(value.java_at)

    def setConsequent(self, value):
        """
        Imposta il valore conseguente alle regole
        :param value: contiene il valore conseguente alle regole
        """
        assert type(value) == ConsequentType
        self.java_frt.setConsequent(value.java_ct)


class AntecedentType:
    """
    Definisce le regole antecedenti del sistema fuzzy
    """

    def __init__(self):
        """
        Costruttore AntecedentType
        :param java_at: contiene il collegamento con JFML
        """
        self.java_at = gateway.entry_point.createAntecedentType()

    def addClause(self, c):
        """
        Aggiunge una lista di clausole nelle regole Antecedenti
        :param c: lista di clausole
        """
        assert type(c) == ClauseType
        self.java_at.addClause(c.java_clauseT)


class ConsequentType:
    """
    Definisce le regole conseguenti del sistema fuzzy
    """

    def __init__(self):
        """
        Costruttore ConsequentType
        """
        self.java_ct = gateway.entry_point.createConsequentType()

    def addThenClause(self, c):
        """
        Aggiunge una lista di clausole nelle regole conseguenti
        :param c: lista di clausole
        """
        assert type(c) == ClauseType
        self.java_ct.addThenClause(c.java_clauseT)


class ClauseType:
    """
    Definisce le clausole di un sistema fuzzy
    """

    def __init__(self, variable, term, modifier=None):
        """
        Costruttore ClauseType
        :param variable: contiene un oggetto KnowledgeBaseVariable
        :param term: contiene un oggetto FuzzyTerm
        :param modifier: contiene il modificatore di una stringa secondo lo StandardModifierType
        :param java_ct: contiene il collegamento con JFML
        """
        if modifier == None:
            assert type(variable) == FuzzyVariableType and type(term) == FuzzyTermType
            self.java_clauseT = gateway.entry_point.createClauseType(variable.java_fvt, term.java_ftt)
        else:
            assert type(variable) == FuzzyVariableType and type(term) == FuzzyTermType and type(modifier) == str
            self.java_clauseT = gateway.entry_point.createClauseType(variable.java_fvt, term.java_ftt, modifier)