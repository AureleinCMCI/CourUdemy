"""Premier programme
Formation Python
apprendre la programmation"""

def afficher_informations_personne(nom, age , taille = 0):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")#methode classic 
    print(f"Vous vous appelez {nom} , vous avez {age} ans") #le f devand pour dire que c'est foramter ,
    print("Vous vous appelez %s , vous avez %s ans" % (nom , age)) #voici une autre methode 
    
    
    print("L'an prochain vous aurez " + str(age+1) + " ans") #c'est ici q'uon définie les chaine formater 
    print("L'an prochain vous aurez %s ans" % (age + 1))

#afficher du texte sur plusieur ligne 
    print(""" 
            vous 
            pouveza
                    aficher 
                    azdkjsk
            fjh        
          """)
    print("toto",45,"ma",78.65) # aps besoin de str car on a juste palcer différent arguement a print
    
#############################################################RESTE DU CODE ########################################################################
    # == egal
    # < inférieur
    # <= inférieur ou égal
    # > supérieur
    # >= supérieur ou égal
    # True / False (Boolean)
    if age == 17:
        print("Vous êtres presque majeur")
    elif 12 <= age < 18:
        print("Vous êtes adolescent")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé")
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

    if not taille == 0 :
        print("votre taille : " + str(taille) + "m")
    
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
#nom1 = demander_nom()
#nom2 = demander_nom()

# demander l'age
#age1 = demander_age(nom1)
#age2 = demander_age(nom2)

# Afficher les résultats
#afficher_informations_personne(nom1, age1)
#afficher_informations_personne(nom2, age2)

                             # for
                             
NB_PERSONNE = 4
for i in range(0 , NB_PERSONNE ):
    nom = "personne" + str(i + 1)
    age = demander_age(nom)
    afficher_informations_personne(nom , age,1.56)

