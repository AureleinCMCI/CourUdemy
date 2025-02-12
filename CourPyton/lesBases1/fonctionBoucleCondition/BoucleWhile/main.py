
n = 0

while n <= 10:
    print("valeur de n: " + str(n))  # n est initialisé a 0 ; on va donc continuer la boucle jusqu'a arrivé a 10 !
    n = n + 1 #on incremente de 1 
    

mot_de_passe = " "    


 #while not mot_de_passe == "TOTO":
#    mot_de_passe = str(input("Quel est votre mot de passe "))
#     if mot_de_passe != "TOTO":
#        print("Veuillez ressaisir votre mot de passe, celui-ci est incorrect.")
# print("Connexion réussie")

# while not mot_de_passe == 758:
  #   mot_de_passe = int(input("Quel est votre  2 mot de passe "))
 #    if mot_de_passe != 758:
   #      print("Veuillez ressaisir votre mot de passe, celui-ci est incorrect.")
# print("Connexion réussie")
nom = input("quel est votre nom ?")

ageProchain = 0
while ageProchain == 0:
        age = input("quel est votre age ? ")
        try:
            ageProchain = int(age) + 1
        except:
            print("Veuillez saisir un nombre pour l'age ")
print("Bonjour " + nom + " vous avez " + age + " ans." + "et l'anner prochaine vous aureé " +  str(ageProchain) + " ans")



nom = input("quel est votre nom ?")

age = 0
while age == 0:
        age_str = input("quel est votre age ? ")
        try:
            age = int(age_str) + 1
        except:
            print("Veuillez saisir un nombre pour l'age ")
print("Bonjour " + nom + " vous avez " + str(age) + " ans." + "et l'anner prochaine vous aureé " +  str(age + 1) + " ans")