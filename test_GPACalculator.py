import unittest
import GPACalculator
import StringIO
import sys

class TestGPACalculator(unittest.TestCase):
    def test_numClassQuit(self):
        """tests for promptNumClasses quitting when quit is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'quit'
        with self.assertRaises(SystemExit):
            tmp = GPACalculator.GPACalculator()
            tmp.promptNumClasses()
        __builtins__.raw_input = original_raw_input
    def test_numClassInvalid(self):
        """tests for promptNumClasses when invalid input is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'wrong'
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = GPACalculator.GPACalculator()
            tmp.promptNumClasses()
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals('Sorry your answer is not valid. Please enter a ' +
                          'number.', onlyOnePrint)
        __builtins__.raw_input = original_raw_input
    def test_numClassValid(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 3
        tmp = GPACalculator.GPACalculator()
        self.assertEquals(3, tmp.promptNumClasses())
        __builtins__.raw_input = original_raw_input
    def test_creditsQuit(self):
        """tests for promptCredits quitting when quit is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'quit'
        with self.assertRaises(SystemExit):
            tmp = GPACalculator.GPACalculator()
            tmp.promptCredits(1)
        __builtins__.raw_input = original_raw_input
    def test_creditsInvalid(self):
        """tests for promptCredits when invalid input is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'wrong'
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = GPACalculator.GPACalculator()
            tmp.promptCredits(1)
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals('Sorry your answer is not valid. Please enter a ' +
                          'number.', onlyOnePrint)
        __builtins__.raw_input = original_raw_input
    def test_creditsValid(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 3
        tmp = GPACalculator.GPACalculator()
        self.assertEquals(3, tmp.promptCredits(1))
        __builtins__.raw_input = original_raw_input
    def test_gradesQuit(self):
        """tests for promptGrade quitting when quit is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'quit'
        with self.assertRaises(SystemExit):
            tmp = GPACalculator.GPACalculator()
            tmp.promptGrade(1)
        __builtins__.raw_input = original_raw_input
    def test_gradesInvalid(self):
        """tests for promptGrade when invalid input is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'wrong'
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = GPACalculator.GPACalculator()
            tmp.promptGrade(1)
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals('Sorry your answer is not valid. Please enter one of ' +
                          'these options: A, B, C, D, F)', onlyOnePrint)
        __builtins__.raw_input = original_raw_input
    def test_gradesValid(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'B'
        tmp = GPACalculator.GPACalculator()
        self.assertEquals('B', tmp.promptGrade(1))
        __builtins__.raw_input = original_raw_input
    #do not have to test for invalid inputs because GPACalculator handles this in prompts
    def test_calculate(self):
        """tests calculate method"""
        gradesAndCredits = [(3, 'A'), (3, 'A'), (3, 'B'), (3, 'B'), (3, 'C')]
        tmp = GPACalculator.GPACalculator()
        self.assertEquals(tmp.calculate(gradesAndCredits), 3.2)
if __name__ == "__main__":
    unittest.main()
