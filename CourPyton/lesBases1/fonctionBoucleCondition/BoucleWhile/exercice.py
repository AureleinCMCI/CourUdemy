

# nom = " "
 #nom = ""
#while  nom == "":
     #   nom = input(" Vous n'avez entrer aucun nom , veuillez recommencer")
#else :
 #   print("votre nom est : " + nom)
    

# correction 
nom = ""
while nom == "":
    nom= input("Quel est votre nom")
    
    age = 0
while age == 0:
        age_str = input("quel est votre age ? ")
        try:
            age = int(age_str) + 1
        except:
            print("Veuillez saisir un nombre pour l'age ")
print("Bonjour " + nom + " vous avez " + str(age) + " ans." + "et l'anner prochaine vous aureé " +  str(age + 1) + " ans")