#imports needed for plotting graph
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import random

"""
homework was to implement the following as a graph
f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]
I understand f,g,h to be 3 separate functions calling a number in the range 0-4
"""

#create variables to store results of graph before use of function
graph_value_1 = ""
graph_value_2 = ""
graph_value_3 = ""

def f(x):
    global graph_value_1 #use global to reference and change variables outside of the function
    graph_value_1 = x


def g(x):
    global graph_value_2
    graph_value_2 = x * 2



def h(x):
    global graph_value_3
    graph_value_3 = x * 3


#this gets a random x value in the range 0 to 4
x = random.randrange (0,5,1)

#f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]
#these functions call x and return new values to a,b,c 
f(x)
g(x)
h(x)

#these are titles shown at the bottom of the graph
objects = ('f = x \n' + str(x), 'g = x * 2 \n' + str(x * 2), 'h = x * 3 \n' + str(x * 3))

y_pos = np.arange(len(objects))


my_data = [graph_value_1,graph_value_2,graph_value_3]

plt.bar(y_pos, my_data, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number')
plt.title('f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]\n random x = ' + str(x))
plt.show()







