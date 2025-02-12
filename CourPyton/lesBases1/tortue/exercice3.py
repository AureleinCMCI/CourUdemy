import turtle

tortue = turtle.Turtle()
taille = 100
def carer(taille, n):
    for i in range(n):
        tortue.forward(taille)
        tortue.left(90)
carer(taille, 4)


#correction
def carer(taille):
    for i in range(0,4):
        tortue.forward(taille)
        tortue.left(90)
tortue = turtle.Turtle()
carer(400)

turtle.done()
