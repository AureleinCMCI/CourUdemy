# CCOPIER
# is / ==
import copy 
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")

    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age


personne1 = Personne("Jean", 20)
personne1.AfficherInfos() #dictionanire 1 

personne2 = copy.copy(personne1) # ici j'ai copier personne 1 dans personne 2 
personne2.AfficherInfos()

print(personne1 == personne2)
print(personne1 is personne2)

print(personne1.__dict__ == personne2.__dict__)
#######################################################EXEMPLE 2 ##########################################################################

print("EXEMPLE 2 ")
print()
# ici on a d'abord rajouté amis 
class Personne:
    def __init__(self, nom, age, amis ):
        self.nom = nom
        self.age = age
        self.amis = amis 
    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")
        print("amis : " + str(self.amis))
    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age


personne1 = Personne("Jean", 20,["claire","marc","emilie"])
personne1.AfficherInfos() #dictionanire 1 

personne2 = copy.deepcopy(personne1) # ici j'ai copier personne 1 dans personne 2

personne1.amis[0] = "chantal" 
# ici c'est seuelement dans personne 2 que le changement sera eefectué car 
#on a ecris le changement apres le copy , si j'utilise deepcopy , cela va cahngé méme si on utilise le hcangement apres le deepcopy
# donc avec deepCoppy on gardera les information de liste 1 dans pesonne 1
personne2.AfficherInfos()

print(personne1 == personne2)
print(personne1 is personne2)

print(personne1.__dict__ == personne2.__dict__)