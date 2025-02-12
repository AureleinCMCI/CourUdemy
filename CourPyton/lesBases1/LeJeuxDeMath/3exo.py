#exerice , il fallais posé 4 question , on a donc utilisé une variable
#NBquestion avec 4 , un boucle for pour posé plusieur fois la méme question ! 
# 2  maniere ci-dessous de faire , 1 la mienne 2 celle du correcteur 



import random

NbQuestion = 4

'''def poser_question():
    NombreMax = 10
    NombreMin = 1 
    
    a = random.randint(NombreMin, NombreMax) 
    b = random.randint(NombreMin, NombreMax)
    
    reponce_str = input(f"calculez {a} + {b} = ")
    reponce = int(reponce_str)
    
    if reponce == a + b:
         print("Bravo vous avez gagné")
         return True
    else:
        print(f"Désolé, vous avez perdu. La bonne réponse était {a + b}.")
        return False
        


nb_point = 0
for i in range(0, NbQuestion):
    print(f"Question n°{i+1}, sur {NbQuestion}: ")
    
    # Appel de la fonction pour poser la question
    if poser_question():
        nb_point += 1  # Incrémentez le nombre de points si la réponse est
        #donc cela sera incrementé seulement si l'utilisateur va areturner true 
    
    print(f"Vous avez actuellement {nb_point} point sur {NbQuestion}.")'''
    
    
###########################----------CORRECTION-------------------------------#############################




def poser_questionCorect():
    NombreMax = 10
    NombreMin = 1 
    
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
    
print(f"vous avez une note de {nb_point}/{NbQuestion}")
