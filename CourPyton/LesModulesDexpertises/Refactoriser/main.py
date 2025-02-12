"""nom1 = input ("nom : ")
age1 = input("age : ")
print("personne1 est " ,nom1 , "age est ", age1 , "ans ")

nom2 = input ("nom : ")
age2 = input("age : ")
print("personne2 est " ,nom2 , "age est ", age2 , "ans ")

nom3 = input ("nom : ")
age3 = input("age : ")
print("personne3 est " ,nom3 , "age est ", age3 , "ans ")"""

"""def recuperer_et_afficher(numero_personne):
    nom = input ("Nom de la personne: " + str(numero_personne) +":")
    age = input("Age de la personne : " + str(numero_personne) +":")
    print("La personne " ,str(numero_personne) ,"est",nom, " sont age est ", age , "ans ")
    print("le nom posséde", len(nom),'caractéres')
    
recuperer_et_afficher(1)
recuperer_et_afficher(2)
recuperer_et_afficher(3)"""
#aller plus loin en hiarchie 
 
""""def recuperer_et_afficher(numero_personne):
    nom = input ("Nom de la personne: " + str(numero_personne) +":")
    age = input("Age de la personne : " + str(numero_personne) +":")
    print("La personne " ,str(numero_personne) ,"est",nom, " sont age est ", age , "ans ")
    print("le nom posséde", len(nom),'caractéres')
nb_personnes = 2

for i in range(nb_personnes):
    recuperer_et_afficher(i+1)
    
#on va fair un appel de fonction """
def est_majeur(age: int):
    if age <= 0:  # "40" <= 0
        return False
    # Vrai ou Faux (True / False)
    # si l'age >= 18 => True sinon False
    if age >= 18:
        return True
    return False


def recuperer_infos_personne(numero_personne):
    nom = input ("Nom de la personne: " + str(numero_personne) +":")
    age = input("Age de la personne : " + str(numero_personne) +":")
    return nom , age

def afficher_info(nom,age,numero_personne):
    print("La personne " ,str(numero_personne) ,"est",nom, " sont age est ", age , "ans ")
    print("le nom posséde", len(nom),'caractéres')
    if est_majeur(age):
        print("la personne est majeur")
    else:
        print("la personne est mineur")
def recuperer_et_afficher(numero_personne):
    nom,age = recuperer_infos_personne(numero_personne)
    afficher_info(nom,age,numero_personne)
    
    
nb_personnes = 2

for i in range(nb_personnes):
    recuperer_et_afficher(i+1)
afficher_info("007","james",)