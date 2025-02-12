def trouver_plus_grand_avec_ajout():
    n = 1
    num_list = [5, 5, 8, 78, 98, 758]

    # Ajouter des éléments à num_list jusqu'à ce que n >= 10
    while n < 10:
        num_list.append(n)
        n = n * 2

    # Trouver le plus grand nombre dans la liste
    plus_grand = max(num_list)

    # Afficher la liste et le plus grand nombre
    print(f'From the numbers {num_list} the highest is {plus_grand}')

# Appeler la fonction pour tester
trouver_plus_grand_avec_ajout()