import random #random library for getting a random question

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
                
        if question_text and choices and correct: #if there is no error found within the file and blocks of code, it is stored.
            questions.append({
                "question": question_text,
                "choices": choices,
                "correct": correct
            })

    return questions

if __name__ == "__main__":
    questions = read_questions() #calls the function to read the question in the file, if none the program exits
    if not questions:
        exit()
        
    question = random.choice(questions) #call a random question for the user to answer
    print("\n" + question["question"])
    for opt, text in question["choices"].items():
        print(f"{opt}) {text}")

    answer = input("\nYour answer (a, b, c, d): ").lower().strip() #prompts the user to input an answer for the random question
    if answer == question["correct"]: #checks if the answer is correct
        print("Your Answer is correct.")
    else:
        print(f"Your Answer is wrong. The correct answer is {question['correct']}) {question['choices'][question['correct']]}")