
def play():
    score=0
    player_ans=input("What is the tallest peak in the world? ")
    if player_ans.lower() == "mount everest":
        score+=1
        print("Correct ans")
    else:
        print("Wrong ans")

    player_ans=input("What is the tower in paris? ")
    if player_ans.lower() == "eiffel tower":
        score+=1
        print("Correct ans")
    else:
        print("Wrong ans")
    
    player_ans=input("What is the city of joy? ")
    if player_ans.lower() == "kolkata":
        score+=1
        print("Correct ans")
    else:
        print("Wrong ans")

    player_ans=input("What is the largest mammel on earth? ")
    if player_ans == "blue whale":
        score+=1
        print("Correct ans")
    else:
        print("Wrong ans")
    player_ans=input("EWho is the prime minister of India? ")
    if player_ans == "narendra modi":
        score+=1
        print("Correct ans")
    else:
        print("Wrong ans")

    print(score)
        
        

play()
