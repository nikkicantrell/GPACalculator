import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import GPACalculator

class window(QWidget):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)

        self.layout = QFormLayout()

        self.getNumClasses()
        self.openClassesWindow()

        self.setWindowTitle("GPA Calculator App")
        self.setLayout(self.layout)
    def getNumClasses(self):
        numClasses, ok = QInputDialog.getInt(self, "integer input dialog", "Enter # of classes")
        if ok:
            self.numClasses = numClasses
    def openClassesWindow(self):
        self.creditsLes = []
        self.gradesLes = []
        for x in range(self.numClasses):
            self.layout.addRow("Class #" + str(x + 1), None)
            creditsle = QLineEdit()
            creditsValidator = QRegExpValidator(QRegExp("[12345678]"), self)
            creditsle.setValidator(creditsValidator)
            creditsle.setAlignment(Qt.AlignRight)
            self.creditsLes.append(creditsle)
            self.layout.addRow("# credits:", creditsle)
            gradele = QLineEdit()
            gradeValidator = QRegExpValidator(QRegExp("[ABCDFabcdf]"), self)
            gradele.setValidator(gradeValidator)
            gradele.setAlignment(Qt.AlignRight)
            self.gradesLes.append(gradele)
            self.layout.addRow("letter grade:", gradele)
        enterButton = QPushButton()
        enterButton.setText("Calculate GPA")
        enterButton.clicked.connect(self.calculateGPA)
        self.layout.addRow(enterButton)

    def calculateGPA(self):
        creditsAndGrades = []
        for x in range(len(self.creditsLes)):
            creditsAndGrades.append((self.creditsLes[x].text().toInt()[0], str(self.gradesLes[x].text()).upper()))
        self.gpa = GPACalculator.GPACalculator().calculate(creditsAndGrades)
        self.openGPAWindow()
    def openGPAWindow(self):
        for x in range(len(self.creditsLes)):
            self.creditsLes[x].clear()
            self.gradesLes[x].clear()
        gpaMsgBox = QMessageBox()
        gpaMsgBox.setText("Your gpa is: " + str(self.gpa))
        gpaMsgBox.addButton(QMessageBox.Ok)
        gpaMsgBox.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())
