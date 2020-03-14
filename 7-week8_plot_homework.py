#imports needed for plotting graph
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import random

#f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]

#create return variable for the bar graph
a = ""
b = ""
c = ""

def f(x):
    global a
    x = x
    a = x


def g(x):
    global b
    x = x * 2
    b = x


def h(x):
    global c
    x = x * 3
    c = x

#this gets a random x value in the range 0 to 4
x = random.randrange (0,5,1)

#these functions call x and return new values to a,b,c 
f(x)
g(x)
h(x)


objects = ('f = x', 'g = x * 2', 'h = x * 3')
y_pos = np.arange(len(objects))
performance = [a,b,c]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number')
plt.title('x = ' + str(x))
plt.show()







