"""Premier programme
Formation Python
apprendre la programmation"""

nom = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")

age_prochain = int(age) + 1 #ici on a converti le age en INT , car sinon on ne peux pas l
#sa sera valite pour abdc car dans age , nous somme obligé de rentre des nombre , car ON LA CONVERTIE EN INT
print("Bonjour " + nom + " vous avez " + str(age) + " ans." + str(age_prochain))



