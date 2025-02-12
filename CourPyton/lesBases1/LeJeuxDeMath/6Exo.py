import random
#ici j'ai donna a l'utilisateur le choix du niveaux de dificulter 
niveaux = input("quel niveaux voulez vous vous avez le choix entre facile , intermediaire , dificile , extreme: \n")
if niveaux == "facile":
    NbQuestion = 10
    NombreMax = 10 
    NombreMin = 1
elif niveaux == "intermediaire":
    NbQuestion = 10
    NombreMax = 50
    NombreMin = 1
elif niveaux == "dificile":
    NbQuestion = 10
    NombreMax = 100
    NombreMin = 50
elif niveaux == "extreme":
    NbQuestion = 10
    NombreMax = 1000
    NombreMin = 450
else:
    print("Niveau non reconnu ! Veuillez choisir entre : facile, intermediaire, dificile, ou extreme.")
def poser_questionCorect():
    a = random.randint(NombreMin, NombreMax)
    b = random.randint(NombreMin, NombreMax)
    
    o = random.randint(0, 2)
    

    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    elif o == 2:
        operateur_str = "-"
    

    reponce_str = input(f"Calculez {a} {operateur_str} {b} = ")
    reponce = int(reponce_str)
    
    calcule = a + b
    if o == 1:
        calcule = a * b
    elif o == 2:
        calcule = a - b
    
    # Vérifier la réponse
    if reponce == calcule:
        return True, calcule
    else:
        return False, calcule

nb_point = 0
for i in range(NbQuestion):
    print(f"Question n°{i+1} sur {NbQuestion}: ")
    
    # Appel de la fonction pour poser la question
    est_correct, reponse_correcte = poser_questionCorect()
    if est_correct:
        print("Bravo, vous avez gagné!")
        nb_point += 1
    else:
        print(f"Désolé, vous avez perdu. La réponse correcte était {reponse_correcte}.")
    print(f"Vous avez actuellement {nb_point} point(s) sur {NbQuestion}.")
    print()

# Résultat final
print(f"Vous avez une note de {nb_point}/{NbQuestion}.")

moyenne = int(NbQuestion/2)
print(f"Vous avez une moyenne de {moyenne}.")
if nb_point == NbQuestion:
    print(f"Félicitations, vous avez obtenu {nb_point}/{NbQuestion}. Vous êtes excellent!")
elif nb_point == 0:
    print(f"Vous avez eu {nb_point}. Il faudra réviser vos maths.")
elif nb_point > moyenne:
    print("Pas mal!")
elif nb_point < moyenne:
    print("Peut mieux faire.")
