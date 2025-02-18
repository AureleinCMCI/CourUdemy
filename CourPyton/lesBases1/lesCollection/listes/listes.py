#ici on va parler des listes , les listes peuvent fair tou se que les
#tupls peuvent faire met également des choses supplémentaire 


personnes = ["Mélanie","jean","marti","Alice "]
nouvelle_personne = "Davie"


print(personnes)
personnes.append(nouvelle_personne)# ici j'ai rajouté une nouvel personnes a ma listes 

print(personnes)
print("ajout d'une personnes")
print()
#attention on ne peux pas supprimé un élement dans certain type de boucle , car si je suis entrain de boucle  sur les element 
#de ma liste et que je les  supprime en cour de route , jaurai un problémes au cour de route
del personnes[1]
print(personnes) # ici j'ai supprimé jean de la liste"""

print("suppréssion d'une personne")
print()
print("exemple avec une fonction :")
print()

def afficher_personnes(c):
    for i in c:
        print(i)
afficher_personnes(personnes)

print("modifier les valeur")

def modifier_valeur(a):
    a = 10
test = [1,2,3,4]
modifier_valeur(test)
print = []