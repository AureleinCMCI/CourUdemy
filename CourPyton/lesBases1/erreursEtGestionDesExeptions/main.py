"""Premier programme
Formation Python
apprendre la programmation"""

nom = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")

try:
    age_prochain = int(age) + 1 #le int nous oblige a rentre une int 
except ValueError:
    print("Erreur: vous devez rentrez un nombre") 
else:
    print("Bonjour " + nom + " vous avez " + str(age) + " ans." + str(age_prochain))



