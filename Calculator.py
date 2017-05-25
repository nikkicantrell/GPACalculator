import sys

class Calculator(object):

    def __init__(self):
        pass
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print ("Usage: python calculator.py")
    else:
        numClasses = raw_input("How many classes do you have? ")
