import json

# Sukhamrit Singh
# Outdoor Park Concert

# path to the JSON files
priceJSONFile = './src/seatingPrice.json' 
seatingJSONFile = './src/seatingData.json' 
purchaseJSONFile = './src/purchaseInfo.json' 

# Lists and dictionaries to store in memory data
seatingJSON = {} 
priceJSON = {}
purchaseJSON = []


# fuction to load Price info JSON
def loadPriceInfo():
    # read price JSON file
    with open(priceJSONFile, "r") as priceFile: 
        # Reading from json file 
        jsondata = json.load(priceFile) 
        priceJSON = jsondata["price"]


# function to load current Seating data json
def loadCurrentSeating():

    # read seating JSON file
    with open(seatingJSONFile, "r") as seatingFile: 
        # Reading from json file 
        jsondata = json.load(seatingFile) 
        sjson = jsondata["seating"]

        for key, value in sjson.items():
            seatingJSON[key] = sjson[key]

        # print(seatingJSON["0"])


# function to load current purchase data JSON
def loadCurrentPurchase():
    # read seating JSON file
    with open(purchaseJSONFile, "r") as purchaseFile: 
        # Reading from json file 
        jsondata = json.load(purchaseFile) 
        pjson = jsondata["purchases"]

        for purchase in pjson:
            purchaseJSON.append(purchase)


# function to show purchase information
def showPurchaseInfo():
    
    print("ALL SALES:")
    
    total = 0.0
    for purchase in purchaseJSON:
        name = purchase["name"]
        rowId = purchase["rowId"]
        amount = float(purchase["amount"])
        total = total + amount
        print(" " + name + ": $%0.2f" % amount)

    print("\n Total Sale: $%0.2f" % total)


# function to look at the seating information        
def viewAvailableSeating():

    # print the column names
    print("\n")
    print("   a b c d e f g h i j k l m n o p q r s t u v w x y z")
    for key, rowData in seatingJSON.items():    
        print(key.zfill(2), end=" ") 
        for col, value in rowData.items():
            # print(value),
            print(value, end=" ")  

        print("")

    showMenu()


# function to buy the tickets
def buyTickets():
 
    # print the prices of the tickets
    userInput = input("""\n
Pick a Row:
    Front Rows 0 - 4: Price $80 
    Middle Rows 5 - 10: Price $50 
    Back Rows 11 -  19: Price $25\n
""")

    # if statement to purchase seats
    if (userInput.isdigit()):
        rowId = int(userInput)
        if (rowId >= 0 and rowId <= 19):
            if (rowId % 2 != 0):
                print("Row not available due to social distancing.")
                showMenu()
            else:
                getPurchaseCount(rowId)
        else:
            print("Invalid row..")
            showMenu()
    else:
        print("Invalid input ... ")
        showMenu()


# function to get purchased seat information
def getPurchaseCount(rowId):
    
    # priting out info to chech available seats
    maxAvailable = getSeatsAvailablityInRow(rowId)
    print("Seats Available in row " + str(rowId) + ": " + str(maxAvailable))
    
    if (maxAvailable > 0):
        userInput = input("How many seats do you want to buy? ")

        if (userInput.isdigit()):
            need = int(userInput)
            if (need <= maxAvailable):
                doRowPurchase(rowId, need)
            else:
                print(str(need) + " seats are not available in row " + str(rowId))
                showMenu()
        else:
            print("Invalid input ... ")
            showMenu()
    else:
        showMenu()


# function for the row purchases
def doRowPurchase(rid, need):
    
    colId = getRowColumnIdToBegin(rid)

    # for loop for purchasing the seats
    colList = []
    for key, rowData in seatingJSON.items(): 
        rowId = int(key)
        if (rowId == rid):
            keylist = rowData.keys()
            count = 0
            start = False

            for key in keylist:

                if (key == colId):
                    start = True
                   
                if (start is True):
                    colList.append(key)
                    count = count + 1

                if (count == need):
                    break
            
    # print(colList)

    # placing X for purchased seats
    for col in colList:
        seatingJSON[str(rid)][col] = "X"

    # print(seatingJSON[str(rid)])

    # updating the JSON files
    updatedJson = {
        "seating": seatingJSON
    }

    # update seating JSON file
    with open(seatingJSONFile, "w") as seatingFile: 
        seatingFile.write(json.dumps(updatedJson, sort_keys=False, indent=4))
        seatingFile.close()

    totalCost = displayCost(rid, need)

    nameInput = input("Your name? ")
    emaiInput = input("Your email? ")

    # creating new JSON for the user's info
    newPurchase = {
            "name": nameInput, 
            "email": emaiInput,
            "rowId": str(rid),
            "seats": colList,
            "amount": str(totalCost)
        }

    purchaseJSON.append(newPurchase)

    # new JSON
    allPurchases = {
        "purchases": purchaseJSON
    }

    # update purchase JSON file
    with open(purchaseJSONFile, "w") as purchaseFile: 
        purchaseFile.write(json.dumps(allPurchases, sort_keys=False, indent=4))
        purchaseFile.close()

    showMenu()


# function for displaying the costs 
def displayCost(rowId, need):

    maskCost = 5
    tax = 0.0725
    ticketCost = 0.0
    totalCost = 0.0

    # if statements to give price based on row
    if (rowId >= 0 and rowId <= 4):
        ticketCost = 80*need

    elif (rowId >= 5 and rowId <= 10):
        ticketCost = 50*need
        
    else:
        ticketCost = 25*need
        
    totalCost = ticketCost + (ticketCost*tax) + maskCost
    print("Total Cost: $%0.2f" % totalCost)
    return totalCost


# function to get the seats available in a row
def getSeatsAvailablityInRow(rid):
    
    colId = getRowColumnIdToBegin(rid)

    # for loop to check available seats
    n = 0
    for key, rowData in seatingJSON.items():    
        
        rowId = int(key)
    
        if (rowId == rid):
            
            c = 0
            gap = 0
            for col, value in rowData.items():

                # if seat is available
                if (value == 'a'):
                    # check if first col, then all seats are available
                    if (col == 'a'):
                        n = 26
                        break
                    else:
                        # skip two seats 
                        # n = 26 - c - 2
                        # break
                        gap = gap + 1
                        if (gap == 3):
                            n = 26 - c - 2
                            break
                c = c + 1
    return n


# function to get the row and colum ID
def getRowColumnIdToBegin(rid):
    
    colId = ""
    for key, rowData in seatingJSON.items():    
        
        # for loop to make sure to maintain social distancing
        rowId = int(key)
        gap = 0
        if (rowId == rid):
            for col, value in rowData.items():
                colId = col
                if (value == 'a'):
                    # if first column, then start from here
                    if (col == 'a'):
                        break
                    else:
                        # if not first column, then give two seat space
                        gap = gap + 1
                        if (gap > 2):
                            break
                else:
                    gap = 0
    return colId


# function to search by name
def searchByName():
    print("\n")
    nameInput = input("Name? ")
    found = False

    # getting info from JSON
    for purchase in purchaseJSON:
        name = purchase["name"]
        rowId = purchase["rowId"]
        amount = float(purchase["amount"])
        if (name == nameInput):
            print("  " + name + ": $%0.2f" % amount)
            found = True
            break

    # error message if no name is found
    if (found is False):
        print("  No purchase by " + nameInput)

    showMenu()


# function to display all purchases
def displayAllPurchase():
    print("\n")
    showPurchaseInfo()
    showMenu()


# function to quit the program
def quit():
    print("\n")
    print("quit")
    continueReservation = False


# function to load the files
def loadFiles():
    loadPriceInfo()
    loadCurrentSeating()
    loadCurrentPurchase()


# main function to show menu
def showMenu():

    # Boolean to keep the loop running
    continueReservation = True

    # Loop to keep running and prompting user
    while continueReservation:

        # Prompting User to choose a setting
        userInput = input("""\n
Menu:
    [V]iew/display available seating
    [B]uy/purchase a ticket
    [S]earch by name
    [D]isplay all purchases
    [Q]uit\n
""")

        # If user enters "V" then view seating 
        if (userInput == 'V' or userInput == 'v'):
            viewAvailableSeating()
            break

        # if user enters "B" then buy tickets
        elif (userInput == 'B' or userInput == 'b'):
            buyTickets()
            break

        # if user enters "S" then search name
        elif (userInput == 'S' or userInput == 's'):
            searchByName()
            break

        # if user enters "D" then display all purchases
        elif (userInput == 'D' or userInput == 'd'):
            displayAllPurchase()
            break

        # if user enters "Q" then quit program
        elif (userInput == 'Q' or userInput == 'q'):
            quit()
            break

        # if user enters invalid input then display error
        else:
            print("\n")
            print("Invalid input")


# default functions
loadFiles()
showMenu()
