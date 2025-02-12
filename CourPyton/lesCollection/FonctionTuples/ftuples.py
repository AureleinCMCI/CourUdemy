###################################      FONCTION ET TUPLES    ######################################

#on peux return un tupls 



###################################### EXEMPLE AVEC  SEUL FONCTION #######################################
print("avec 1 fonction : ")

def obternir():
    return "melain",37,1.60

"""info = obternir()
print("nom: " + info[0])
print("age: " + str(info[1]))
print("taille: " + str(info[2])) """# dans les 3 cas j'ai enfaite récupérer un tupls ! 

nom , age , taille = obternir()
print(f"nom:  {nom} ,   age: {age}, taille: {taille}")
print()

########################################### EXEMPLE AVEC 2 FONCTION #######################################

print("AVEC deux fonction ")
def obternir():
    return "melain",37,1.60

def affciher_info(nom , age , taille):
    print(f"nom:  {nom} ,   age: {age}, taille: {taille}")

    nom , age , taille = obternir()
affciher_info(nom , age, taille)
print()
######################################################AUTRE METHODE ####################################################
print("autre methode ")
def obternir():
    return "melain",37,1.60

def affciher_info(nom , age , taille):
    print(f"nom:  {nom} ,   age: {age}, taille: {taille}")

infos = obternir()
affciher_info(*infos) # = info[1] info[2] infoi[3]ect 