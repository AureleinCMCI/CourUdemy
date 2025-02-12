# ALEATOIRE  : genére le nombre d'essaie' nombre de vie 
import random

def demander_nombre(NOMBRE_MAX, NOMBRE_MIN):
    nombre_user = 0
    vie = NOMBRE_DE_VIE # itinialisatioon de la variable 
    
    while not  nombre_user == NOMBRE_MAGIQUE and vie > 0 : #utilisation pour dir que la boucle continue jusqu'a le nombre de vie n'est pas attein 0 
        print(f"il vous reste {vie} vie") #imprime le nombre de vie restant , diminue a chaque fois que la boucle recommence
        try:
            nombre_user = float(input(f"Quel est le nombre magique entre  {NOMBRE_MIN} et {NOMBRE_MAX} : "))
            if nombre_user > NOMBRE_MAGIQUE : 
                    print("Le nombre est trop grand , recommencez")
                    vie -= 1 # - 1 vie a chaque fois que on tombe dans le cas trop grand
                    if vie == 0:
                        print(f"vous avez perdu le nombre magique était {NOMBRE_MAGIQUE}")
            else:
                if  nombre_user < NOMBRE_MAGIQUE :
                    print('le nombre est trop petit , recommencer')
                    
                    vie -= 1  # pareil pour le cas trop petit 
                    if vie == 0:
                        print(f"vous avez perdu le nombre magique était {NOMBRE_MAGIQUE}")
                        
                else: 
                    if nombre_user == NOMBRE_MAGIQUE :
                        print('Bravo !')
        except ValueError:
            print("ERREUR, vous devez entrer un nombre")
        else:
            if nombre_user < NOMBRE_MIN or nombre_user > NOMBRE_MAX:
                print(f"ERREUR, vous devez entrer un nombre entre {NOMBRE_MIN} et {NOMBRE_MAX} ,  recommencer ")
                
                
    return nombre_user
    
NOMBRE_DE_VIE = 10 # definition des nombre de vie 

NOMBRE_MAGIQUE = random.randint(1,450)
NOMBRE_MIN = 1 
NOMBRE_MAX = 450
nobmre = demander_nombre(NOMBRE_MAX, NOMBRE_MIN)