#les cas d'erreur try exetp
# 1. si l'utilisateur entre un nombre qui n'est pas un int  ou un float 
# cela tobmera dans l'erreur 


def demander_nombre(NOMBRE_MAX, NOMBRE_MIN):
    nombre_user = 0
    while not  nombre_user == NOMBRE_MAGIQUE:
        try:
            nombre_user = float(input(f"Entrez un nombre entre {NOMBRE_MIN} et {NOMBRE_MAX} : "))
            if nombre_user > NOMBRE_MAGIQUE : 
                print("Le nombre est trop grand , recommencez")
            elif nombre_user < NOMBRE_MAGIQUE :
                    print('le nombre est trop petit , recommencer')
            elif nombre_user == NOMBRE_MAGIQUE :
                    print('Bravo !')
        except ValueError:
            print("ERREUR, vous devez entrer un nombre")
    return nombre_user
    

NOMBRE_MAGIQUE = 5
NOMBRE_MIN = 1 
NOMBRE_MAX = 20
nobmre = demander_nombre(NOMBRE_MAX, NOMBRE_MIN)