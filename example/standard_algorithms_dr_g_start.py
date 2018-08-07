def loadArray(thisArray):
    print("loadArray was called")

def printArray(thisArray):
    outString = ""
    for n in thisArray:
        outString = outString + str(n) + " "
    print(outString)
    numElements = len(thisArray)
    print("there are {} elements in the array".format(numElements))

def sumArray():
    pass



#Main
theArray = [1,2,3,4,5]
choice = input("do you want to Add numbers to the array, Print the array or Sum the array: ")
if choice == 'a':
    loadArray(theArray)
elif choice == "p":
    printArray(theArray)
elif choice == 's':
    sumArray()
    
    
