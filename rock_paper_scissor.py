import random
def play():
    user="y"
    user_score=0
    comp_score=0
    while user=="y":
        comp_choice= random.choice(['rock','paper','scissor'])
        user_choice= input("Choose rock,paper or scissor: ")
        if comp_choice== user_choice:
            print("Draw")

        elif comp_choice == "rock" and user_choice=='scissor':
            print("You lose")
            print(comp_choice+" "+user_choice)
            comp_score+=1

        elif comp_choice == "rock" and user_choice=='paper':
            print("You win")
            print(comp_choice+" "+user_choice)
            user_score+=1

        elif comp_choice == "paper" and user_choice=='scissor':
            print("You win")
            print(comp_choice+" "+user_choice)
            user_score+=1

        elif comp_choice == "paper" and user_choice=='rock':
            print("You lose")
            print(comp_choice+" "+user_choice)
            comp_score+=1

        elif comp_choice == "scissor" and user_choice=='paper':
            print("You lose")
            print(comp_choice+" "+user_choice)
            comp_score+=1

        elif comp_choice == "scissor" and user_choice=='rock':
            print("You win")
            print(comp_choice+" "+user_choice)
            user_score+=1



        user= input("Wanna continue [y/n]")
    print("Your score: ",user_score)
    print("Computer score: ",comp_score)

play()