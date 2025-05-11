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
    
    for block in blocks: #skips empty blocks
        if not block.strip():
            continue
        lines = block.splitlines()
        question_text = ""  
        choices = {}  #storage of the choices
        correct = "" #storage of the correct answer
        
        for line in lines: #Locate for the line with the question
            line = line.strip()
            if line.startswith("Question"):
                question_text = line.split(":", 1)[1].strip()
            elif any(line.startswith(f"{opt})") for opt in "abcd"): #locates the choices in the file
                choices[line[0]] = line[3:].strip()
            elif line.startswith("ANSWER:"): #locates the correct answer and stores it, converts in lower cases
                correct = line.split(":", 1)[1].strip().lower()
        
#read the question, options abcd, and the correct answer
#store the questions to a list
#shuffle the order of the questions
#show the first question
#prompt the user for an answer
#verify if the answer is correct 
#loop until all questions are answered
#count the correct answers
#output the final score