import sys

#sub routine
def loadArray():
    arrayExit = ' '
    while arrayExit != '':
        try:
            arrayNum = int(input("Enter a number or press enter to go back: "))
        except ValueError:
            print("This is not an integer!")
            arrayExit = ''
        theArray.append(arrayNum)
        print("Numbers in array are", theArray,"\n")
    
    
def printArray():
    outString = "" 
    for n in theArray: 
        outString = outString + str(n) + " " 
    print(outString) 
    numElements = len(theArray) 
    print("there are {} elements in the array\n".format(numElements)) 

    
def sumArray():
    numberSum = sum(theArray)
    print("The total sum of these numbers is:", numberSum, "\n")
    
def minimumArray():
    print("Minimum number of array is called\n")

def maximumArray():
    print("Maximum number of array is called\n")

def quitArray():
    print("\nGoodbye")
    program = 'false'


#main routine
program = 'true'
theArray = []
while program == 'true':
    
    choice = input(" Type 'l' to load a number into the Array\n Type 'p' to print the Array\n Type 's' to sum the numbers in the Array\n Type 'min' for minimum number\n Type 'max' for maximum number\n Type 'q' to quit\n")

    if choice == 'l':
        loadArray()
    elif choice == 'p':
        printArray()
    elif choice == 's':
        sumArray()
    elif choice == 'min':
        minimumArray()
    elif choice == 'max':
        maximumArray()
    elif choice == 'q':
        program = 'false'
    else:
        print("Invalid input")

    
    
