# --- Define your functions below! ---
from random import *
def intro():
    print("Hi, I see you opened me up. I am Bob bot.")
    print("( ͡° ͜ʖ ͡°)")


def process_input(answer):
    if is_valid_input(answer):
        say_greeting()
    if is_valid_input_other(answer):
        print("Oh okay rude but understandable. ಥ_ಥ")
    else:
        say_default()

def is_valid_input(word):
    valid= ["hi", "hey", "whats up", "heyo","yo", "'sup", "greeting", "hi my name is"  ]
    if word in valid:
        return True
    else:
        return False

def is_valid_input_other(word):
    valid2=["bye", "bye loser", "Au revior", "Adios", "bai", "im leaving", "shut up"]
    if word in valid2:
        return True
    else:
        return False

def say_greeting():
    print("..... Should I say hi again?")
    say_askmequestion()

def say_default():
    print("weirdo. (<.>)")
    say_askmequestion()




#def default_answer_question(answer):
    #answer= answer.split()
    #valid3= ["do", "can", "you"]
    #if answer[0] in valid3:
        #return True
    #else:
        #return False

def say_askmequestion():
    answer= input("I'm bored. Ask me any question if you want: ")
    answer1=answer.split()
    list= ["yes", "not at all ", "haha NOPE", "usually"]
    whenlist= ["never", "Every week at Tuesday.", "At night when no one is looking"]
    wherelist= ["At your mom's house", "In your dad's bedroom", "Right here loser"]
    random_wherelist= randint(0, len(whenlist)-1)
    random_whenlist= randint(0, len(whenlist)-1)
    random_listofchoice = randint(0, len(list)-1)
    for word in answer:
        #if default_answer_question(word):
            #print( list[random_listofchoice])
            #continue_1()
        if answer1[0]=="do":
            print( list[random_listofchoice])
            continue_1()
        elif answer1[0]=="can":
            print( list[random_listofchoice])
            continue_1()
        elif answer1[0]=="you":
            print( list[random_listofchoice])
            continue_1()
        elif answer1[0]=="why":
            print("why not...")
            import time
            time.sleep(2)
            print("Sorry if I got philosophical :/")
            continue_1()
        elif answer1[0]=="how":
            print("I dont know howwwwwwwwwwwwww. I have low intelligence")
            print("Anddd low emotional intelligence.")
            continue_1()
        elif answer1[0]=="what":
            print("Dont ask me a what questions I dont even know what I am.")
            print("I'm just a bot that self-degrades itself. :')")
            continue_1()
        elif answer1[0]=="will":
            print("yes")
            print("I'm a yes kind of gal.")
            continue_1()
        elif answer1[0]=="when":
            print(whenlist[random_whenlist])
            continue_1()
        elif answer1[0]=="where":
            print(wherelist[random_wherelist])
            continue_1()
    



def continue_1():
    import time
    time.sleep(1.3)
    answer=input("Sooooooo, want to continue chatting? yes or no:")
    if answer=="yes":
        say_askmequestion()
    if answer== "no":
        print("Well me neither. Bye. ಠ益ಠ")





# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("You: ")
        process_input(answer)
        break

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
