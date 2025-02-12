
# i les plus mieux d'utilisé les variable locale ! 

# ICI on a tous simplement utilisé une variable gloable 
age = 0
reponce_nom = ""

def demander_nom():
    global reponce_nom
    while reponce_nom == "":
        reponce_nom = input("Veuillez entrer votre nom : ")

def demander_age():
    global age 
    while age == 0:
        age_str = input("quel est votre age ? ")
        try:
            age = int(age_str) + 1
        except:
            print("ERRER : Veuillez saisir un nombre pour l'age ")

demander_nom()
demander_age()

print("Bonjour " + reponce_nom + " vous avez " + str(age) + " ans." + "et l'anner prochaine vous aureé " +  str(age+ 1) + " ans")

# SANS VARIABLE GLOBALE , TULISATION DES VARIABLE LOCAL 

def demander_nom2():
    reponce_nom2= ""
    while reponce_nom2 == "":
        reponce_nom2 = input("Veuillez entrer votre nom : ")
    return reponce_nom2


def demander_age2():
    age2 = 0
    while age2 == 0:
        age_str = input("quel est votre age ? ")
        try:
            age2 = int(age_str) + 1
        except:
            print("ERRER : Veuillez saisir un nombre pour l'age ")
    return age2



reponce_nom2 = demander_nom2()
age2 = demander_age2()
print("Bonjour " + reponce_nom2 + " vous avez " + str(age2) + " ans." + "et l'anner prochaine vous aureé " +  str(age2 + 1) + " ans")
