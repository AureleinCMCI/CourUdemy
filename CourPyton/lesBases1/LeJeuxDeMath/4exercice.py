#ICI , on va rajouté un condition , Si la note est 2 4/4 afficher exxelent , si c'est 0 , réviser vos math 
# si c'est 


import random

NbQuestion = 4
NombreMax = 10
NombreMin = 1

def poser_questionCorect():


    a = random.randint(NombreMin, NombreMax) 
    b = random.randint(NombreMin, NombreMax)
    
    reponce_str = input(f"calculez {a} + {b} = ")
    reponce = int(reponce_str)
    
    if reponce == a + b: 
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
    