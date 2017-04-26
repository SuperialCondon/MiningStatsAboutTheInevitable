import csv

from Tkinter import Tk
from tkFileDialog import askopenfilename



def calculateCSV():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    fileUse = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(fileUse)
    #userFile = raw_input("Please enter a file name: ")
    #fileUse = userFile + ".csv"
    with open(fileUse,'r') as filename:
        userCode = raw_input("Please enter a Icd10Code(s) seperated by commas: ")
        actualUserCode = userCode.upper()
        listOfCodes = actualUserCode.split(',')
        counter = 0
        for line in filename:
            lineList = line.split(',') #Loop through file to find the corresponding death code(s) and count how many appear in dataset
            for code in listOfCodes:
                if(lineList[24] == code):
                    counter+= 1
    return counter

print calculateCSV()