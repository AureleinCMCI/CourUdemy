nom = input("quel est votre nom ?")

age = 0
while age == 0:
        age_str = input("quel est votre age ? ")
        try:
            age = int(age_str) + 1 #si on rentre un int il va convertir age avec la valeur entrer dans  la variable age_str
        except:
            print("Veuillez saisir un nombre pour l'age ")
print("Bonjour " + nom + " vous avez " + str(age) + " ans." + "et l'anner prochaine vous aureé " +  str(age + 1) + " ans")