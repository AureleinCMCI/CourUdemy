#EXERCICE MULTIPLICATION 
#multiplication

def afficheTableMultiplication(n):
    min = 1 
    max = 10
    print()
    for i in range(min , max + 1):
        print(f"{n} * {i} = {n * i}")
        
        
    n = int(input("Entrez le nombre dont vous voulez la table de multiplication : "))
    min = 1 
    max = 10
    print(f"\nTable de multiplication de {n} :")
    for i in range(min, max + 1):
        print(f"{n} * {i} = {n * i}")
        
afficheTableMultiplication(1)
afficheTableMultiplication(2)
afficheTableMultiplication(3)
afficheTableMultiplication(4)
afficheTableMultiplication(5)
afficheTableMultiplication(6)
afficheTableMultiplication(7)
afficheTableMultiplication(8)
afficheTableMultiplication(9)
afficheTableMultiplication(10)

#correction 
def afficher_table_multiplication(n, min=1, max=10):
    if min > max:
        print("ERREUR : Le min est supéreur au max")
        return

    for i in range(min, max+1):
        print(i, "x", n, "=", i*n)


afficher_table_multiplication(5, 10, 1)


