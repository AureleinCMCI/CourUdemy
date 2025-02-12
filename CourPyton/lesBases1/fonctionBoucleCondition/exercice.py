
#Exercice , demander le nom
def demander_nom():
    reponce_nom= ""
    while reponce_nom == "":
        reponce_nom = input("Veuillez entrer votre nom : ")
    return reponce_nom
reponce_nom = demander_nom()



print("Bonjour " + reponce_nom)

#corection 
def demander_nomC():
    reponce_nom= ""
    while reponce_nom == "":
        reponce_nom = input("Veuillez entrer votre nom : ")
    return reponce_nom
    