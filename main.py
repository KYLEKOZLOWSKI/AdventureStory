# Kyle Kozlowski 27/06/2019

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
    global health
    global run
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
    print("Ok... Let me remember that!")
    #Makes it seem like it is trying to store it
    time.sleep(2)
    print("Done!")
    #Greets user
    print("Hello," + " " + username + "!")
    input("Press enter to continue")
    #Tells them there health
    print("You have " + str(health) + " health!")
    #Tells them to answer in capitals
    print("\tWhen you are asked something like this:\n\t(A)Animal (O)Other\n\tAnswer with a capital letter: A not a")
    
    input("Press enter to begin")
    
    #Story (Question 1)
    print("\n\n\n\t-==The Street==-")
    print("You are walking down a very dull and wet street at night!\nYou see a stray cat!")
    print("You can (T)Take the cat with you\nOR\nYou can (G)Give the cat to the vets!")
    
    #Asks for answer
    s1 = input("\tAnswer:")
    
    # Checks what route they want ot take
    if s1 == "T":
        print("You take the cat but it was addressed to The Capital ")
        s11 = input("What is the capital of United Kingdom?")
        if s11 == "London":
            correct("London")
        else:
            incorrect("London")
    elif s1 == "G":
        print("You take the cat to the vets they ask youto solve a puzzle to prove your not a robot!")
        print("What is the capital of wales?")
        s12 = input("\tAnswer: ")
        if s12 == "Cardiff":
          #Runs correct functio9n
            correct("Cardiff")
        else:
            incorrect("Cardiff")
    else:
        print("Invalid input")
        health - 20


    #Story (Question 2)
    print("\t-==Shed==-")
    print("You are tired and see a shed\n You go to sleep in it...")
    print("You can (U)Unlock door\nOR\nYou can (W)Go through a window")
    s2 = input("\tAnswer:")
    if s2 == "U":
        print("You try to open but the door is locked ")
        s21 = input("What is the capital of France")
        if s21 == "Paris":
            correct("Paris")
        else:
            incorrect("Paris")
    elif s2 == "W":
        print("You try to go through the window! Is the earth flat?")
        print("(T)True (F)False")
        s22 = input("\tAnswer: ")
        if s22 == "F":
            correct("False")
        else:
            incorrect("False")
    else:
        print("Invalid input")
        health - 20
        
        
    #Story (Question 3)
    print("\t-==Basement==-")
    print("You are curious and see an entrance to a basement\n You try to open it up but it is stuck...")
    print("You can (B)Break it open\nOR\nYou can (C)Use a crowbar")
    s3 = input("\tAnswer:")
    if s3 == "b":
        print("You try to break it doesn't open\n You increase your power by answering the following question...")
        s21 = input("What is the other presenter with Ant & D**?")
        if s21 == "Dec":
            correct("Dec")
        else:
            incorrect("Dec")
    elif s2 == "C":
        print("You try to go break it with the crowbar!\n You get in!")
        correct("Nothing")
    else:
        print("Invalid input")
        health - 20
        
        
    
    #Story (Question 4)
    print("\n\n\n\t-==The Zoo==-")
    print("You help a animal back into the zoo!")
    print("You can (O)Open the cage\nOR\nYou can (B)Break in!")
    
    #Asks for answer
    s4 = input("\tAnswer:")
    
    # Checks what route they want ot take
    if s4 == "B":
        print("You break in")
        s41 = input("What is the largest land animal?")
        if s41 == "Elephant":
            correct("Elephant")
        else:
            incorrect("Elephant")
    elif s4 == "O":
        print("You open the cage")
        print("What is the longest river in the world?")
        s42 = input("\tAnswer: ")
        if s42 == "Nile":
          #Runs correct function
            correct("Nile")
        else:
            incorrect("Nile")
    else:
        print("Invalid input")
        health - 20
        
    #Story (Question 5)
    print("\n\n\n\t-==The War==-")
    print("You enter war")
    print("You can (F)Fight\nOR\nYou can (S)Sit and watch")
    
    #Asks for answer
    s5 = input("\tAnswer:")
    
    # Checks what route they want ot take
    if s5 == "F":
        print("You fight")
        s51 = input("What is the largest contry by land?")
        if s51 == "Russia":
            correct("Russia")
        else:
            incorrect("Russia")
    elif s5 == "S":
        print("You open the cage")
        print("What is the largest contry by land?")
        s52 = input("\tAnswer: ")
        if s52 == "Russia":
          #Runs correct function
            correct("Russia")
        else:
            incorrect("Russia")
    else:
        print("Invalid input")
        health - 20

    

        
            


while run:
    startGame()
    if health <= 0:
      exit()
