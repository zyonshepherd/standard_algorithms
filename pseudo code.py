BEGINTASK
    program = true
    WHILE  program == 'true':
        choice = Get input " Type 'l' to load a number into the Array\n Type 'p' to print the Array\n Type 's' to sum the numbers in the Array\n Type 'min' for minimum number\n Type 'max' for maximum number\n Type 'q' to quit\n"
        CASEWHERE choice is
            l: loadArray()
            p: printArray()
            s: sumArray()
            min: minimumArray()
            max: maximumArray()
            q: program = false
            
        ENDCASE
    ENDWHILE
ENDTASK

BEGIN loadArray()
    arrayExit = ' '
    WHILE arrayExit != '':
        TRY:
            arrayNum = int input "Enter a number or press enter to go back: "
        EXCEPT ValueError:
            print "This is not an integer"
            arrayExit = ''
        append arrayNum to theArray
        print "Numbers is array are", theArray
    END WHILE
END loadArray
   
BEGIN printArray()
    print theArray
    print 'number of elements in array is' numElements
END printArray

BEGIN sumArray()
    numberSum = sum(theArray)
    print "The total sum of these numbers is:" number sum
END sumArray

BEGIN minimumArray()
    print "Minimum number of array is called"
END minimumArray

BEGIN maximumArray()
    print "Maximum number of array is called"
END maximumArray
