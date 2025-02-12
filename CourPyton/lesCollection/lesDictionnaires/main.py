#les Dictionnaaires
#les dictionnaires sont des collections non ordonnées de paires clé-valeur

#les valeur que on assoscie a nos clef peuvent etre de différent type 
'''personne = {'nom': 'melanie' , 'age': 25, 'ville': 'paris' , "taille": 1.70}

personne['age'] = 50 #modifier la valeur d'une clé
personne['poids'] = 60 #ajouter une nouvelle clé
print("le nom de la personnes est : ", personne['nom'])
print(personne['age']) 
print(personne['poids'])'''

########################################################################PARTIE 2#########################################################

personne = [
    ('melanie',25, 'paris',1.6),
    ('Paul',    25, 'paris',1.6),
    ('falla', 25, 'paris',1.6),
]

def obtenir_nom(nom,liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None
info = obtenir_nom('melanie',personne)


personne_dict = {
    "melanie": (25, 'paris',1.6),
    "Paul":(25, 'paris',1.6),
    "falla":(25, 'paris',1.6)
    
    
}
info = personne_dict.get('fallayy')
if not info:
    print("la personne n'existe pas")
else:
    print(info)