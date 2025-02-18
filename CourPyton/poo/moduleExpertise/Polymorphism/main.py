#POLYMORPHY
#pluqieur types ->
"""
En Python, le polymorphisme permet de traiter différents types d'objets de manière uniforme, c'est-à-dire que tu peux appeler la même méthode ou fonction sur différents objets, et chaque objet se comportera différemment selon son propre type (classe).

Polymorphisme en Python
Python est un langage dynamique et flexible, ce qui signifie que tu peux appeler la même méthode ou fonction sur différents types d'objets sans avoir à spécifier le type exact de l'objet au moment de l'écriture du code. Cela se fait principalement par héritage et redéfinition de méthodes.

Exemple simple de polymorphisme en Python avec héritage :
Imaginons une classe de base Animal et deux classes filles Chien et Chat, chacune ayant une méthode parler(). Grâce au polymorphisme, tu pourras appeler parler() sur n'importe quel objet dérivé de Animal, et chaque objet se comportera différemment.

python
Copy

"""
class EtreVivant:
    def afficher_infos(self):
        print("Je suis un être vivant")

class Chat(EtreVivant):
    def afficher_infos(self):
        print("Je suis un chat")

class Personne(EtreVivant):
    def afficher_infos(self):
        print("Je suis une personne")
  

list = [EtreVivant(), Chat(), Personne()]

for element in list:
  element.afficher_infos()

def additionner(a,b):
    return a + b
print(additionner(5,1)) # ICI CELA MARCHE seulement avec les type INT
#ici je place des chaines de charactére ca va pas marché 

def additionner(a,b):
    som = 0
    if isinstance(a,int):
        som += a 
    if isinstance(b,str):
        som += len(b)
    return som
print(additionner(5,'ss')) # ICI on a dit que on return la longeur de B 
# donc la longeur return une un int , donc on peux l'additionné

