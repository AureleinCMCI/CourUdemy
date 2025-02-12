#ICI , on améliore le code en rajoutant l'aléatoire et la multiplicaton ,
# c'est tiré au sort pour savoir si on multiplie , soustrai ou additione 


import random

NbQuestion = 10
NombreMax = 100# a*la modification de ces CONSTANTE vont changé tous le programe , on peux en autre
# définir le niveaux de dificulte du jeux ici 
NombreMin = 1

def poser_questionCorect():


    a = random.randint(NombreMin, NombreMax) 
    b = random.randint(NombreMin, NombreMax)
    
    o = random.randint(0 ,2) # génere un nombre entre  0 et 2 , donc o sera egale a 0 ou 1 ou 2 a , cela change a chaque fois que la fonction recommence 
    
    # si on tire au sort 0 sa sera une multiplication 
    # si c'est 1 ca cera une addition
     
    operateur_str = "+" # initialisé de base a 0 
    if  o == 1: # si o est égale a 1 on va multiplie 
        operateur_str = "*" # 
    elif o == 2: 
        operateur_str = "-" #idem on soustrait 
    reponce_str = input(f"calculez {a} {operateur_str} {b} = ")
    reponce = int(reponce_str)
    
    
    calcule = a + b
    if o == 1:
        calcule = a * b
    elif o == 2 :
        calcule = a - b 
    if reponce == calcule: 
        return True
    else:
        return False

    
nb_point = 0
for i in range(0, NbQuestion):
    
    print(f"Question n°{i+1}, sur {NbQuestion}: ")
        
    # Appel de la fonction pour poser la question
    if poser_questionCorect():
        print("Bravo vous avez gagné")
        nb_point += 1  # Incrémentez le nombre de points si la réponse est
        #donc cela sera incrementé seulement si l'utilisateur va areturner true 
    else : 
        print("Désolé, vous avez perdu")
    print()

    print(f"Vous avez actuellement {nb_point} point sur {NbQuestion}.")
    print()

print(f"vous avez une note de {nb_point}/{NbQuestion}")


moyenne = int(NbQuestion/2)
print(f"Vous avez une moyenne de {moyenne}")
if nb_point ==  NbQuestion:
    print(f"Félicitation vous avez obtenu {nb_point}/{NbQuestion}, vous êtes excellent !")
elif nb_point == 0:
    print(f"vous avez eu {nb_point} il faudra reviser vos math")
elif nb_point > moyenne:
    print("Pas mal")
elif nb_point < moyenne:
    print("peux mieux faire")
    