# LISTES - EXERCICES  : DEMANDER NOMS PERSONES


# demander des noms de personnes 
#boucles infinie et sortire de la boucles quand le nom et vide == "" ==>

def demander_name():
    noms = []
    
    while True:
            name = str(input("Veuillez entrer votre nom : "))
            if name == "":
                break
        
            noms.append(name) 
    print(noms)
    
demander_name()

print("corection")
print()
##############################################correction################################################"


nom = []
while True:
    nomPersonne = input("Nom de la personne : ")
    if nomPersonne  == "":
        break
    nom.append(nomPersonne) 
print(nom)
print("nom des personnes : ")
for nomDesPersonne in nom:
    print(nomDesPersonne)
    nom.sort()#cela va trier dans l'odre Alphabéthique , selon la tale ASCII donc les amjuscule von priorisé les minuscules 
###################################################################################################################################################
