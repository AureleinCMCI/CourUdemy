def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Veuillez entrer votre nom : ")
    return nom


def demander_age2(nom_personne): #Oui, tu as tout à fait raison ! Le fait de mettre nom_personne comme paramètre dans la fonction demander_age2 permet de rendre cette fonction plus flexible et réutilisable. Cela permet d'utiliser cette fonction pour demander 
    #l'âge de plusieurs personnes, en personnalisant l'invite avec leur nom respectif.
    age = 0
    while age == 0:
        age_str = input(nom_personne + "quel est votre age ? ") 
        try:
            age = int(age_str) + 1
        except:
            print("ERRER : Veuillez saisir un nombre pour l'age ")
    return age

nom1 = demander_nom()
nom2 = demander_nom()

age = demander_age2(nom1)
age2 = demander_age2(nom2)
print("Bonjour " + nom1 + " vous avez " + str(age) + " ans." + "et l'anner prochaine vous aureé " +  str(age + 1) + " ans")
print("Bonjour " + nom2 + " vous avez " + str(age) + " ans." + "et l'anner prochaine vous aureé " +  str(age + 1) + " ans")