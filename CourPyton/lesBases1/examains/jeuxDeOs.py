import random
import time
import os

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def Jeux_os():
    SCORE = 0
    number = "458"# Commencez avec un nombre vide.
    
    while True:
        # Ajouter un chiffre aléatoire (entre 0 et 9) au nombre existant.
        new_digit = random.randint(0, 9)
        number += str(new_digit)  # Concaténer le nouveau chiffre à la chaîne existante.

        print("Retenez le nombre :")
        print(number)

        time.sleep(2)
        clear_screen()

        user = input("Entrez le nombre complet : ")

        if user == number:
            print("Gagné!")
            SCORE += 1
            print(f"Vous avez gagné {SCORE} point(s).")
        else:
            print("Perdu!")
            break

    print(f"Score final : {SCORE}")
    print(f"La séquence était {number}")
Jeux_os()
#correction 
"""import time
import random
import os
 
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# Génération de la séquence initiale
sequence = ""
for i in range(4):
    chiffre = random.randint(0, 9)
    sequence += str(chiffre)

clear_screen()
print("Bienvenue dans le jeu du Simon")

score = 0
while True:
    print("Retenez la séquence")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()

    seq_utilisateur = input("Votre réponse : ")
    if seq_utilisateur == sequence:
        score += 1
    else:
        break

    chiffre = random.randint(0, 9)
    sequence += str(chiffre)
    clear_screen()

print("Mauvaise réponse")
print(f"La séquence était {sequence}")
print(f"Votre score final est : {score}")"""