import json

# Sukhamrit Singh
# Birthday Look Up Assignment

# path to find the JSON file
pathToFile = './src/birthday.json' 

# opening the JSON file
with open(pathToFile, 'r') as openfile: 
    # Reading from json file 
    birthdayJSON = json.load(openfile) 

# Boolean to keep the loop running
keepSearching = True

# Loop to keep running and prompting user
while keepSearching == True:

    # Prompting User to Put Name
    userInput = input("\nPlease enter your first or last name or enter 'q' to exit: ")

    # If user enters "q" then terminates program
    if (userInput == 'q'):
        keepSearching = False
        break

    # Variable to get number of matches for inputed name
    matchFound = 0
    print("")

    # loop json list of data and put each name into a dictionary
    for record in birthdayJSON:

        # fetch name and birthday
        name = record["name"]
        birthday = record["birthday"]

        # Spliting up name into first and last name
        nameArray = name.split(" ")
        firstName = nameArray[0]
        lastName = nameArray[1]

        # Booleans to check if first or last name match
        fnameMatch = False
        lnameMatch = False

        # Turing both name and user input into upper case
        #Checking if the input matches the first or last name
        if ( userInput.upper() == firstName.upper() ):
            fnameMatch = True
        
        if ( userInput.upper() == lastName.upper() ):
            lnameMatch = True

        # If statement to check input
        if ( fnameMatch or lnameMatch) :
            # Returns birthday if in list
            matchFound += 1
            print("\t" + name + "'s Date of Birth is: " + birthday)
    
    # If no matches print error message
    if ( matchFound == 0):
        print("\tSorry no record found for this name")