import sys

class FinalCalculator(object):
    def __init__(self):
        pass
    def calculateFinal(self, percentagesAndGrades):
        """Calculates final grade"""
        finalGrade = 0
        for x in range(len(percentagesAndGrades)):
            percentage = percentagesAndGrades[x][0]/100
            grade = percentagesAndGrades[x][1]
            finalGrade += percentage*grade
        return finalGrade

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python FinalCalculator.py")
    else:
        print('Please note you can exit the program at any time by entering "quit"')
        while True:
            try:
                numSections = raw_input("How many sections of the class are there? ")
                numSectionsInt = int(numSections)
            except ValueError:
                if numSections == "quit":
                    sys.exit()
                print("Sorry your answer is not valid. Please enter a number.")
            else:
                break
        percentagesAndGrades = []
        for x in range(numSectionsInt):
            while True:
                try:
                    percentage = raw_input("What perecentage is section#" +
                                           str(x+1) + " worth(out of 100)? ")
                    percentageFloat = float(percentage)
                except ValueError:
                    if credits == "quit":
                        sys.exit()
                    print("Sorry your answer is not valid. Please enter a number.")
                else:
                    #To catch if the user accidentally makes the percentage out of 1
                    if (percentageFloat < 1):
                        print("Sorry your answer is not valid. Please enter a" +
                              " number greater than 1")
                    else:
                        break
            while True:
                try:
                    grade = raw_input("What grade do you have in section #" +
                                      str(x) + " (out of 100)? ")
                    gradeFloat = float(grade)
                except ValueError:
                    if grade == "quit":
                        sys.exit()
                    print("Sorry your answer is not valid. Please enter a number.")
                else:
                    #To catch if the user accidentally makes the grade out of 1
                    if (gradeFloat < 1):
                        print("Sorry your answer is not valid. Please enter a" +
                              " number greater than 1")
                    else:
                        break
            percentagesAndGrades.append((percentageFloat, gradeFloat))
        finalCalculator = FinalCalculator()
        finalGrade = finalCalculator.calculateFinal(percentagesAndGrades)
        print("Your final grade is: " + str(finalGrade))
