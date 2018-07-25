""" Short, one line description of the module ending with a period.
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Your Name"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "your.address@education.nsw.com.au"
__status__ = "Prototype, Development or Production"


#dependencies
import turtle as T
import math as M

#subroutines
def drawSquare(turtle, length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    
def drawCircle(turtle, radius):
    turtle.circle(radius)
    
def drawTriangle(turtle, length):
    print("not yet implemented :(")
    
def areaSquare(length):
    return length * length

def areaCircle(radius):
    return M.pi * radius * radius

def areaTriangle(length):
    return 0.433 * length * length
    
# initial setup
fred = T.Turtle()
cont = True

#main loop
while cont: 
    shape = input("what shape would you like to draw? C - circle, S - square, T - triangle, Q - quit: ")
    shape = shape.lower() #force to lower case in case user didn't use caps
    if shape == "q":
        cont = False
        T.bye() #closes the turtle window
    elif shape in "cst": #see if a valid choice was made
        size = input("What size would you like it? ")
        
        if size.isnumeric(): #check that the text entered is a number
            size = eval(size) #change to a number
            if shape == "c":
                drawCircle(fred, size)
                area = areaCircle(size)
                
            elif shape == "s":
                drawSquare(fred, size)
                area = areaSquare(size)
            
            elif shape == "t":
                drawTriangle(fred, size)
                area = areaTriangle(size)
                
            
        area = int(area)
        print("the area is {}".format(area))
    else:
        print("not a valid entry")
        
    

