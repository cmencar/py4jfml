import unittest
from click.testing import CliRunner
import cli.py4jfmlcli as cli
import os as OS
import csv

#Number of test case
n = 24
class TestCLI(unittest.TestCase):

    def setUp(self):
        #Runner of CLI
        self.runner = []
        for i in range(n):
            self.runner.append(None)
            self.runner[i] = CliRunner()
        #Input of CLI
        self.args = [['-l','XMLFiles/JDAM.xml','-i','2,2,1,2,1'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/iJDAM.csv'],['-l','XMLFiles/JDAM.xml','-i','2,2,1,2,1','-o','CSVFiles/output.csv'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/iJDAM.csv','-o','CSVFiles/output.csv'],['-o','CSVFiles/output.csv','-e','CSVFiles/iJDAM.csv','-l','XMLFiles/JDAM.xml'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/iJDAMs.csv'],['-l','XMLFiles/JDAM.xml','-i','2,2,1,2'],['-l','XMLFiles/JDAM.xml','-i','2,2,1,2,1,1'],['-l','XMLFiles/JDA.xml','-e','CSVFiles/iJDAM.csv'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/inpu.csv'],['-l','XMLFiles/empty.xml','-e','CSVFiles/iJDAM.csv'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/empty.csv'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/iJDAMi.csv'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/iJDAMf.csv'],['-l','XMLFiles/JDAM','-e','CSVFiles/iJDAM'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/input'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/iJDAM.csv','-o','CSVFiles/output'],['-l','XMLFiles/JDAM.xml','-i','a'],['-l','XMLFiles/JDAM.xml','-i','a,b'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/1str.csv'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/2str.csv'],['-l','XMLFiles/JDAM.xml','-e','CSVFiles/1int1str.csv'],['-l','XMLFiles/JDAM.xml'],[]]
        #Expected Output
        self.expect = ['1.020752\n','1.020752\n1.1291949\n','1.020752\n','1.020752,1.1291949\n','1.020752,1.1291949\n','1.020752\n','Wrong number of arguments in Evaluate\n','Wrong number of arguments in Evaluate\n','A file isn\'t found\n','A file isn\'t found\n','A file is empty\n','A file is empty\n','Wrong number of arguments in Evaluate\n','Wrong number of arguments in Evaluate\n','A file haven\'t the correct extension\n','A file haven\'t the correct extension\n','A file haven\'t the correct extension\n','Values must be Integer or Float in Evaluate\n','Values must be Integer or Float in Evaluate\n','Values must be Integer or Float in Evaluate\n','Values must be Integer or Float in Evaluate\n','Values must be Integer or Float in Evaluate\n','Can\'t be executed only Load\n','Wrong or missing option\n']

    def tearDown(self):
        self.runner = None
        self.args = None
        self.expect = None

    #Load + Evaluates
    def test_0(self):
        index = 0
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluate
    def test_1(self):
        index = 1
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluates + Output
    def test_2(self):
        index = 2
        self.runner[index].invoke(cli.startCLI,self.args[index])
        with open('CSVFiles/output.csv') as f:
            s = f.read() + '\n'
        s = s[:-2]
        self.assertEqual(s,self.expect[index])
        OS.remove('CSVFiles/output.csv')

    #Load + Evaluate + Output
    def test_3(self):
        index = 3
        self.runner[index].invoke(cli.startCLI,self.args[index])
        with open('CSVFiles/output.csv') as f:
            s = f.read() + '\n'
        s = s[:-2]
        self.assertEqual(s,self.expect[index])
        OS.remove("CSVFiles/output.csv")

     #Output + Evaluate + Load
    def test_4(self):
        index = 4
        self.runner[index].invoke(cli.startCLI,self.args[index])
        with open('CSVFiles/output.csv') as f:
            s = f.read() + '\n'
        s = s[:-2]
        self.assertEqual(s,self.expect[index])
        OS.remove("CSVFiles/output.csv")

    #Load + Evaluate using a file that contain 1 space
    def test_5(self):
        index = 5
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluate with 1 argument
    def test_6(self):
        index = 6
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluate with 3 argument
    def test_7(self):
        index = 7
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load with file inexistent
    def test_8(self):
        index = 8
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluate with file inexistent
    def test_9(self):
        index = 9
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load with empty file xml
    def test_10(self):
        index = 10
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluate with blank file csv
    def test_11(self):
        index = 11
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluate with file csv with more than 5 values on first row
    def test_12(self):
        index = 12
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluate with file csv with more than 5 values on first row
    def test_13(self):
        index = 13
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load with wrong file extension
    def test_14(self):
        index = 14
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluate with wrong file extension
    def test_15(self):
        index = 15
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluate + Output with wrong file extension
    def test_16(self):
        index = 16
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluate with 1 character in input
    def test_17(self):
        index = 17
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluates with 2 characters in input
    def test_18(self):
        index = 18
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluates using a file csv with 1 charater
    def test_19(self):
        index = 19
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluates using a file csv with 2 charaters
    def test_20(self):
        index = 20
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Load + Evaluates using a file with a number and a character
    def test_21(self):
        index = 21
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #Only Load
    def test_22(self):
        index = 22
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

    #No option
    def test_23(self):
        index = 23
        result = self.runner[index].invoke(cli.startCLI,self.args[index])
        self.assertEqual(result.output,self.expect[index])

if __name__ == '__main__':
    unittest.main()