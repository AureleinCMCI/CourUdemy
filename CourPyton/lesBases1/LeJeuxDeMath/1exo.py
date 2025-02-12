import random



# La question a poser est : Calculer 1 + 5 = 1 et 5 se sont des nobmre alléatoire que je dois définire
# je dois tirer au sort 2 nombre a et b 
# je dois ducoup demadner la reponce a l'utilisateur et la reponce dois etre egale a a + b 
'''def poser_question():
    NombreMax = 10
    NombreMin = 1 
    
    a = random.randint(NombreMin, NombreMax) 
    b = random.randint(NombreMin, NombreMax)

    reponce = input("Calculer le nombre ")
    
    if reponce == a + b :
        print("Bravo vous avez gagné")
    else :
        print(f"Désolé, vous avez perdu. La bonne réponse était {a + b}.")
poser_question()'''
#correction 

def poser_questionCorect():
    NombreMax = 10
    NombreMin = 1 
    
    a = random.randint(NombreMin, NombreMax) 
    b = random.randint(NombreMin, NombreMax)
    
    reponce_str = input(f"calculez {a} + {b} = ")
    reponce = int(reponce_str)
    
    if reponce == a + b:
         print("Bravo vous avez gagné")
    else:
        print(f"Désolé, vous avez perdu. La bonne réponse était {a + b}.")
poser_questionCorect()