def sqrt(findsquareroot):

    """
    My square root guess
    this part of code is used to reduce iterations
    """
    
    mysquarerootguesses = len(str(findsquareroot))

    use="1"

    for i in range(1,mysquarerootguesses):
        if i == 1:
            pass
        else:
            use = use + "0"

    mysquarerootguess = float(use)


    print("my starting guess " , mysquarerootguess)

    if (mysquarerootguess ** 2) > findsquareroot:
        mysquarerootguess = mysquarerootguess / 4
    

    while (mysquarerootguess  ** 2) < (findsquareroot-2):
        mysquarerootguess += 1
        print(mysquarerootguess)
    print("beginning second while loop")

    while abs((findsquareroot-0.1)-mysquarerootguess) < 0.1:
        mysquarerootguess += 0.01
        print(mysquarerootguess)



findsquareroot = int(input("input number you wish to find the square root of"))
print(sqrt(findsquareroot))





