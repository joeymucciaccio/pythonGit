#Joseph Mucciaccio
import matplotlib
import math


p = 0

print("Quadratic Formula Calulator")
while (True):

    a = float(input("Enter a value for 'a' (or Enter '0' to stop the program): "))
    #used to end the program
    if a == 0:
        print("program ended")
        break
    
    b = float(input("Enter a value for 'b': "))
    c = float(input("Enter a value for 'c': "))
 
    D = (b**2) - 4*a*c
    
    #different values for D
    if D < 0:
        print("No real solution")
        continue
    
    if D == 0:
        #if there is one solution, calculate x1       
        x1 = (-b) / (2 * a)
        print("The solution is ", x1)
        
    if D > 0:
        #if there are two solutions, calculate both x's
        x1 = ((-b) + math.sqrt(D))/(2 * a)
        x2 = ((-b) - math.sqrt(D))/(2 * a)
        print("The solutions are ", x1, " & ", x2)
   
    #put xs and ys into an empty list
    xs = []
    ys = []

    i = -5.0
    
    #nested while loop
    while i < 5.0:
        
        x = i
  
        #append values to xs and ys
        xs.append(x)
        ys.append(a * (x**2) + (b * x) + c)

        #used to get next floating point number (one of the 100)
        i = float('%.1f'%(i + 0.1))
  
    #plot the function line 
    matplotlib.pyplot.plot(xs, ys, "b.")
    matplotlib.pyplot.xlabel("x")
    matplotlib.pyplot.ylabel("y")
  
    #title for each graph string
    title = "Figure " + str(p)
  
    matplotlib.pyplot.title(title)
  
    #this is used to show the plot
    matplotlib.pyplot.show()
  
    p = p + 1    
