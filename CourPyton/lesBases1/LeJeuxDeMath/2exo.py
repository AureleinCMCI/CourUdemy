#exerice , il fallais posé 4 question , on a donc utilisé une variable
#NBquestion avec 4 , un boucle for pour posé plusieur fois la méme question ! 
# 2  maniere ci-dessous de faire , 1 la mienne 2 celle du correcteur 



import random
NombreMax = 10
NombreMin = 1 
NbQuestion = 4
def poser_questionCorect():
    
  NombreQuestionRestante = NbQuestion
  for _ in range(NbQuestion):
    print(f"Il vous reste {NombreQuestionRestante} question.")
    a = random.randint(NombreMin, NombreMax) 
    b = random.randint(NombreMin, NombreMax)
    
    reponce_str = input(f"calculez {a} + {b} = ")
    reponce = int(reponce_str)
    
    
    if reponce == a + b:
         print("Bravo vous avez gagné")
         NombreQuestionRestante -= 1
    else:
        print(f"Désolé, vous avez perdu. La bonne réponse était {a + b}.")
        NombreQuestionRestante -= 1
        
poser_questionCorect()

###################################################CORECTION#####################
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
        
        
        
        
for i in range(0,NbQuestion):
    print(f"question n°{i+1}, sur {NbQuestion}: ")
    poser_questionCorect()
    
    
    