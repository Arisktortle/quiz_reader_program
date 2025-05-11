#locate and open the quiz file
#read the question, options abcd, and the correct answer
#store the questions to a list

def read_questions(filename="quiz_data.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("File not found.")
        return []
    
    blocks = content.strip().split("#QUESTION_") #reads the file for a question header and stores it
    questions = []
    
#read the question, options abcd, and the correct answer
#store the questions to a list
#shuffle the order of the questions
#show the first question
#prompt the user for an answer
#verify if the answer is correct 
#loop until all questions are answered
#count the correct answers
#output the final score