import sys

class Calculator(object):

    def __init__(self):
        pass
    def calculate(self, gradesAndCredits):
        """Calculates the users GPA"""
        qualityPts = 0
        numCredits = 0
        for x in range(len(gradesAndCredits)):
            grade = gradesAndCredits[x][1]
            if grade == 'A':
                grade = 4
            elif grade == 'B':
                grade = 3
            elif grade == 'C':
                grade = 2
            elif grade =='D':
                grade = 1
            else:
                grade = 0
            qualityPts += gradesAndCredits[x][0] * grade
            numCredits += gradesAndCredits[x][0]
        return float(qualityPts)/numCredits
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print ("Usage: python calculator.py")
    else:
        print('Please note you can exit the program at any time by entering "quit"')
        while True:
            try:
                numClasses = raw_input("How many classes do you have? ")
                numClassesInt = int(numClasses)
            except ValueError:
                if numClasses == "quit":
                    sys.exit()
                print("Sorry your answer is not valid. Please enter a number.")
            else:
                break
        gradesAndCredits = []
        for x in range(numClassesInt):
            while True:
                try:
                    credits = raw_input("How many credits is class #" +
                                        str(x+1) + "? ")
                    creditsInt = int(credits)
                except ValueError:
                    if credits == "quit":
                        sys.exit()
                    print("Sorry your answer is not valid. Please enter a number.")
                else:
                    break
            while True:
                grade = raw_input("What grade did you get in class #" + str(x) +
                              "(A, B, C, D, F)? ")
                gradeStripped = grade.lstrip().rstrip()
                if (gradeStripped != 'A' and gradeStripped != 'B'
                    and gradeStripped != 'C' and gradeStripped != 'D'
                    and gradeStripped != 'F'):
                    if(gradeStripped == "quit"):
                        sys.exit()
                    else:
                        print("Sorry your answer is not valid. Please enter one " +
                          "of these options: A, B, C, D, F)")
                else:
                    break
            gradesAndCredits.append((creditsInt, grade))
        calculator = Calculator()
        gpa = calculator.calculate(gradesAndCredits)
        print("Your gpa is: " + str(gpa))
