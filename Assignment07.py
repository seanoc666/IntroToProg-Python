# -------------------------------------------------#
# Title: Working with errors and pickling
# Dev:   Sean O'Connor
# Date:  02/21/19
# Desc: Track Diet
# ChangeLog:SOC, 02/21/2019,  Create a simple example  of Python Exception handling and pickling.
# -------------------------------------------------#
'''
1)	Create a simple example of how you would use Python Exception Handling. Make sure to comment your code.
2)	Create a simple example of how you would use Python Pickling. Make sure to comment your code.
'''

# --Data--#

# declare variables and constants
# f = An object that represents a file
# weight_input= input of weight
# date_input= Input of date

# --Processing--#

import pickle


WEIGHT = []  # create a global list to save weight and date



# define the method
def add_weight():
    print("Please input your weight, and the date.")  # capture user input
    print("Enter 'Exit' to quite.")  # Program exit when user input 'exit'.
    while True:
        weight_input = input("Please your weight: ")
        if weight_input.lower() == 'exit': # if user input'exit', program exit
            break
        else:
            date_input = str(input("Please enter the date: "))  # possible point of exception
            WEIGHT.append([weight_input, date_input])  # append to global list


# Save data to the file using pickle
def dump_data(weight, filename):
    f = open(filename, 'ab')  # Create and write(append) into a binary file
    pickle.dump(weight, f)  # dump the text contents to f
    f.close()  # File close


# Read data with pickle from a binary file
def load_data(filename):
    f = open(filename, 'rb')  # open and read text from the binary file
    data = pickle.load(f)  # Load data from f
    f.close()  # File close
    return data


# Error handling
#--Presentation--#
try:
    add_weight()
    dump_data(WEIGHT, 'weight.dat')
    file_content = load_data('weight.dat')

    # format and print the items in the file
    print('Here is a summary of your weight:')
    for x in file_content:
       print(x[0] + ' on ' + str(x[1]))
   # print(load_data)


except Exception as e:  # capture exception and print the error
    print('An error has occurred:')
    print(e)
