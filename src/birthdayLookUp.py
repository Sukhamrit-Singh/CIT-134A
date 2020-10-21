import json

# Sukhamrit Singh
# Birthday Look Up Assignment

# path to find the JSON file
pathToFile = './src/birthday.json' 

# opening the JSON file
with open(pathToFile, 'r') as openfile: 
  
    # Reading from json file 
    birthdayJSON = json.load(openfile) 

# HashMap to store data
birthdayDictionary = {}

# loop json list of data and put each name into a dictionary
for record in birthdayJSON:

    # fetch name and birthday
    name = record["name"]
    birthday = record["birthday"]

    # Getting Birthday for the name
    birthdayDictionary[name] = birthday

# Prompting User to Put Name
userInput = input("Please enter your name: ")

# If statement to check input
if (userInput in birthdayDictionary) :

    # Returns birthday if in list
    print("Your birthday is " + birthdayDictionary[userInput])
else :

    # displays error message if not in list
    print("Sorry, your name is not registered in our list")