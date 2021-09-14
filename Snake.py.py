from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
<<<<<<< HEAD:snake_velocidad.py
velocidad = 100
#se utiliza una variable en la que se sellecciona la velocidad
vel = input("Seleccione velocidad con los números 0, 1, 2 donde dos es el más rápido \n")
=======
foodN = vector(0, 0)
global mouseclickx 
global mouseclicky

foodNew = True
>>>>>>> origin/JaredBranch:Snake.py

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

<<<<<<< HEAD:snake_velocidad.py
=======
    
def findcoords(x,y):
    
    
    mouseclickx = x
    mouseclicky = y
    foodN.x = int(int(x)/10)*10
    foodN.y = int(int(y)/10)*10
    #square(mouseclickx,mouseclicky, 9, 'green')
    update()

>>>>>>> origin/JaredBranch:Snake.py
def move():
    print(food.x,food.y)
    print(foodN.x,foodN.y)
     
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    
        
    elif head == foodN:
        print('Snake:', len(snake))
        foodN.x = randrange(-15, 15) * 10
        foodN.y = randrange(-15, 15) * 10
        
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')
    
    square(food.x, food.y, 9, 'green')
    square(foodN.x,foodN.y, 9, 'green')
    update()
    # si se introduce 0, es la velocidad más lenta
    if vel == "0" :
        ontimer(move,300)
    # si se introduce 1, es la velocidad media
    elif vel == "1" :
        ontimer(move, 150)
    # si se introduce 0, es la velocidad más rápida
    elif vel == "2" :
        ontimer(move, 20)
    # si se introduce cualquier valor fuera de los 3 válidos (3 anteriores), se manda un mensaje y se termina el programa
    else:
        print("favor de meter un valor dentro del rango 0-2")
        exit(0)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
#newx, newy = canvas.winfo_pointerxy()
#onclick(food(x,y))

#onscreenclick(food)
onscreenclick(findcoords,1)
move()
done()
<<<<<<< HEAD:snake_velocidad.py
=======

>>>>>>> origin/JaredBranch:Snake.py
