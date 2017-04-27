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

def calculateTotalPercentage(arrayOfTotalDeaths):
    updatedArray = []
    for statistic in arrayOfTotalDeaths:
        updatedArray.append((statistic / 6000)) #The 6000 would be changed to the total number of deaths from the dataset
    return updatedArray

def subMain():
    alzheimers = calculateCSV()
    parkinsons = calculateCSV()
    septcemia = calculateCSV()
    #print alzheimers #g309,g318
    #print parkinsons #g20
    #print septcemia #a40
    arrayOfDeathsFromSet = [alzheimers,parkinsons,septcemia]
    percentagesOfDeaths = calculateTotalPercentage(arrayOfDeathsFromSet) #This works but it wont print numbers less than 1, so anything from 0 to 0.99999999 it keeps rounding to 0
    #blanking on how to fix, but once fixed we could calculate the percentage of total deaths to match the cdc pdf.
    print percentagesOfDeaths

subMain()
