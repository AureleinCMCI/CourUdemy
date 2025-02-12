def demander_mot_magique():
    mot_magique = ""
    while mot_magique != "Sauver":
        mot_magique = input("entrer le mot magique :")
    return mot_magique
mot_magique = demander_mot_magique()

print("Vous avez trouvé")
#correction 


def demander_mot_magique():
    mot = ""  # Initialisation du mot
    while mot != "magique":
        mot = input("Tape le mot magique : ")
    print("Bravo, tu as trouvé le mot magique !")

# Appelle la fonction pour tester
demander_mot_magique()
