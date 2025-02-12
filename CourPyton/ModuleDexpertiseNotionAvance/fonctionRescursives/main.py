#fonction RESCURSIVE
# les fonction on toujour un condition de SORTIE 



""""La récursivité en Python est une technique de programmation où une fonction s'appelle elle-même pour résoudre un problème en le décomposant en sous-problèmes plus simples. Une fonction récursive comporte généralement deux éléments essentiels :
Un cas de base : Une condition qui arrête la récursion lorsqu'elle est atteinte.
Un appel récursif : La fonction s'appelle elle-même avec un argument modifié, généralement plus petit ou plus simple que l'entrée initiale.
La récursivité permet de résoudre des problèmes complexes de manière élégante et concise, en particulier pour des tâches qui ont une structure naturellement récursive, comme le parcours d'arbres ou la résolution de problèmes mathématiques13.
Cependant, il est important de noter que la récursivité en Python a des limites, notamment en termes de profondeur de récursion maximale et de consommation de mémoire, ce qui peut nécessiter des précautions lors de son utilisation dans certains cas"""




def demander_choix(min , max):
    reponce_str = input(f"quel est votre choix entre {min} et {max} :")
    try:
        reponce_int = int(reponce_str)
        if not min <= reponce_int <= max:
            print("ERREUR: vous devez rentre un nombre entre: ", min, " et ", max)
            return demander_choix(min,max)# recomence la fonction en cas d'erreur
        return reponce_int
    except:
        print("vous devez entrer un nombre")
        return demander_choix(min,max) # recomence la fonction en cas d'erreur 

choix = demander_choix(1,4)
print("Choix de l'utilisateur:" , choix )
        
    