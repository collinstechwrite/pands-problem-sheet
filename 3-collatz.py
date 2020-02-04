"""
This program asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and,
if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.
"""

import sys #import sys module can be used to terminate program

def number_calculation(user_input):
    """Help doc info for number_calculation, this function performs calculation on number input by the user
    if it is even, divide it by two, but if it is odd, multiply it by three and add one.
    Have the program end if the current value is one."""
    try:
        user_input = int(user_input)

        while user_input != 1: #instruction telling program to end when calculated number = 1
            if user_input % 2 == 0: #checks to see if number is even
                print(round(user_input,ndigits=None)) #prints current number removing decimal point so user can see flow of calculations
                user_input = user_input / 2 #if number is even divides number by two

            else: #by default if number is not even then else deals as an odd number
                print(round(user_input,ndigits=None)) #prints current number removing decimal point so user can see flow of calculations
                user_input = (user_input * 3) + 1 #if number is odd multiplies it by three and adds one.
  
        print(round(user_input,ndigits=None)) #prints 1 on exiting the while loop
        play_again() #activates function play_again to offer user choice of whether they want to play again.

    except:
        print("Type Error")
        play_again()
        

def play_again():
    """Help doc info for play_again, this function checks whether user wants to play again"""
    choose = input("Do you want to play again? Type YES or NO:")
    while choose != "YES" or "NO":
        if choose == "YES":
            play()
        elif choose == "NO":
            sys.exit("Exiting program")
        else:
            choose = input("Do you want to play again? Type YES or NO:")



print("""This program requires you to input a number.
If it is even it will divide it by two, but if it is odd it will multiply it by three and add one.
The program will continue to perform this calculation until it reaches value of one.""") #first instruction user sees explaining the program


def play():
    """Help doc info for play, this function is the first function that the program loads and it performs checks on the users input data to insure that positive number is greater than 0"""
    try: 
        user_input = int(input("Input any positive integer:"))   #int() ensures that program is looking for an integer  
        if user_input <= 0: #ensures user input is greater than zero
            print("You must write a positive number greater than zero:")
            play()
        else: #conditions are met then program activates function number_calculation
            number_calculation(user_input)
    except: #if an integer is not found the program will give user an error message
        print("Error: You must enter a number value")
        play()

play() #activates the play function when programm is first loaded
