import sys

class GPACalculator(object):

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
    def promptNumClasses(self):
        tries = 0
        while True:
            #prevents infinite loop in tests
            if tries > 10:
                sys.exit()
            try:
                numClasses = raw_input("How many classes do you have? ")
                numClassesInt = int(numClasses)
            except ValueError:
                if numClasses == "quit":
                    sys.exit()
                print("Sorry your answer is not valid. Please enter a number.")
                tries += 1
            else:
                return numClassesInt
    def promptCredits(self, number):
        tries = 0
        while True:
            #prevents infinite loop in tests
            if tries > 10:
                sys.exit()
            try:
                credits = raw_input("How many credits is class #" +
                                    str(number+1) + "? ")
                creditsInt = int(credits)
            except ValueError:
                if credits == "quit":
                    sys.exit()
                print("Sorry your answer is not valid. Please enter a number.")
                tries += 1
            else:
                return creditsInt
    def promptGrade(self, number):
        tries = 0
        while True:
            #prevents infinite loop in tests
            if tries > 10:
                sys.exit()
            grade = raw_input("What grade did you get in class #" + str(number+1) +
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
                    tries += 1
            else:
                return gradeStripped
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print ("Usage: python GPACalculator.py")
    else:
        GPACalculator = GPACalculator()
        print('Please note you can exit the program at any time by entering "quit"')
        numClassesInt = GPACalculator.promptNumClasses()
        print(str(numClassesInt))
        gradesAndCredits = []
        for x in range(numClassesInt):
            creditsInt = GPACalculator.promptCredits(x)
            gradeStripped = GPACalculator.promptGrade(x)
            gradesAndCredits.append((creditsInt, gradeStripped))
        gpa = GPACalculator.calculate(gradesAndCredits)
        print("Your gpa is: " + str(gpa))
