import random
key=1
while key==1:
    a=random.randrange(1,4)

    if(a==1):
        comp="rock"
    elif(a==2):
        comp="paper"
    else:
        comp="scissor"

    print("Enter rock(r) paper(p) or scissor(s) :")
    b=input()

    if(b=="r"):
        human="rock"
    elif(b=="p"):
        human="paper"
    elif(b=="s"):
        human="scissor"
    else:
        print("INVALID CHOICE !!!")



    print("You choose :\n",human)
    print("Computer choose :\n",comp)
    print(20*"-")
    if(comp=="rock" and human=="paper"):
        print("Congratulations! You win")
    elif(comp=="paper" and human=="rock"):
        print("Computer wins! Better Luck next Time")
    elif(comp=="paper" and human=="scissor"):
        print("Congratulations! You win")
    elif (comp == "scissor" and human == "paper"):
        print("Computer wins! Better Luck next Time")
    elif(comp=="scissor" and human=="rock"):
        print("Congratulations! You win")
    elif(comp=="rock" and human=="scissor"):
        print("Computer wins! Better Luck next Time")

    if(comp==human):
        print("Its a Draw")

    print()
    print("press -> play again(1) or exit(0) :")
    key=int(input())
