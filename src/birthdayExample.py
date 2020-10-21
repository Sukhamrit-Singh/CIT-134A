import json

# getting user input
# userInput = input("Enter a name:")
# print("userInput = " + userInput)

# read the birthday json file (the path to your file may be different than mine)
# use the full path if that helps, for example
# pathToFile = 'E:/Users/gabriel/GitHub/evc-cit134a-python-data-structures/src/birthday.json'

# you can use a shorter relative path too
pathToFile = './src/birthday.json' 

with open(pathToFile, 'r') as openfile: 
  
    # Reading from json file 
    birthdayJSON = json.load(openfile) 


birthdayDictionary = {}

# loop json list of data and put each name into a dictionary
for record in birthdayJSON:

    # fetch name and birthday
    name = record["name"]
    birthday = record["birthday"]

    birthdayDictionary[name] = birthday


# print melany's birthday
melBirthday = birthdayDictionary["Clair Boyle"]
print("Melany Birthday = " + melBirthday)



