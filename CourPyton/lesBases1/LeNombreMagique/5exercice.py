#NOUVEAUX ? CAS d'erreur 
 #except ValueError:
  #          print("ERREUR, vous devez entrer un nombre")
   #     else:
    #        if nombre_user < NOMBRE_MIN or nombre_user > NOMBRE_MAX:
     #           print(f"ERREUR, vous devez entrer un nombre entre {NOMBRE_MIN} et {NOMBRE_MAX} ,  recommencer ")

def demander_nombre(NOMBRE_MAX, NOMBRE_MIN):
    nombre_user = 0
    while not  nombre_user == NOMBRE_MAGIQUE:
        try:
            nombre_user = float(input(f"Quel est le nombre magique entre  {NOMBRE_MIN} et {NOMBRE_MAX} : "))
            if nombre_user > NOMBRE_MAGIQUE : 
                print("Le nombre est trop grand , recommencez")
            elif nombre_user < NOMBRE_MAGIQUE :
                    print('le nombre est trop petit , recommencer')
            elif nombre_user == NOMBRE_MAGIQUE :
                    print('Bravo !')
        except ValueError:
            print("ERREUR, vous devez entrer un nombre")
        else:
            if nombre_user < NOMBRE_MIN or nombre_user > NOMBRE_MAX:
                print(f"ERREUR, vous devez entrer un nombre entre {NOMBRE_MIN} et {NOMBRE_MAX} ,  recommencer ")
    return nombre_user
    

NOMBRE_MAGIQUE = 5
NOMBRE_MIN = 1 
NOMBRE_MAX = 20
nobmre = demander_nombre(NOMBRE_MAX, NOMBRE_MIN)