import turtle
import random
import time
HEIGHT=500
WIDTH=500

COLOR=['red','blue','cyan','orange','green','yellow']
def get_racers():
    while True:
        racer= input("Enter number of racers: ")
        if racer.isdigit():
            racer= int(racer)
        else:
            continue
        if 2<=racer<=10:
            return racer
        else:
            continue

def race(colors):
    turtles= generate_racer(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.dot()
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]



def generate_racer(colors):
    turtles=[]
    spacingx= WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer= turtle.Turtle()
        racer.shape('turtle')
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacingx, -HEIGHT//2+20)
        
        turtles.append(racer)

    

    return turtles

def init_turtle():
    screen= turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")
 


racers= get_racers()
init_turtle()
random.shuffle(COLOR)
colors= COLOR[:racers]
winner = race(colors)
print("The winner is the turtle with color:", winner)

turtle.done()