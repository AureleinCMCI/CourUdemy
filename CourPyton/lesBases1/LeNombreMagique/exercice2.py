#condition 
NOMBRE_MAGIQUE = 5

NOMBRE_MIN = 1 

NOMBRE_MAX = 20

def demander_nombre(NOMBRE_MAX, NOMBRE_MIN):
    nombre_user = int(input(f"Entrez un nombre entre {NOMBRE_MIN} et {NOMBRE_MAX} : "))
    
    if nombre_user > NOMBRE_MAGIQUE : 
        print("Le nombre est trop grand")
    elif nombre_user < NOMBRE_MAGIQUE :
        print('le nombre est trop petit')
    elif nombre_user == NOMBRE_MAGIQUE :
        print('Bravo !')
        
        
    nombre_int = int(nombre_user)
    return nombre_int
nobmre = demander_nombre(NOMBRE_MAX, NOMBRE_MIN)