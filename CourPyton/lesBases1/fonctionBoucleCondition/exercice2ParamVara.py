

def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Veuillez entrer votre nom : ")
    return nom 


def demander_numéro():
    tel = ""
    while len(tel) < 10 or not tel.isdigit():  # On vérifie que la longueur est >= 10 et que le tel est un nombre
        tel = input("Veuillez entrer un numéro de téléphone de minimum 10 chiffres : ")
        if len(tel) < 10:
            print("ERREUR : Le numéro doit comporter au moins 10 chiffres.")
        elif not tel.isdigit():
            print("ERREUR : Le numéro doit contenir uniquement des chiffres.")
    return tel


def demander_age2(): #Oui, tu as tout à fait raison ! Le fait de mettre nom_personne comme paramètre dans la fonction demander_age2 permet de rendre cette fonction plus flexible et réutilisable. Cela permet d'utiliser cette fonction pour demander 
    #l'âge de plusieurs personnes, en personnalisant l'invite avec leur nom respectif.
    age = 0
    while age == 0:
        age_str = input("quel est votre age ? ") 
        try:
            age = int(age_str)
        except:
            print("ERRER : Veuillez saisir un nombre pour l'age ")
    return age



def afficher_information_personne(nomDeLaPersonne , ageDeLaPersonne, telehponeDeLaPersonne):
    personne = nomDeLaPersonne  + " ager de " +  str(ageDeLaPersonne) + "votre numéro est le : " + str(telehponeDeLaPersonne)
    return personne 

nomDeLaPersonne = demander_nom()
ageDeLaPersonne = demander_age2()
telehponeDeLaPersonne = demander_numéro()
personne = afficher_information_personne(nomDeLaPersonne   , ageDeLaPersonne , telehponeDeLaPersonne)


print( "vos information sont " + personne)
#COOOOOOREEEEEEEEEEEEEEECCCCTIONNNNNNNNNNNNNNNNNNNNNNNNNNN

"""Premier programme
Formation Python
apprendre la programmation"""

def afficher_informations_personne(nom, age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom

def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int

#-----------------------------------------------------------------------------
            
# demander le nom
nom1 = demander_nom()
nom2 = demander_nom()

# demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# Afficher les résultats
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)


