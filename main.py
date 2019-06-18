import random
import time
################################################
# The storage of data
username = ""
health = 100
run = True
question_no = 0
################################################

def startGame():
    global question_no
    def correct(correct):
        global question_no
        question_no = question_no+1
        global health
        print("Correct!")
        print("The answer was " + correct)
        print("Health: " + str(health))
        print("Question: " + str(question_no))
        return
    def incorrect(incorrect):
        global health
        global question_no
        question_no + question_no+1
        print("Incorrect!")
        print("The correct answer was " + incorrect)
        health = health-20
        print("Health: " + str(health))
        print("Question: " + str(question_no))
        return
    #Gives the startGame the data
    global username
    global health
    global run
    global question_no
    print("Hello User!\nThats what we know you as weird?")
    #Gets username
    username = input("\tWhat is your name? ")
    #Capatilises the username
    username = username.title()
    print("Ok...Let me remember that!")
    #Makes it seem like it is trying to store it
    time.sleep(3)
    print("Done!")
    #Greets user
    print("Hello," + " " + username + "!")
    #Tells them there health
    print("You have " + str(health) + " health!")
    #Story (Question 1)
    print("\t-==The Street==-")
    print("You are walking down a very dull and wet street at night!\nYou see a stray cat!")
    print("You can (T)Take the cat with you\nOR\nYou can (G)Give the cat to the vets!")
    s1 = input("\tAnswer:")
    if s1 == "T" or "t":
        print("You take the cat but it was addressed to The Capital ")
        s11 = input("What is the capital of United Kingdom?")
        if s11 == "London":
            correct("London")
        else:
            incorrect("London")
    elif s1 == "G" or "g":
        print("You take the cat to the vets they ask youto solve a puzzle to prove your not a robot!")
        print("What is the capital of wales?")
        s12 = input("\tAnswer: ")
        if s12 == "Cardiff" or "cardiff":
            correct("Cardiff")
        else:
            incorrect("Cardiff")
    else:
        print("Invalid inpout")


    #Story (Question 2)
    print("\t-==Shed==-")
    print("You are tired and see a shed\n You go to sleep in it...")
    print("You can (U)Unlock door\nOR\nYou can (W)Go through a window")
    s1 = input("\tAnswer:")
    if s1 == "U" or "u":
        print("You try to open but the door is locked ")
        s11 = input("What is the capital of United Kingdom?")
        if s11 == "London":
            correct("London")
        else:
            incorrect("London")
    elif s1 == "G" or "g":
        print("You take the cat to the vets they ask youto solve a puzzle to prove your not a robot!")
        print("What is the capital of wales?")
        s12 = input("\tAnswer: ")
        if s12 == "Cardiff" or "cardiff":
            correct("Cardiff")
        else:
            incorrect("Cardiff")
    else:
        print("Invalid input")
    

        
            


while run:
    startGame()
