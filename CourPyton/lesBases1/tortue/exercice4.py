import turtle

tortue = turtle.Turtle()
taille = 100
def carer(taille, n):
    for i in range(n):
        tortue.forward(taille)
        tortue.left(90)
carer(taille, 4)


def carres(taille_depart,nb):
    for i in range(0,nb):
        for j in range(0,4):
            tortue.forward(taille_depart)
            tortue.left(90)
    taille_depart =  i * taille_depart
    
carres(200,1)
carres(300,1)
# corection
def carres(taille_depart, nb):
    for i in range(nb):
        taille = (i + 1) * taille_depart
        carer(taille, 4)
# Appel de la fonction pur dessiner plusieurs carrés
carres(10, 50)

turtle.done()
