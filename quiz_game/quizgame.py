def new_quiz():
    choption=[]
    correct_options=0
    question_num=1

    for key in questions:
        print("<--------------------->")
        print(key)
        for i in options[question_num-1]:
            print(i)
        choose=input("Enter (a,b,c,d):")
        choose.lower()
        choption.append(choose)
        correct_options+=check_answer(questions.get(key),choose)
        question_num+=1
    display_score(correct_options,choption)
def check_answer(answer,guess):
    if answer==guess:
        print("Correct!")
        return 1
    else:
        print("wrong!")
        return 0

    
def display_score(correct_guesses,guesses):
    print("<---------->")
    print("Results")
    print("<---------->")
    print("Answers:",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guesses:",end=" ")
    for i in guesses:
        print(i,end=" ")
    print()

    score=(correct_guesses/len(questions))*100
    print("Your score is {}{}:".format(score,'%'))
def play_again():
    respnse=input("Do you want to play again?:(yes or no): ")
    respnse=respnse.upper()
    if respnse=="YES":
        return True
    else:
        return False
    

questions={"Which type of Programming does Python support?:":"d","Which of the following is the correct extension of the Python file?:":"c","What will be the value of the following Python expression?4 + 3 % 5":"a","Which keyword is used for function in Python language?:":"b", "Which of the following functions can help us to find the version of python that we are currently working on?:":'a',"Python supports the creation of anonymous functions at runtime, using a construct called?:":"c"}
options=[['a. object-oriented programming','b. structured programming','c. functional programming','d. all of the mentioned'],['a. .python','b. .pl','c. .py','d. .p'],['a. 7','b. 2','c. 4','d. 1'],['a. Function','b. Def','c. Fun', 'd. Define'],['a. sys.version(1)','b. sys.version(0)','c. sys.version()','d. sys.version'],['a.  pi','b. anonymous','c. lambda','d. none of the mentioned']]

new_quiz() 
while play_again():
    new_quiz()

print("See you again")

