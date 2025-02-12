


def demander_nom():
    reponce_nom= ""
    while reponce_nom == "":
        reponce_nom = input("Veuillez entrer votre nom : ")
    return reponce_nom


def demander_age():
    age = 0
    while age == 0:
        age_str = input("quel est votre age ? ")
        try:
            age = int(age_str) + 1
        except:
            print("ERRER : Veuillez saisir un nombre pour l'age ")
    return age



reponce_nom = demander_nom()
age = demander_age()

print("Bonjour " + reponce_nom + " vous avez " + str(age) + " ans." + "et l'anner prochaine vous aureé " +  str(age + 1) + " ans")

# La fonction va commencer par lir le code #
#nom = ""
#while nom == "":
 #       nom= input("Quel est votre nom")
        