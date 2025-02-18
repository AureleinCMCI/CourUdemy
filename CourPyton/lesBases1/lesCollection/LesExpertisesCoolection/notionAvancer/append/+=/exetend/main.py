#les Collection : listes , tuples ,
# les différence entre append/EXTEND/ += /insert

##################################AVEC APPEND############################################
print("avec append")
noms = ["Mélanie","jean","marti","Alice"]

nom_suppelementaire = ["Davie" , "mazrie"]
noms.append(nom_suppelementaire) # ici j'ai bien rajoute davie a ma liste , rajoute une liste a une liste

"""for e in nom_suppelementaire:
      noms.append(e)"""
    
print(noms)
print()
# si je veux rajouter une liste a une autre liste
##################################AVEC EXTEND############################################
#: La méthode extend() en Python permet d'ajouter tous les éléments d'un itérable (comme une liste,
# un tuple, un ensemble, etc.) à la fin de la liste sur laquelle elle est appelée.
print("avec extend")
nomsExetend = ["Mélanie","jean","marti","Alice"]
nom_suppelementaireExtend = ["Davie" , "mazrie"]
nomsExetend.extend(nom_suppelementaireExtend)
print(nomsExetend)
print()
###########################################""AVEC += ############################################
#L'opérateur += est un opérateur d'addition/affectation. Il est utilisé pour ajouter un élément à une variable existante, 
# mais il fonctionne différemment selon le type de variable sur laquelle il est appliqué.
print("avec +=")
nomsPlus = ["Mélanie","jean","marti","Alice"]
nom_suppelementairePlus = ["Davie" , "mazrie"]
#nomsPlus += nom_suppelementairePlus
#nomsPlus = ["aurelien"] + nomsPlus
nomsPlus = nomsPlus + nom_suppelementairePlus
print(nomsPlus)
print()
###########################################AVEC INSERT################################
#La méthode insert() ajoute un élément à une liste à un index spécifié.
print("avec insert")
nomsInsert = ["Mélanie","jean","marti","Alice"]
nom_suppelementaireInsert = ["Davie" , "mazrie"]
nomsInsert.insert(0,"Davie")
print(nomsInsert)
