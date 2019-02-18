# ---------------------------------------------------------------------#
# Title: To Do file creation with class and functions
# Dev: SOC
# Date: 2/17/19
# ChangeLog: (Who, What, When)
# Purpose: to create a home inventory
# SOC, 2/17/19, Created Scipt
# ---------------------------------------------------------------------#


# -- Data --#
# declare variables and constants
objFileName = "c:\_pythonclass\Assignment06\Todo.txt" #Name and location of text file
strData = ""                                          # strData = A row of text data from the file
dicRow = {}                                           # dicRow = A row of data separated into elements of a dictionary {Task,Priority} 
lstTable = []                                         # lstTable = A dictionary that acts as a 'table' of rows


# Creating a class and functions
class ToDoFunctions (object):

        @staticmethod  #If I needed a write funtion.
        def writeFunction():
                objFile = open(objFileName, "a")
                for line in objFile:
                        strData = line.split(",") # readline() reads a line of the data into 2 elements
                        dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
                        lstTable.append(dicRow)
                objFile.close()



        @staticmethod  #For option 1-Show current Data with formatting
        def showFunction():
                print("******* The current items ToDo are: *******")
                for row in lstTable:
                        print(row["Task"] + "(" + row["Priority"] + ")")
                print("*******************************************")

        @staticmethod  #Add a new item and priority to the list
        def addFunction():
           # Add a new item to the list/Table

                 strTask = str(input("What is the task? - ")).strip()
                 strPriority = str(input("What is the priority? [high|low] - ")).strip()
                 dicRow = {"Task":strTask,"Priority":strPriority}
                 lstTable.append(dicRow)
                 print("Current Data in table:")
                 for dicRow in lstTable:
                        print(dicRow)

        @staticmethod  #Remove an item and priority from the list
        def removeFunction():
                 strKeyToRemove = input("Which TASK would you like removed? - ")
                 blnItemRemoved = False #Creating a boolean Flag
                 intRowNumber = 0
                 while(intRowNumber < len(lstTable)):
                        if(strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])): #the values function creates a list!
                                del lstTable[intRowNumber]
                                blnItemRemoved = True
                        #end if
                        intRowNumber += 1
    
        #5b-Update user on the status
                 if(blnItemRemoved == True):
                        print("The task was removed.")
                 else:
                         print("I'm sorry, but I could not find that task.")

        #5c Show the current items in the table
                 print("******* The current items ToDo are: *******")
                 for row in lstTable:
                        print(row["Task"] + "(" + row["Priority"] + ")")
                 print("*******************************************")

        @staticmethod #To save an item.  Giving them the choice.
        def saveFunction():
                print("******* The current items ToDo are: *******")
                for row in lstTable:
                        print(row["Task"] + "(" + row["Priority"] + ")")
                print("*******************************************")
        #5b Ask if they want save that data
                if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
                        objFile = open(objFileName, "w")
                        for dicRow in lstTable:
                                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
                        objFile.close()
                        input("Data saved to file! Press the [Enter] key to return to menu.")
                else:
                        input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")


while(True):
        print ("""
        Menu of Options
        1) Show current data
        2) Add an item
        3) Remove an existing item.
        4) Save Data to File
        5) Exit Program
        """)
        strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
        print()#adding a new line

        if (strChoice.strip() == '1'):
                ToDoFunctions.showFunction()   #Calling class ToDoFunctions and the show function
                continue
        elif (strChoice.strip() == '2'):       #Calling class ToDoFunctions and adding an item
                ToDoFunctions.addFunction()
                continue
        elif (strChoice.strip() == '3'):
                ToDoFunctions.removeFunction() #Calling class ToDoFunctions and removing an item
                continue
        elif (strChoice.strip() == '4'):       #Calling class ToDoFunctions and saving the item
                ToDoFunctions.saveFunction()
                continue
        elif (strChoice.strip() == '5'):
                break













#
