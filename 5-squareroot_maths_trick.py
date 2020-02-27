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

print("There are many different ways to analyse square root")
myinput = input("Please enter a positive number e.g. 14.5:") #ask user for input

print("____________________ \n")
print("PYTHON MATH FUNCTION \nThe most accurate method is Python square root function from the math module\n")


print("When you use python math.sqrt the square root of", myinput, "is approx." , sqrt(myinput),"\n\n")

print("Below are some other methods")



"""https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo"""

def mySqrt(x):

    r = x
    precision = 10 ** (-10)
    
    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
        
    return r

print("When you use the Newton method as per https://hackernoon.com ", myinput, "is approx." , mySqrt(int(myinput)),"\n\n")


"""This Square Root Calculator is based on this maths trick
https://www.youtube.com/watch?v=nUyLnjgGumg 
I borrowed and edited this code to find closest number
https://stackoverflow.com/questions/36275459/find-the-closest-elements-above-and-below-a-given-number"""


from collections import OrderedDict
try:
    myvariable = int(myinput)

    #take far right character
    farrightcharacter = str(myvariable)
    farrightcharacter2 = farrightcharacter[-1]
    farrightcharacterint = int(farrightcharacter2)

    #take the far left 2 characters
    myfirstanalysis = str(myvariable)
    myfirstanalysis2 = myfirstanalysis[0:2]
    myfirstanalysisint = int(myfirstanalysis2)

    # yellow magic numbers
    yellowmagic = {
        1:1,
        2:4,
        3:9,
        4:6,
        5:5,
        6:6,
        7:9,
        8:4,
        9:1,
    }

    # reference by nearest square root
    data = {
        1:1,
        2:4,
        3:9,
        4:16,
        5:25,
        6:36,
        7:49,
        8:64,
        9:81,
    }

    def find_closer():
        global myinput

 

        print("YOUTUBE: SQUARE ROOT IN 3 SECONDS - MATH TRICK https://www.youtube.com/watch?v=nUyLnjgGumg\n")
        if len(myinput) > 4 or len(myinput)<= 2:
            print("The method below becomes unreliable with input greater than 4 digits or less than 2 digits")


        # reference by nearest square
        data2 = {
            1:1,
            4:2,
            9:3,
            16:4,
            25:5,
            36:6,
            49:7,
            64:8,
            81:9,
        }

        a = [1, 4, 9, 16, 25, 36, 49, 64, 81]
        b = myfirstanalysisint #EDITED TO TAKE MY VARIABLE
        # diff_list = []
        diff_dict = OrderedDict()
        if b in a:
            findroot = data2[myfirstanalysisint] #findroot
        else:
            for x in a:
                diff = x - b
                if diff < 0:
                    # diff_list.append(diff*(-1))
                    diff_dict[x] = diff*(-1)
                else:
                    # diff_list.append(diff)
                    diff_dict[x] = diff
        """print("diff_dict", diff_dict)"""
        # print(diff_dict[9])
        sort_dict_keys = sorted(diff_dict.keys())
        """print(sort_dict_keys)"""
        closer_less = 0
        closer_more = 0
        for closer in sort_dict_keys:
            if closer < b:
                closer_less = closer
                findroot = data2[closer_less] #findroot
            else:
                closer_more = closer
                break


        



        print("Analysing: ", myvariable) #number being analysed
        print("____________________ \n")

        print("Analysing smallest number on the right: ", farrightcharacterint) #far right character


        yellowlist = []

        for k,v in yellowmagic.items():
            if v == farrightcharacterint:
                yellowlist.append(k)
        print("stored: ", yellowlist)

        if findroot * (findroot + 1) < myvariable:
            print("use smaller number")
            print(min(yellowlist))

        if findroot * (findroot + 1) > myvariable:
            print("use bigger number")
            print(max(yellowlist))
        

        print("____________________ \n")
        
        print("Analysing greatest number on the left: ", myfirstanalysisint) #first two left digits
     
        print("closest square less or equal to =", myfirstanalysisint, " is ", closer_less)    
        print(findroot)


        print("____________________ \n")

        if findroot * (findroot + 1) < myvariable:
            print("The square root is")
            print(str(findroot) + str(min(yellowlist)))

        if findroot * (findroot + 1) > myvariable:
            print("The square root is")
            print(str(findroot) + str(max(yellowlist)))

    find_closer()

except ValueError: #use of error handling to prompt user to enter number
    print("YOUTUBE: SQUARE ROOT IN 3 SECONDS - MATH TRICK https://www.youtube.com/watch?v=nUyLnjgGumg\n doesn't work with decimal points") 



