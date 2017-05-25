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
    def calculateNeeded(self, percentage, wanted, percentagesAndGrades):
        """Calculates what grade is needed to get a certain final grade"""
        currentGrade = self.calculateFinal(percentagesAndGrades)
        needed = 0
        if wanted == "A":
            needed = 90 - currentGrade
        elif wanted == "B":
            needed = 80 - currentGrade
        elif wanted == "C":
            needed = 70 - currentGrade
        else:
            needed = 60 - currentGrade
        return (needed/percentage)*100
if __name__ == "__main__":
    if len(sys.argv) > 1:
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
        while True:
            try:
                function = raw_input("Enter 1 for a final grade calculator, or " +
                                     "2 for calculating what you need on a section ")
                functionInt = int(function)
            except ValueError:
                if function == "quit":
                    sys.exit()
                print("Sorry your answer is not valid. Enter 1 or 2")
            else:
                if functionInt != 1 and functionInt != 2:
                    print("Sorry your answer is not valid. Enter 1 or 2")
                else:
                    break
        if functionInt == 2:
            while True:
                try:
                    percentageLast = raw_input("What perecentage is the section" +
                                               " you are looking to find out the" +
                                               " needed grade for? ")
                    percentageLastFloat = float(percentageLast)
                except ValueError:
                    if percentageLast == "quit":
                        sys.exit()
                    print("Sorry your answer is not valid. Please enter a number.")
                else:
                    #To catch if the user accidentally makes the percentage out of 1
                    if (percentageLastFloat < 1):
                        print("Sorry your answer is not valid. Please enter a" +
                              " number greater than 1")
                    else:
                        break
            while True:
                wanted = raw_input("What final grade do you want to get in the class" +
                                   " (A, B, C, D)? ")
                if wanted != "A" and wanted != "B" and wanted != "C" and wanted != "D":
                    if numSections == "quit":
                        sys.exit()
                    print("Sorry your answer is not valid. Please enter one of" +
                          " the follow: A, B, C, D")
                else:
                    break
            #so the next part asks for one less of the sections
            numSectionsInt -= 1
        percentagesAndGrades = []
        for x in range(numSectionsInt):
            while True:
                try:
                    percentage = raw_input("What perecentage is section#" +
                                           str(x+1) + " worth(out of 100)? ")
                    percentageFloat = float(percentage)
                except ValueError:
                    if percentage == "quit":
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
        if functionInt == 1:
            finalGrade = finalCalculator.calculateFinal(percentagesAndGrades)
            print("Your final grade is: " + str(finalGrade))
        else:
            neededGrade = finalCalculator.calculateNeeded(percentageLastFloat,
                                          wanted, percentagesAndGrades)
            print("You need a " + str(neededGrade) + " to keep a " + wanted)
