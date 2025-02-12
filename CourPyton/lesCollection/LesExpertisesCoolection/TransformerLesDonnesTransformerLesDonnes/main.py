# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions
###################################################################Exercice 1############################################################################################
"""""
def poser_question(titre_question):
    # Extraire les données de la question
    question = titre_question[0]
    r1 = titre_question[1][0]
    r2 = titre_question[1][1]
    r3 = titre_question[1][2]
    r4 = titre_question[1][3]
    choix_bonne_reponse = titre_question[2]
    global score

    # Afficher la question et les choix
    print("QUESTION")
    print("  " + question)
    print("  (a)", r1)
    print("  (b)", r2)
    print("  (c)", r3)
    print("  (d)", r4)
    print()

    # Demander une réponse
    reponse = input("Votre réponse (a, b, c, d) : ").strip().lower()
    if reponse == choix_bonne_reponse:
        print("Bonne réponse!")
        score += 1
    else:
        print(f"Mauvaise réponse. La bonne réponse était : {choix_bonne_reponse}")
    print()


# Initialiser les questions et le score
questions = [
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "c"),
    ("Quelle est la capitale de l'Allemagne ?", ("Berlin", "Munich", "Francfort", "Hambourg"), "a"),
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "a"),
    ("Quelle est la capitale de l'Espagne ?", ("Barcelone", "Madrid", "Séville", "Valence"), "b"),
]

score = 0  # Initialiser le score

# Poser chaque question
for question in questions:
    poser_question(question)

# Afficher le score final
print(f"Votre score final est : {score}/{len(questions)}")"""""
##########################CORRECTION############################################################################################################
"""def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    global score
    
    print("QUESTION")
    print("  " + question[0])
    print("  ", choix[0])
    print("  ", choix[1])
    print("  ", choix[2])
    print("  ", choix[3])
    print()
    reponse = input("Votre réponse : ")
    if reponse.lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        
    print()


score = 0


question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)




poser_question(question2)
# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)"""""
###################################################EXERCICE 2############################################################################################################
#ajouté une boucle for pour les question :

"""def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    
    global score
    
    print("QUESTION")
    
    print("  " + question[0])
    for i in choix:
         print(i)
    print()
    

    
    reponse = input("Votre réponse : ")
    if reponse.lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse , la bonne réponse était : ", bonne_reponse)
        
    print()


score = 0


question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)
poser_question(question2)
# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)"""
###################################################Correction############################################################################################################
"""def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    
    global score
    
    print("QUESTION")
    
    print("  " + question[0])
    for i in range(len(choix)):
         print(choix[i])
    print()
    

    
    reponse = input("Votre réponse : ")
    if reponse.lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse , la bonne réponse était : ", bonne_reponse)
        
    print()


score = 0


question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)
poser_question(question2)
# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)"""
###################################################EXERCICE 3############################################################################################################
"""def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    
    global score
    
    print("QUESTION")
    
    print("  " + question[0])
    for i in range(len(choix)):
         print(choix[i])
    print()
    

    
    reponse = input("Votre réponse : ")
    if reponse.lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse , la bonne réponse était : ", bonne_reponse)
        
    print()


score = 0


question1 = ("Quelle est la capitale de la France ?", ("1-Marseille", "2-Nice", "1-3Paris", "1-4Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)
poser_question(question2)
# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)"""""
###################################################Correction############################################################################################################

"""def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    
    global score
    
    print("QUESTION")
    
    print("  " + question[0])
    for i in range(len(choix)):
         print(" ", i+1 ,"-",choix[i])
    print()
    

    
    reponse_str = input("Votre réponse : (entre 1 et " + str(len(choix)) + ") ")
    
    reponce_int = int(reponse_str)
    choix[reponce_int - 1]
    
    
    if choix[reponce_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse , la bonne réponse était : ", bonne_reponse)
        
    print()


    
score = 0


question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes","lile"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)
poser_question(question2)
# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)"""""
###################################################EXERCICE 3 - definition de al fonction demander_reponce_numerique utilisater############################################################################################################
#la gestion des erreurs
"""""
def demander_reponse_numerique(min, max):
    reponse_str = input(f"Votre réponse (entre {min} et {max}) : ")
    
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        else:
            print(f"ERREUR:Veuillez entrer un nombre entre {min} et {max}.")
    except ValueError:
            print("ETRREUR: Veuillez entrer uniquement des chiffres.")
    
    return demander_reponse_numerique(min, max)
    
def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    
    global score
    
    print("QUESTION")
    
    print("  " + question[0])
    for i in range(len(choix)):
         print(" ", i+1 ,"-",choix[i])
    print()
    
    reponce_int = demander_reponse_numerique(1, len(choix))

    
    
    if choix[reponce_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse , la bonne réponse était : ", bonne_reponse)
        
    print()


    
score = 0


question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes","lile"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)
poser_question(question2)
# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)"""
###################################################FINALE############################################################################################################
# lancer_questionnaire(questionnaire)

#on va finir cela , questionnaire sera ducoup une liste de question
def demander_reponse_numerique(min, max):
    reponse_str = input(f"Votre réponse (entre {min} et {max}) : ")
    
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        else:
            print(f"ERREUR:Veuillez entrer un nombre entre {min} et {max}.")
    except ValueError:
            print("ETRREUR: Veuillez entrer uniquement des chiffres.")
    
    return demander_reponse_numerique(min, max)
    
def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    
    
    print("QUESTION")
    
    print("  " + question[0])
    for i in range(len(choix)):
         print(" ", i+1 ,"-",choix[i])
    print()
    
    
    
    resultat_personne_correct = False
    reponce_int = demander_reponse_numerique(1, len(choix))
    if choix[reponce_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        resultat_personne_correct = True
    else:
        print("Mauvaise réponse , la bonne réponse était : ", bonne_reponse)
        
    print()
    return resultat_personne_correct 

    
score = 0

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score final :", score ,"sur", len(questionnaire))

questionnnaires = (
    

    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"),
    ("Quelle est la capitale de l'Allemagne ?", ("Berlin", "Munich", "Francfort", "Hambourg"), "Berlin"),
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Rome", "Venise", "Pise", "Florence", "Bruxelles"), "Bruxelles")
)
            

lancer_questionnaire(questionnnaires)

# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

