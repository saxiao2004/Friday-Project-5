# Susana Xiao
# Friday Project 5
# DS 3850 Section 001
# The following project displays question from a dictionary to the user and further provided feedback is they answered the question correctly.

# Importing the sqlite3 module which establishes a connection to the database.
import sqlite3

# The connection function is then used to call the database name 'FridayProj5.db', and then we add one last variable called cursor to execute the connection to the database.
connection = sqlite3.connect ('FridayProj5.db')
cursor = connection.cursor()

# The execute method allows us to perform some execution on our db object, and retrieving data from the 'question' and 'answer' columns of the 'QuestAns' database table.
# The fetchall is used to retrieve all rows at once and converting it into dictionaries.
cursor.execute("SELECT question, answer FROM QuestAns")
quiz_Questions = dict (cursor.fetchall())

# Creating a for loop that allows user to input there answers to the questions.
# An "if" and "else" statement providing feedback on if the user's answer match the correct answer from the dictionary.
for questions in quiz_Questions:
    print (questions)
    user_answer = input ("Your answer: ")
    if user_answer.lower() == str(quiz_Questions[questions]).lower():
        print ("Correct!")
    else:
        print ("Incorrect. The correct answer is:", quiz_Questions[questions])

print ("Quiz ended.")

# Closing the cursor and the database connection.
cursor.close()
connection.close()