
# Créer une fonction qui affiche les pizzas suivantes:
##################################################EXERCIE 1 #####################################################################
'''def afficher_pizzas():
    pizzas = ("4 fromages", "végétarienne", "hawaïenne", "calzone", "margarita")
    print("le nombre de pizzas est de :", len(pizzas))
    print()
    for i in pizzas:
        print(i)
   
afficher_pizzas()'''
##################################################CORRECTION#####################################################################
'''print("exercie 1")
def afficher_pizzas(collection):
    nb_pizzas = len(collection)
    print(f"---- LISTE DES PIZZAS ({nb_pizzas}) ----")
    for i in collection:
        print(i)
pizzas = ("4 fromages", "végétarienne", "hawaïenne", "calzone", "margarita")

afficher_pizzas(pizzas)
print()
print("exercice 2")
print()'''
###############################"EXERCICE 2############################################################################################################
#ajout du cas si la collection est vide
'''def afficher_pizzas(collection):
    
    
    nb_pizzas = len(collection)
    if nb_pizzas == 0:
        print("Aucune pizza")
        return
    print(f"---- LISTE DES PIZZAS ({nb_pizzas}) ----")
    for i in collection:
        print(i)
    print() 
    
    print("premiére pidzza:" , pizzas[0])
    print("derniére pidza :", pizzas[-1])   
    
pizzas = ("4 fromages", "végétarienne", "hawaïenne", "calzone", "margarita")

vide = ()
afficher_pizzas(vide)'''
################################################"exercice 3############################################################################################################"
#demande a l'utilisateur de rajouté une pidzaa






'''def ajouter_pizaa_utilisateur(pizzas):
    nouvelle_pizzas = input("Entrez le nom de la nouvelle pizza : ")
    pizzas = pizzas + (nouvelle_pizzas,)
    for i in pizzas:
        print(i)
    

def afficher_pizzas(collection):
    nb_pizzas = len(collection)
    
    if nb_pizzas == 0:
        print("Aucune pizza")
    else :
        print(f"---- LISTE DES PIZZAS ({nb_pizzas}) ----")
        for i in collection:
            print(i) 

pizzas = ("4 fromages", "végétarienne", "hawaïenne", "calzone", "margarita")

vide = ()
afficher_pizzas(pizzas)
ajouter_pizaa_utilisateur(pizzas)  # Mettre à jour la liste des pizzas'''

################################################"CORRECTION############################################################################################################"

'''def afficher_pizzas(collection):
    nb_pizzas = len(collection)
    
    if nb_pizzas == 0:
        print("Aucune pizza")
    else :
        print(f"---- LISTE DES PIZZAS ({nb_pizzas}) ----")
        for i in collection:
            print(i) 
         
def ajouter_pizaa_utilisateur(collection):
    nouvelle_pizzas = input("Entrez le nom de la nouvelle pizza : ")
    collection.append(nouvelle_pizzas)
    for i in pizzas:
        print(i)
    print()
    print("premiére pidzza:" , pizzas[0])
    print("derniére pidza :", pizzas[-1])  
pizzas = ["4 fromages", "végétarienne", "hawaïenne", "calzone", "margarita"]

vide = ()
   
afficher_pizzas(pizzas)
ajouter_pizaa_utilisateur(pizzas)'''  # Mettre à jour la liste des pizzas
################################################"exercice 4############################################################################################################"
def trie_fonction(e):
    return len(e)
def afficher_pizzas(collection,n_premiers_elements=-1):
    
    c = collection
    if n_premiers_elements != -1:
        c = collection[:n_premiers_elements]
    collection.sort(key=trie_fonction)
    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("Aucune pizza")
    else :
        print(f"---- LISTE DES PIZZAS ({nb_pizzas}) ----")
        for i in c:
            print(i) 
            
'''def pizzas_existe(collection, pizza_a_verifier):
    # Vérifier si la pizza existe déjà dans la liste
    if pizza_a_verifier in collection:
        return True  # La pizza existe déjà
    else:
        return False'''
         
def ajouter_pizaa_utilisateur(collection):
    nouvelle_pizzas = input("Entrez le nom de la nouvelle pizza : ")

    if nouvelle_pizzas.lower() in collection:
        print("ERREUR : La pizza existe déjà dans la liste.")
        # print("veuillez entrer une autre pizza")
        # ajouter_pizaa_utilisateur(collection)
    else:
        collection.append(nouvelle_pizzas)
        print(f"Pizza '{nouvelle_pizzas}' ajoutée avec succès.")
        
pizzas = ["4 fromages", "végétarienne", "hawaïenne", "calzone", "margarita"]


ajouter_pizaa_utilisateur(pizzas) 
afficher_pizzas(pizzas,1)
 # Mettre à jour la liste des pizzas

###################################CORECTION FINALE ############################################################################################################
'''def afficher(collection, n_premiers_elements=-1):
    # "---- LISTE DES PIZZAS (4) ----"
    # afficher les pizzas 1 pizza par ligne
    # "AUCUNE PIZZA"
    # collection.sort(reverse=True, key=tri_personnalise)
    c = collection
    if not n_premiers_elements == -1:
        c = collection[:n_premiers_elements]

    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
        return

    print(f"---- LISTE DES PIZZAS ({nb_pizzas}) ----")
    for i in c:
        print(i)
    print()
    print("Première pizza: " + c[0])
    print("Dernière pizza: " + c[-1])
    # première pizza
    # la dernière pizza


def ajouter_pizza_utilisateur(collection):
    p = input("Pizza à ajouter: ")
    #if pizza_existe(p, collection):
    if p.lower() in collection:
        print("ERREUR : Cette pizza existe déjà")
    else:
        collection.append(p)


# def pizza_existe(e, collection):
#     for i in collection:
#         if i == e:
#             return True
#     return False

pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]

# pizza_existe -> bool
#   True : la pizza existe -> print ("ERREUR : la pizza existe déjà")
#   False : elle n'existe pas -> append
ajouter_pizza_utilisateur(pizzas)

afficher(pizzas, 2)'''
