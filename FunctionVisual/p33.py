#Joseph Mucciaccio
#This program reads a mathematical function that uses a parameter, domain, and number of samples and outputs a list of
#of elements within the sample number inputed by the user

import math
import matplotlib.pyplot as plt

def displaylist_and_plot(fun_str, domain, ns):
    even_interval = (domain[1] - domain[0]) / ns
    xs = []
    #length = len(xs)
    
    for index in range(ns):
        xs.append(domain[0] + even_interval * index)
    ys = []
    for x in xs:
        y = eval(fun_str)
        ys.append(y)
    for index in range(len(xs)):
        print('{:8.4f}\t{:8.4f}'.format(xs[index],ys[index]))

    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.plot(xs, ys)
    plt.show()


fun_str = input("Enter function with variable x: ")
ns = int(input("Enter number of samples: "))
xmin = float(input("Enter x-min value: "))
xmax = float(input("Enter x-max value: "))


print("    x                y")
print("------------------------")

domain = xmin, xmax
    
displaylist_and_plot(fun_str, domain, ns)