#les return sert a sortir de la fonction , ou returne une vvlauer
def afficher_infos_personne(nom="",age=0):
    if nom == "":
        print("0 nom , age" , age)
    
    else:
        if age == 0:
            print("nom : " , nom )
        else:
            print("nom : " , nom , "age : " , age)
        print('le nom comporte',len(nom),"caractéres")
print("debut du programe")
afficher_infos_personne(age="20")


def afficher_infos_personne(nom="",age=0):
    if nom == "":
        print("0 nom , age" , age)
        return # le return fair que on sort de la fonction , donc on a plus besoin du else
        #comme on rentre dans la condition ! le reste du code ne sera pas exécuté par le programe 
    
    if age == 0:
        print("nom : " , nom )
    else:
        print("nom : " , nom , "age : " , age)
        
    print('le nom comporte',len(nom),"caractéres")
print("debut du programe")
afficher_infos_personne(age="20")
        