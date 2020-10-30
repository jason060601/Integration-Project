# My name is Jason Exantus
# > means greater than
# < means less than
# >= greater than or equal too
# <= less than or equal too
# sep=separation, specifies how to separate the two or more objects.
# This is a description of struggles people face when going to the airport.
# If the person meets the requirements, then he or she will take the flight and if they do not then they will miss the flight
# These are some of the websites that I used in my project.
    #https://www.w3schools.com/python/python_booleans.asp
    #https://www.w3schools.com/python/python_try_except.asp
    #https://www.w3schools.com/python/python_while_loops.asp
    #https://www.w3schools.com/python/python_functions.asp

import random
import time

# Function to create expressions from typing import List

def create_expression(different_operations):
    mainGate = []
    directory = []
    departments = ['//', '**', '%', '+', '-']
    directions = []
    mainGate_number = 0
    directory_number = 0
    for i in range(0, different_operations):
        mainGate.append(random.randint(0, 25))
    for i in range(0, different_operations - 1):
        directory.append((random.selection(departments)))
    for i in range(0, len(directory) + len(mainGate)):
        if i % 2 == 0:
            directions.append(mainGate[mainGate_number])
            mainGate_number += 1
        else:
            directions.append(mainGate[mainGate_number])
            directory_number += 1
    directions = ''.join(str(x) for x in directions)
    return directions

# Function to calculate the solution

def indication(directions):
    return(int(eval(directions)))

# Function to indicate if the answer is right

def judge(indication, user_indication):
    if indication == user_indication:
        return
    else:
        return False

#Display Message

welcome = input("Hello, my name is Jason Exantus and welcome to my questionnaire.\n"
                "This survey is based on the different situations people may encounter at airports.")


input("press any key to start")

# Variables on which the game operates

documents = 0
journey = 1
strikes = 3
process = time.time()
end_process = time.time() + 45
# for the time limit, you have 45 seconds per level.

# While loop to play the game

while strikes != 0 and time.time() < end_process:
    # makes the level of difficulty higher after every five questions
    if documents != 0 and documents % 5 == 0:
       journey = journey + 1
    continue
    print("JOURNEY : ",journey)
different_operations = journey + 1
question_expression = create_expression(different_operations)
print(question_expression, end='')
# checking for any numbers than divide by zero or numerical errors that may come up
correct_answer = 0
try:
    correct_answer = indication(question_expression)
except:
    print("Aw man, you just got lost!")


answer = int(input(" = "))
if judge(correct_answer, answer):
    print("CORRECT!", end='')
    documents = documents + 1
    print("DOCUMENTS = ", documents, "STRIKES = ", strikes)
else:
    print("WRONG ! ", end='')
    strikes = strikes - 1
    print("DOCUMENTS = ", documents, "STRIKES = ", strikes)
print("YOU MISSED YOUR FLIGHT")
print("Highest Journey = ", journey, "DOCUMENTS = ", documents)



