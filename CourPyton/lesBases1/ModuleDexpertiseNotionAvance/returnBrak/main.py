#Voici les principales différences entre break et return en Python :
"""break
Utilisé dans les boucles (for, while) pour en sortir immédiatement.
Termine seulement la boucle la plus proche, pas la fonction entière.
Ne renvoie aucune valeur.
Utile pour arrêter une itération prématurément.
Exemple :
python
for i in range(10):
    if i == 5:
        break
    print(i)
# Affiche 0, 1, 2, 3, 4
return
Utilisé dans les fonctions pour terminer leur exécution et renvoyer une valeur.
Sort complètement de la fonction, pas seulement d'une boucle.
Peut renvoyer une valeur (ou None si aucune valeur n'est spécifiée).
Termine l'exécution de la fonction immédiatement.
Exemple :
python
def fonction():
    for i in range(10):
        if i == 5:
            return i
    return None

resultat = fonction()
print(resultat)  # Affiche 5
En résumé, break contrôle le flux dans les boucles, tandis que return contrôle le flux et les valeurs de retour des fonctions.
"""
