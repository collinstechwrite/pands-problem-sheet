findsquareroot = input("input number you wish to find the square root of")
abc = int(findsquareroot)


"""
My square root guess
"""

mysquarerootguesses = len(str(abc))
use="1"

for i in range(1,mysquarerootguesses):
    if i == 1:
        pass
    else:
        use = use + "0"



mysquarerootguess = float(use)


checkingapossible_squareroot = mysquarerootguess ** 2

while checkingapossible_squareroot  < abc:
    checkingapossible_squareroot = (mysquarerootguess + 0.01) ** 2
    mysquarerootguess = mysquarerootguess + 0.01
    print(mysquarerootguess)

print(mysquarerootguess)
print(mysquarerootguesses)


print(use)
