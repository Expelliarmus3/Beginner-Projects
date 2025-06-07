import random


def play():
    turn=0
    player1_score=0
    player2_score=0
    max_score= 50
    i=0
    while i<=max_score:
        if turn%2==0:
            ques= input("Do you wanna play the game Player1? (Y/N)")
            if str.upper(ques)=="Y":
                print("Cool! Lets roll the die!Player1 Your turn ")
                roll= random.randint(1,6)
                if roll != 1:
                    print("Lucky Player1")
                    player1_score+=roll
                else:
                    print("You lost points player1")
                    player1_score=0
            if str.upper(ques)=="N":
                break
            turn+=1

        elif turn%2!=0:
            ques= input("Do you wanna play the game Player2? (Y/N)")
            if str.upper(ques)=="Y":
                print("Cool! Lets roll the die! Player 2 your turn ")
                roll= random.randint(1,6)
                if roll != 1:
                    print("Lucky Player2")
                    player2_score+=roll
                else:
                    print("You lost points player2")
                    player2_score=0
            if str.upper(ques)=="N":
                break
            turn+=1

        i+=1

    if player1_score==50 and player2_score<50 or player1_score>player2_score:
        print("Player1 you won!")
        print("Player1:",player1_score,"Player2: ",player2_score)
    elif player2_score==50 and player1_score<50 or player2_score>player1_score:
        print("Player2 you won!") 
        print("Player1:",player1_score,"Player2: ",player2_score)
    else:
        print("Player1:",player1_score,"Player2: ",player2_score)

play() 