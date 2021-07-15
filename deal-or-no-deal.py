import copy
import math
import os
import random as random

def clear():
    os.system('clear')
    os.system('cls')

caseNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
prizes = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

def getCases():
    newCaseNumbers = copy.deepcopy(caseNumbers)
    random.shuffle(newCaseNumbers)
    return dict(zip(newCaseNumbers, prizes))

cases = getCases()
gameRound = 1
caseSelectionsRemaining = 0
selectedCaseNumber = 0
currentCaseNumber = 0
selectedCasePrize = 0
firstSelection = True

def printRemainingCases():
    print("You have case " + str(selectedCaseNumber) + ".\n")
    print("\nCases Remaining:")
    print("----------------\n")
    cases = ""
    for caseNumber in caseNumbers:
        cases += str(caseNumber) + ", "
    
    print(cases[:-2])

def printRemainingPrizes():
    print("\nPrizes Remaining:")
    print("----------------\n")
    for prize in prizes:
        print("$" + str(prize))

def printRemainingInformation():
    printRemainingCases()
    printRemainingPrizes()

def printSelectedCaseInformation():
    global firstSelection
    global caseNumbers

    if firstSelection:
        caseNumbers.remove(int(selectedCaseNumber))
        firstSelection = False
    else:
        selectedCasePrize = cases[int(currentCaseNumber)]
        caseNumbers.remove(int(currentCaseNumber))
        print("\nCase " + currentCaseNumber + " contained $" + str(selectedCasePrize) + "!\n")
        prizes.remove(selectedCasePrize)
    clear()

def bankOffer():
    global gameRound

    bankOffer = 0
    for prize in prizes:
        bankOffer += prize
    bankOffer = bankOffer / len(prizes)

    if gameRound == 1:
        bankOffer = bankOffer * 0.1
    if gameRound == 2:
        bankOffer = bankOffer * 0.2
    if gameRound == 3:
        bankOffer = bankOffer * 0.3
    if gameRound == 4:
        bankOffer = bankOffer * 0.5
    if gameRound == 5:
        bankOffer = bankOffer * 0.65
    if gameRound >= 6:
        bankOffer = bankOffer * 0.8

    printRemainingPrizes()
    print("\nThe bank has offered you $" + str(int(bankOffer)) + " for your case. \n\nDeal, or No Deal?")
    deal = input()

    if deal.lower() == "deal":
        gameReveal(bankOffer)
        exit()
    else:
        clear()
        print("No Deal! Let's continue!")
    gameRound = gameRound + 1

def finalBankOffer():
    bankOffer = 0
    for prize in prizes:
        bankOffer += prize
    bankOffer = bankOffer / len(prizes)

    printRemainingInformation()
    print("\nThe bank has offered you $" + str(int(bankOffer)) + " for your case. \n\nDeal, or No Deal?")
    deal = input()

    if deal.lower() == "deal":
        gameReveal(bankOffer)
    else:
        clear()
        print("\nYou declined the final bank offer of $" + str(int(bankOffer)) + "!\n")
        print("Was it a good deal? You decide- here's what was remaining:\n")
        print("You decided to keep case " + str(selectedCaseNumber) + ", which had $" + str(cases[int(selectedCaseNumber)]) + " inside it.\n")

    for caseNumber in caseNumbers:
        print("Case " + str(caseNumber) + " had $" + str(cases[int(caseNumber)]))

    print("\nThanks for playing!")
    exit()

def setCaseSelections():
    global caseSelectionsRemaining

    if gameRound == 1:
        caseSelectionsRemaining = 5
    if gameRound == 2:
        caseSelectionsRemaining = 4
    if gameRound == 3:
        caseSelectionsRemaining = 3
    if gameRound == 4:
        caseSelectionsRemaining = 2
    if gameRound >= 5:
        caseSelectionsRemaining = 1

def gameReveal(bankOffer):
    clear()
    print("\nYou accepted the bank offer of $" + str(int(bankOffer)) + "!\n")   
    print("Was it a good deal? You decide- here's what was remaining:\n")
    print("You had case " + str(selectedCaseNumber) + ", which had $" + str(cases[int(selectedCaseNumber)]) + " inside it.\n")
    for caseNumber in caseNumbers:
        print("Case " + str(caseNumber) + " had $" + str(cases[int(caseNumber)]))

    print("\nThanks for playing!")
    exit()
    

def dealOrNoDeal():
    global currentCaseNumber
    global caseSelectionsRemaining
    global selectedCaseNumber

    print("\nWelcome to deal or no deal!\n")
    print("We're going to assume that you're familiar with the rules of the game and continue without an explanation of them.\n")
    print("We'll start by having you pick your case. Choose a number between 1 and 26: ")

    selectedCaseNumber = input()
    setCaseSelections()

    while True:
        printSelectedCaseInformation()

        if len(caseNumbers) == 1:
            finalBankOffer()
            exit()

        if caseSelectionsRemaining == 0:
            bankOffer()
            setCaseSelections()
        
        printRemainingInformation()
        print("\nYou must choose " + str(caseSelectionsRemaining) + " more case(s). Which case would you like to choose next? ")
        caseSelectionsRemaining = caseSelectionsRemaining - 1
        currentCaseNumber = input()

dealOrNoDeal()