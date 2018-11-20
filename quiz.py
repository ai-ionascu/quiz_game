import random

def game_menu():
    
    print("1. Ask a question")
    print("2. Add questions")
    print("3. Exit game")
    
    option = input("Choose option: ")
    return option
    
def add_questions():
    
    question = input('Please add a question:\n>')
    answer = input("Ok, then provide an answer:\n>{0}\n>".format(question))
    f = open('questions.txt', 'a')
    f.write(question+'\n')
    f.write(answer+'\n')
    f.close()
    
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
        guess = input(question+"> ")
        
        if guess == answer:
            print("You're right!")
            score+=1
            print("Your score: {0}".format(score))
            
        else:
            print("Wrong answer!")
        
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
            break
        
        else:
            print('Please input a valid option')
            
        print('')
            
game_loop()            