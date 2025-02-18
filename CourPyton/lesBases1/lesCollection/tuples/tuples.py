#Collection , tableaux , listes , Tuples ... 
# contenire plusieurs éléments 

#liste []: Mutable -> modifiable : rajouter/supprimer des éléments ou les modifiérs
#tuples : personnes = ("Mélanie","jean","marti","Alice ") 

a = 5 
b = "toto"

personnes = ("Mélanie","jean","marti","Alice ") #ici j'ai crée un tuples ! 
#print(personnes[3])# est égale a alice  
#print(personnes[-1])


#c'est comment le principe d'un tableau , je récupére le premier element qui est mélanie 
#le dernier élement est Alice = 3 car on commence a partir de l'index 0 
#for i in range(0,len(personnes)):
#   print(personnes[i]) #je parcours le tuples avec un for et je récupére
#for i in personnes:
#   print(i)
#   print(len(i))
#   print(i[0])
valeur = range(0,10)
print(valeur[-1])