# ---------------------------------------------------------------------#
# Title: To Do file creation
# Dev: SOC
# Date: 2/3/19
# ChangeLog: (Who, What, When)
# Purpose: to create a home inventory
# SOC, 2/10/19, Created Scipt
# ---------------------------------------------------------------------#









# -- Data --#
# declare variables and constants

objFileName = "ToDo.txt" # objFile = An object that represents a file
strData = ""  # strData = A row of text data from the file
dicRow = {}  # dicRow = A row of data separated into elements of a dictionary {Task,Priority}
lstTable = [] # lstTable = A dictionary that acts as a 'table' of rows
strChoice = ""   # Choice for data

# -- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.
# Add the each dictionary "row" to a python list "table"

objFile = open(objFileName, "r")
for line in objFile:
    strData = line.strip()  # remove line breaks
    intComLoc = strData.index(",")  # locate comma to parse/slice text into the two pieces of data
    strTask = strData[0:intComLoc]  # task data string
    strPriority = strData[intComLoc + 1: len(strData)]  # priority data string
    dicRow = {"Task": strTask, "Priority": strPriority}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

# Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print("The current tasks to do follow:")
        print("*******************************")
        for item in lstTable:
            print(item["Task"] + "(" + item["Priority"] + ")")
        print("*******************************")
        print()
        continue
# Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # query user for information
        strAddedTask = input("What is the task you would like to add? - ")
        strAddedTaskPr = input("What is the priority (high/low)? - ")
        # define new dictionary item using input and append to dictionary
        dicRowNew = {"Task": strAddedTask, "Priority": strAddedTaskPr}
        lstTable.append(dicRowNew)
        # display updated list to user
        print("The task has been added.")
        print("The current tasks to do follow:")
        print("*******************************")
        for item in lstTable:
            print(item["Task"] + "(" + item["Priority"] + ")")
        print("*******************************")
        print()
        continue
# Step 5 - Remove an item from the list/Table
    elif (strChoice == '3'):
        # query user for information
        strRemoveTask = input("What is the task you would like to remove? - ")
        # verify task is in the dictionary
        #initialize variables
        blnTaskInDic = False
        intItemNo = 0
        # task found in dictionary
        for item in lstTable:
            if strRemoveTask == item["Task"]:
                del lstTable[intItemNo]
                blnTaskInDic = True
            else:
                intItemNo = intItemNo + 1
        # display updated list to user
        if blnTaskInDic == True:
            print("The task has been removed.")
            print("The current tasks to do follow:")
            print("*******************************")
            for item in lstTable:
                print(item["Task"] + "(" + item["Priority"] + ")")
            print("*******************************")
            print()
        # task not found in dictionary
        else:
            print("Task not found in list.  Nothing has been removed.")
            print()
        continue
# Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        objFile = open(objFileName, "w")
        for item in lstTable:
            objFile.write(item["Task"] + "," + item["Priority"] + "\n")
        objFile.close()
        print("List saved to the file ToDo.txt.")
        continue
# Step 7 - Exit program
    elif (strChoice == '5'):
        break  # and Exit the program
