import turtle #Cette ligne importe le module turtle qui contient toutes les fonctions nécessaires pour dessiner des graphiques

tortue = turtle.Turtle()


tortue.forward(100)#avancer de 100 pixel 
tortue.left(90)# tourner de 90 degrés vers la gauche 
tortue.forward(50)#avancer de 50 pixel
tortue.backward(100)# reculer de 100 pixel
tortue.right(90)#tourner de 90 degrés vers la droite

turtle.done() 
#Cette ligne indique à Python que nous avons terminé de dessiner et que la fenêtre
 #graphique peut rester ouverte. Sans cette ligne, la fenêtre se fermerait immédiatement après l'exécution du script.



