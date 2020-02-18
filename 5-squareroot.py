"""squareroot.py is a program that takes a positive floating-point number as input and outputs an approximation of its square root.
it achieves this by use of a function called sqrt. An output example would be The square root of 14.5 is approx. 3.8."""

import math #import math module to access square root calculation

def sqrt(myinput):
    """sqrt function takes and validates a user number input and finds approximate square root to nearest 1 decimal point utilizing and rounding math sqrt function"""
    while True: #use of while loop with exception handling to ensure user inputs either a float or an integer
        try:
            myinput = float(myinput) #convert input from string to a float, as want to initially make it possible for input to accept int or float input
            myresult = round(math.sqrt(myinput),1) #combining round function to just return maximum of one decimal place from calculated square root
            break
        except ValueError: #use of error handling to prompt user to enter number
            print("Not a valid number! Please try again ...") 
            myinput = input("Please enter a positive number e.g. 14.5") #ask user for input
    return myresult

myinput = input("Please enter a positive number e.g. 14.5:") #ask user for input
print("The square root of", myinput, "is approx." , sqrt(myinput))

                
