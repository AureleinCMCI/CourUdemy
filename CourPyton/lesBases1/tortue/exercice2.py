import turtle

tortue = turtle.Turtle()
taille = 30
def escalier(taille, n):
    for i in range(n):
        tortue.forward(taille)
        tortue.left(90)
        tortue.forward(taille)
        tortue.right(90)
escalier(taille, 5)

turtle.done()