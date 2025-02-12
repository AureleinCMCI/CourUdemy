import random

# Demander le niveau de difficulté à l'utilisateur
niveaux = input("Quel niveau de difficulté voulez-vous (facile, intermediaire, dificile, extreme) ? ").strip().lower()

# Initialisation des paramètres en fonction du niveau choisi
if niveaux == "facile":
    NbQuestion = 10
    NombreMax = 10
    NombreMin = 1
    operateurs = ["+"]
elif niveaux == "intermediaire":
    NbQuestion = 10
    NombreMax = 50
    NombreMin = 1
    operateurs = ["+", "-"]
elif niveaux == "dificile":
    NbQuestion = 10
    NombreMax = 100
    NombreMin = 1
    operateurs = ["+", "-", "*"]
elif niveaux == "extreme":
    NbQuestion = 10
    NombreMax = 1000
    NombreMin = 450
    operateurs = ["+", "-", "*"," /"]
else:
    print("Niveau non reconnu ! Niveau par défaut : facile.")
    NbQuestion = 10
    NombreMax = 10
    NombreMin = 1
    operateurs = ["+"]  # Par défaut, seulement l'addition

# Fonction pour poser une question
def poser_questionCorect():
    a = random.randint(NombreMin, NombreMax)
    b = random.randint(NombreMin, NombreMax)
    
    # Choisir un opérateur valide pour le niveau
    operateur_str = random.choice(operateurs)
    
    # Poser la question
    reponce_str = input(f"Calculez {a} {operateur_str} {b} = ")
    try:
        reponce = int(reponce_str)
    except ValueError:
        print("Entrée invalide ! Assurez-vous de saisir un nombre entier.")
        return False, None
    

    if operateur_str == "+":
        calcule = a + b
    elif operateur_str == "-":
        calcule = a - b
    elif operateur_str == "*":
        calcule = a * b
    elif operateur_str =="/":
        calcule = a / b
    else:
        calcule = None  # Sécurité, bien que cela ne devrait jamais arriver


    if reponce == calcule:
        return True, calcule
    else:
        return False, calcule

nb_point = 0
for i in range(NbQuestion):
    print(f"Question n°{i+1} sur {NbQuestion}: ")
    

    est_correct, reponse_correcte = poser_questionCorect()
    if est_correct:
        print("Bravo, vous avez gagné !")
        nb_point += 1
    else:
        print(f"Désolé, vous avez perdu. La réponse correcte était {reponse_correcte}.")
    print(f"Vous avez actuellement {nb_point} point(s) sur {NbQuestion}.")
    print()


print(f"Vous avez une note de {nb_point}/{NbQuestion}.")


moyenne = int(NbQuestion/2)
print(f"Vous avez une moyenne de {moyenne}.")
if nb_point == NbQuestion:
    print(f"Félicitations, vous avez obtenu {nb_point}/{NbQuestion}. Vous êtes excellent !")
elif nb_point == 0:
    print(f"Vous avez eu {nb_point}. Il faudra réviser vos maths.")
elif nb_point > moyenne:
    print("Pas mal !")
elif nb_point < moyenne:
    print("Peut mieux faire.")
