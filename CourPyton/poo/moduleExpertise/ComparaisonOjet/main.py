# Comparer des objets
# is / ==

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

personne2 = Personne("Jean", 20) # dictionnaire 2 
personne2.AfficherInfos()

print(personne1 == personne2)
print(personne1 is personne2)

print(personne1.__dict__ == personne2.__dict__)# ici on compare les 2 dictionnaire 