#Parser for extracting information from the user input like 54x+67y=22
#---------------------------------------------------------------------
###CURRENTLY WORKING ON:###
#-Distributing?
#-Sorting variables in alphabetical order - FINISHED
#-Combine like terms
#---------------------------------------------------------------------

def sort(variables, row):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    sortedVariables = []
    save = ""
    i = 0
    
    #Loop through each letter in alphabet
    for x in alphabet:
        #If the letter in the alphabet is in our variables
        if (x in variables):
            #Add it to sortedVariables list
            sortedVariables.append(x)
            if (sortedVariables[i] != variables[i]):
                #Find the position of the wrong order letter
                variablesPos = variables.index(sortedVariables[i])
                #Swap the numbers corresponding to the letters
                save = row[i]
                row[i] = row[variablesPos]
                row[variablesPos] = save
                
                #Swap the variables as well
                save = variables[i]
                variables[i] = variables[variablesPos]
                variables[variablesPos] = save

            i += 1
    

def parse(equation):
    allowed = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "."]
    notAllowed = ["+", "-", "=", "*", "(", ")"]
    numbers = [""]
    row = [0]
    variables  = []
    fractionPos = firstDigitPos = -1
    i = 0
    equation += "|"

    #Go through each single character in the string
    for x in range(len(equation)):
        #If it is a digit or a decimal then add it to a new string to be considered one number
        if (equation[x] in allowed):
            #If there is a fraction, set fraction boolean to true so we can simplfy the fraction later
            if (equation[x] == "/"):
                fractionPos = x
            #Add the digit to the number
            numbers[i] += equation[x]
            #If it is the first digit, we save the position of that digit
            if (firstDigitPos == -1):
                firstDigitPos = x
        elif (equation[x] not in allowed):
            #If it is a variable
            if (equation[x] not in notAllowed):
                #If there is no number in front of a variable, put a 1
                if (numbers[i] == ""):
                    numbers[i] = "1"
                    
                #As long as it is NOT our special character
                if (equation[x] != "|"):
                    variables.append(equation[x])
                    #Append empty string to numbers list for every variable
                    numbers.append("")
                    #Add more elements to row list for next number
                    row.append(0) 
                    
                #When there is a variable, that means the number before it, is already entered, so now simplfy if fractions
                if (fractionPos >= 0):
                    row[i] = float(equation[firstDigitPos:fractionPos]) / float(equation[fractionPos+1:x])
                    #Reset frac position
                    fractionPos = -1
                else:
                    #Convert the string from numbers list to row list
                    row[i] = float(numbers[i])
          
                #If negative add it to the number
                if (firstDigitPos >= 0 and equation[firstDigitPos-1] == "-" or equation[x-1] == "-"):
                    row[i] = -1 * row[i]
                #Increment for us to get the numbers list ready to store next number
                i += 1
                
                #Reset start since this is only ran when we encounter a variable... get ready for next start
                start = False
                firstDigitPos = -1
                
        
     #Sort variables in alphabetical order with same changes applied to their respective number
    sort(variables, row)
    print(variables)
    return row

#------------------------------------------------
#MAIN BELOW

equation = input()
print(parse(equation))
