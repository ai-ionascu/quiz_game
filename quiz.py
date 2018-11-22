import random
import difflib

def game_menu():
    
    print("")
    print("1. Ask a question")
    print("2. Add questions")
    print("3. Remove questions")
    print("4. Exit game")
    print("")
    
    option = input("Choose option: ")
    return option
    
def add_questions():
    
    while True:
        question = input("Please add a question: (press 'r' for main menu)\n>")
        if question == 'r':
            break
        else:    
            answer = input("Ok, then provide an answer: (press 'r' for main menu)\n>{0}\n>".format(question))
            if answer == 'r':
                break
            else:    
                f = open('questions.txt', 'a')
                f.write(question+'\n')
                f.write(answer+'\n')
                f.close()
        break        
    
def questions_only():
    with open("questions.txt","r") as f:
        lines = f.read().splitlines()
        count=0
        questions_list=[]
        for i in lines:
            count+=1
            if count%2 != 0:
                questions_list.append(i)
        for i in questions_list:
            i = "{0}. {1}".format(questions_list.index(i)+1,i)
            print(i)
        return questions_list

def delete_operation(select):
    f = open("questions.txt","r")
    lines = f.read().splitlines()
    f.close()
    f = open("questions.txt","w")
    for line in lines:
        if line != lines[2*select-2] and line != lines[2*select-1]:
            f.write(line+"\n")
    f.close()
       
def delete_question():
    
    try:
        print("")
        questions_only()
        selection = input("\nPlease type the question number to delete: (press 'r' for main menu)\n>") 
        print("")
        while True:
            if int(selection) > len(questions_only()):
                selection = input("\nPlease make a valid selection: (press 'r' for main menu)\n>")
            else:
                delete_operation(int(selection))
                break
    
    except ValueError:
            if selection != "r":
                print("\nInvalid selection!")
                delete_question()    
                
def ask_questions():
    
    questions=[]
    answers=[]
    score = 0
    
    with open("questions.txt","r") as f:
        lines = f.read().splitlines()
        
    for i,text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
            
    questions_and_answers = list(zip(questions,answers))
    random.shuffle(questions_and_answers)
    
    for question, answer in questions_and_answers:
        guess = input(question+" (press 'r' for main menu)\n> ")
        if guess == 'r':
            break
        if guess == answer:
            print("\nYou're right!")
            score+=1
            print("Your score: {0}\n".format(score))
        else:
            count = 0
            for i in difflib.ndiff(guess, answer):
                if i[0]!=' ':
                    count+=1
            if count<=2:    
                print("\nWrong spelling, but you're right!")
                score+=1
                print("Your score: {0}\n".format(score))
            else:    
                print("\nWrong answer!\n")
        
    print("You answered correct for {0} questions out of {1}".format(score,len(questions)))    
    
def game_loop():
    
    while True:
        
        option = game_menu()
        print('')
        
        if option == '1':
            ask_questions()
            
        elif option == '2':
            add_questions()
            
        elif option == '3':
            delete_question()
            
        elif option == '4':
            break
        
        else:
            print('Please input a valid option')
            
        print('')
            
game_loop()            