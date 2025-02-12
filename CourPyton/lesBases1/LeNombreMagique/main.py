
NOMBRE_MAGIQUE = 5 


def demander_nombre(nombre_user):
    while nombre_user != NOMBRE_MAGIQUE:
        nombre_user = int(input("Entrez un nombre : "))
        if nombre_user == NOMBRE_MAGIQUE:
            print("Bravo, vous avez trouvé le nombre magique !")
        else:
            print("Désolé, ce n'est pas le bon nombre !")
demander_nombre(nombre_user = int(input("Entrez un nombre : ")))