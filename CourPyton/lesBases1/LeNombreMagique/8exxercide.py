import random

def demander_nombre(NOMBRE_MAX, NOMBRE_MIN):
    nombre_user = 0
    NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)  # Génération du nombre magique
    
    for i in range(NOMBRE_DE_VIE):
        vie = NOMBRE_DE_VIE - i  # Mise à jour du nombre de vies restantes
        print(f"Il vous reste {vie} vie.")
        
        try:
            nombre_user = float(input(f"Quel est le nombre magique entre {NOMBRE_MIN} et {NOMBRE_MAX} : "))

            # Vérification de la plage des nombres
            if nombre_user < NOMBRE_MIN or nombre_user > NOMBRE_MAX:
                print(f"ERREUR : Vous devez entrer un nombre entre {NOMBRE_MIN} et {NOMBRE_MAX}. Recommencez.")


            # Comparaison avec le nombre magique
            if nombre_user > NOMBRE_MAGIQUE:
                print("Le nombre est trop grand. Recommencez.")
            elif nombre_user < NOMBRE_MAGIQUE:
                print("Le nombre est trop petit. Recommencez.")
            else:
                print("Bravo ! Vous avez trouvé le nombre magique !")
                break
        
        except ValueError:
            print("ERREUR : Vous devez entrer un nombre valide. Recommencez.")

        # Si aucune vie restante après la boucle
        if vie == 1 and nombre_user != NOMBRE_MAGIQUE:
            print(f"Vous avez perdu ! Le nombre magique était {NOMBRE_MAGIQUE}.")
            break

# Paramètres principaux
NOMBRE_DE_VIE = 10
NOMBRE_MIN = 1
NOMBRE_MAX = 450

demander_nombre(NOMBRE_MAX, NOMBRE_MIN)

#correction 
''''gagne = False
for i in range(0, NB_VIES):
    vies = NB_VIES-i
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
        gagne = True
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
    else:
        print("Le nombre magique est plus grand")

if not gagne:
    print(f"Vous avez perdu! Le nombre magique était: {NOMBRE_MAGIQUE}")'''''



''''def demander_nombre(nb_min, nb_max):
    # quel est le nombre magique (entre 1 et 10)
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Le nombre doit être entre {nb_min} et {nb_max}. Réessayez.")
                nombre_int = 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4

"""nombre = 0
vies = NB_VIES
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies -= 1
    else:
        print("Le nombre magique est plus grand")
        vies -= 1

if vies == 0:
    print(f"Vous avez perdu! Le nombre magique était: {NOMBRE_MAGIQUE}")"""'''