#this is a rock paper and scissors game 

import random

def rps():
    options=["rock","paper","scissors"]
    player=input("Enter your choice: ").lower()
    comp=random.choice(options)
    print(f"You chose {player} and computer chose {comp}")
    if(player==comp):
          print("A TIEEE")
    elif(player=="rock"):
        if(comp=="scissors"):
            print("YOU WIN!")
        elif(comp=="paper"):
            print("you lose:(")
    elif(player=="scissors"):
        if(comp=="paper"):
            print("YOU WIN!")
        elif(comp=="rock"):
            print("you lose:(")
    else:
        if(comp=="rock"):
            print("YOU WIN!")
        elif(comp=="scissors"):
            print("you lose:(")

rps()
    
    
