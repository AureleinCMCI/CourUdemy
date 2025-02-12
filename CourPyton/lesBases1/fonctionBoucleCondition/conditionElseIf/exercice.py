"""Premier programme
Formation Python
apprendre la programmation"""

def afficher_informations_personne(nom, age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")

   # if age >= 18:
   #     print("vous etes majeur")
#else:
 #       print("vous etes mineur ")
        
        # OU ON PEUS FAIRE 
    # condition = age >= 18
    # if condition:
    #   print("vous etes majeur")
    #else:
   #  print("vous etes mineur ")
            
        # AUTRE CONDITION 

    if  age == 17:
        print("vous etes presque majeur")
    elif age == 18:
        print("tou juste majeur ")
    elif age > 60:
        print("vous estes Seignor")
    elif age < 10:
        print("vous etes un enfant")
    elif age >= 18:
        print("vous este majeur")
    else :
        print("vous etes mineur")
        
        


        
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
nom3 = demander_nom()
nom4 = demander_nom()
nom5 = demander_nom()
nom6 = demander_nom()
# demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)
age3 = demander_age(nom3)
age4 = demander_age(nom4)
age5 = demander_age(nom5)
age6 = demander_age(nom6)


# Afficher les résultats
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)
afficher_informations_personne(nom3, age3)
afficher_informations_personne(nom4, age4)
afficher_informations_personne(nom5, age5)
afficher_informations_personne(nom6, age6)


#ccccccccoooooooooooooreeccctionnnn
"""Premier programme
Formation Python
apprendre la programmation"""

def afficher_informations_personne(nom, age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")

    # == egal
    # < inférieur
    # <= inférieur ou égal
    # > supérieur
    # >= supérieur ou égal
    # True / False (Boolean)
    if age == 17:
        print("Vous êtres presque majeur")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age > 60:
        print("Vous êtes sénior")
    elif age < 10:
        print("Vous êtes enfant")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")


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


