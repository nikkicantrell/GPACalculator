import unittest
import FinalCalculator
import StringIO
import sys

class TestFinalCalculator(unittest.TestCase):
    def test_numSectionsQuit(self):
        """tests for promptNumClasses quitting when quit is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'quit'
        with self.assertRaises(SystemExit):
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptNumSections()
        __builtins__.raw_input = original_raw_input
    def test_numSectionsInvalid(self):
        """tests for promptNumClasses when invalid input is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'wrong'
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptNumSections()
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals('Sorry your answer is not valid. Please enter a ' +
                          'number.', onlyOnePrint)
        __builtins__.raw_input = original_raw_input
    def test_numSectionsValid(self):
        """tests for promptNumClasses when there is valid input"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 3
        tmp = FinalCalculator.FinalCalculator()
        self.assertEquals(3, tmp.promptNumSections())
        __builtins__.raw_input = original_raw_input
    def test_functionQuit(self):
        """tests for promptFunction quitting when quit is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'quit'
        with self.assertRaises(SystemExit):
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptFunction()
        __builtins__.raw_input = original_raw_input
    def test_functionInvalidString(self):
        """tests for promptFunction when invalid input in the form of a string is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'wrong'
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptFunction()
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals("Sorry your answer is not valid. Enter 1 or 2", onlyOnePrint)
        __builtins__.raw_input = original_raw_input
    def test_functionInvalidInt(self):
        """tests for promptFunction when invalid input in the form of an int besides 1 and 2 is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 3
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptFunction()
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals("Sorry your answer is not valid. Enter 1 or 2", onlyOnePrint)
        __builtins__.raw_input = original_raw_input
    def test_functionValid(self):
        """tests for promptFunction when there is valid input"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 1
        tmp = FinalCalculator.FinalCalculator()
        self.assertEquals(1, tmp.promptFunction())
        __builtins__.raw_input = original_raw_input
    def test_lastPercentageQuit(self):
        """tests for promptLastPercentage quitting when quit is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'quit'
        with self.assertRaises(SystemExit):
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptLastPercentage()
        __builtins__.raw_input = original_raw_input
    def test_lastPercentageInvalidString(self):
        """tests for promptLastPercentage when invalid input in the form of a string is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'wrong'
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptLastPercentage()
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals("Sorry your answer is not valid. Please enter a " +
                          "number greater than 1.", onlyOnePrint)
        __builtins__.raw_input = original_raw_input
    def test_lastPercentageInvalidFloat(self):
        """tests for promptLastPercentage when invalid input in the form of a float < 1 is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: .01
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptLastPercentage()
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals("Sorry your answer is not valid. Please enter a " +
                          "number greater than 1.", onlyOnePrint)
    def test_lastPercentageValid(self):
        """tests for promptPercentage when there is valid input"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 25
        tmp = FinalCalculator.FinalCalculator()
        self.assertEquals(25, tmp.promptLastPercentage())
        __builtins__.raw_input = original_raw_input
    def test_wantedGradeQuit(self):
        """tests for promptWantedGrade quitting when quit is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'quit'
        with self.assertRaises(SystemExit):
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptWantedGrade()
        __builtins__.raw_input = original_raw_input
    def test_wantedGradeInvalid(self):
        """tests for promptWantedGrade when invalid input is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'wrong'
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptWantedGrade()
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals("Sorry your answer is not valid. Please enter one of" +
                          " the following: A, B, C, D", onlyOnePrint)
        __builtins__.raw_input = original_raw_input
    def test_wantedGradeValid(self):
        """tests for promptWantedGrade when there is valid input"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'D'
        tmp = FinalCalculator.FinalCalculator()
        self.assertEquals('D', tmp.promptWantedGrade())
        __builtins__.raw_input = original_raw_input
    def test_percentageQuit(self):
        """tests for promptPercentage quitting when quit is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'quit'
        with self.assertRaises(SystemExit):
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptPercentage(1)
        __builtins__.raw_input = original_raw_input
    def test_percentageInvalidString(self):
        """tests for promptPercentage when invalid input in the form of a string is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'wrong'
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptPercentage(1)
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals("Sorry your answer is not valid. Please enter a " +
                          "number greater than 1.", onlyOnePrint)
        __builtins__.raw_input = original_raw_input
    def test_percentageInvalidFloat(self):
        """tests for promptPercentage when invalid input in the form of a float < 1 is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: .01
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptPercentage(1)
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals("Sorry your answer is not valid. Please enter a " +
                          "number greater than 1.", onlyOnePrint)
    def test_percentageValid(self):
        """tests for promptPercentagewhen there is valid input"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 25
        tmp = FinalCalculator.FinalCalculator()
        self.assertEquals(25, tmp.promptPercentage(1))
        __builtins__.raw_input = original_raw_input
    def test_gradeQuit(self):
        """tests for promptGrade quitting when quit is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'quit'
        with self.assertRaises(SystemExit):
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptGrade(1)
        __builtins__.raw_input = original_raw_input
    def test_gradeInvalidString(self):
        """tests for promptGrade when invalid input in the form of a string is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'wrong'
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptGrade(1)
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals("Sorry your answer is not valid. Please enter a " +
                          "number greater than 1.", onlyOnePrint)
        __builtins__.raw_input = original_raw_input
    def test_gradeInvalidFloat(self):
        """tests for promptGrade when invalid input in the form of a float < 1 is entered"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: .01
        printed = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            sys.stdout = printed
            tmp = FinalCalculator.FinalCalculator()
            tmp.promptGrade(1)
            sys.stdout = sys.__stdout
        onlyOnePrint = printed.getvalue().split('\n')[0]
        self.assertEquals("Sorry your answer is not valid. Please enter a " +
                          "number greater than 1.", onlyOnePrint)
    def test_gradeValid(self):
        """tests for promptGrade when there is valid input"""
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 85
        tmp = FinalCalculator.FinalCalculator()
        self.assertEquals(85, tmp.promptGrade(1))
        __builtins__.raw_input = original_raw_input
    #do not have to test for invalid inputs because GPACalculator handles this in prompts
    def test_calculateNeeded(self):
        """tests calculateNeeded method"""
        percentagesAndGrades = [(20, 73.63), (20, 87.5), (20, 70)]
        tmp = FinalCalculator.FinalCalculator()
        self.assertEquals(tmp.calculateNeeded(40, 'B', percentagesAndGrades), 84.435)
    def test_calculateFinal(self):
        """tests calculateFinal method"""
        percentagesAndGrades = [(15, 100), (30, 79.7), (10, 80), (5, 80), (20, 94.5),
                                (12, 95), (8, 94.5)]
        tmp = FinalCalculator.FinalCalculator()
        self.assertAlmostEqual(tmp.calculateFinal(percentagesAndGrades), 88.77)
if __name__ == "__main__":
    unittest.main()
