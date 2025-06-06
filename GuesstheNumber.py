import random

def play():
    upper=int(input("Enter upper limit : "))
    comp = random.randint(0,upper)
    while True:
        num= input("Guess a number between 0 and "+ str(upper)+" : ")
        guess= int(num)
        if guess==comp:
            print("You got it")
            break
        elif guess<comp:
            print("Nope,a lil higher")
        elif guess>comp:
            print("Nope a lil lower")
        else:
            print("Invalid input..Try again next time")
            quit()

play()