# Susana Xiao
# Project 3 Quiz Bowl
# DS 3850 Section 001
# The following project displays question from a dictionary to the user and further provided feedback is they answered the question correctly.

# A dictionary filled with questions displayed for the user to answer.

quiz_Questions =  {'Who painted the Mona Lisa': "Leonardo da Vinci",
                   'What is the capital of France?': "Paris", 
                   'How many colors are in a rainbow?': "7",
                   'True or False: Honey is the only food that never goes bad?': "True",
                   'What star sign is latin for the word lion?': "Leo"}

# Creating a for loop that allows user to input there answers to the questions.
# An "if" and "else" statement providing feedback on if the user's answer match the correct answer from the dictionary.

for questions in quiz_Questions:
    print (questions)
    user_answer = input ("Your answer: ")
    if user_answer == quiz_Questions[questions]:
        print ("Correct!")
    else:
        print ("Incorrect. The correct answer is:", quiz_Questions[questions])

print ("Quiz ended.")
