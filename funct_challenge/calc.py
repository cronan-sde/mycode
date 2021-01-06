#!/usr/bin/env python3

"""
    Author: Cody Cronberger
    simple program that takes 2 number inputs and an operator input eg. +,-,/,*
    and returns the value of the calculation of those numbers with the operator

"""

#get user input 2 numbers, 1 operator
def getUserData():
    operators = ["+", "-", "/", "*"]
    calcToBeMade = []
    while len(calcToBeMade) < 3:
        if len(calcToBeMade) < 2:
            inputNumStr = "Enter the first number: " if len(calcToBeMade) < 1 else "Enter the second number: "
            try:
                numInput = float(input(inputNumStr))
                calcToBeMade.append(numInput)
            except:
                print("Please Enter a valid number")
        else:
            opInput = input(f"Enter the operator for the calculation you'd like, {operators} ").strip()
            if opInput in operators:
                calcToBeMade.append(opInput)
            else:
                print(f"Please enter one of the following from this list - {operators}\n")

    calculate(calcToBeMade)
    calcAgain()



#calculate value of user input
def calculate(calcList):
    num1 = calcList[0]
    num2 = calcList[1]
    op = calcList[-1]
    res = 0

    if op == "+":
        res = num1 + num2
    elif op == "-":
        res = num1 - num2
    elif op == "*":
        res = num1 * num2
    elif op == "/":
        if num2 == 0:
            res = "Cannot divide by zero"
        else:
            res = num1 / num2

    print(f"The value of {num1} {op} {num2} = {res}\n")


#ask if user wants to do another calculation or quit
def calcAgain():
    while True:
        again = input("Would you like to calculate some more? (y/n) ").strip().lower()
        if again == "y":
            getUserData()
            break
        elif again == "n":
            break
        else:
            print(f"Please type either y or n, {again} is not a valid input")

#call method to start program
getUserData()

#exit program
print("Exiting program")
