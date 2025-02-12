# PYTHON FONCTIONS - NOTIONS AVANCÉES
#
# CALLBACK
#

'''def ma_fonction():
    print("toto")
    return 1

a = 5

b = ma_fonction

print("a", a, "b", b())'''

def mult_collback(a , b):
    return a * b # la fonction collback ici va enfaite returner a * b 
def sustrai_collback(a , b):
    return a - b 

def add_collback(a , b):
    return a + b 

def pow_collback(a , b):
    return pow(a,b) 

def afficher_table(n,operateur_str,operateur_cbk):
    for i in range(1, 10):
        print(i, operateur_str , n ,'=', operateur_cbk(i,n))

afficher_table(5 , "x" , mult_collback) 
print()
afficher_table(1809 , "x" , mult_collback)
print()
afficher_table(150 , "-" , sustrai_collback)
print() 
afficher_table(15 , "^" , pow_collback) 
print()
# a et b : a (ou i) : Cela correspond au premier facteur de la multiplication. Dans votre boucle for, a prend les valeurs de 1 à 9 (c'est-à-dire i dans la boucle for i in range(1, 10)). 
# b (ou n) : Cela correspond au deuxième facteur de la multiplication. Dans cet exemple, b est constant et correspond à n = 5.


# operateur_cbk = mult_collback()

# i est l'équivalent de 1 a 10 donc on va prendre les table de 1 a 9 ( for i in range(1, 10):

# n : est le nombre que l'on va multiplier, et il est bien égal à 5.

# opérateur_str = X dans   afficher_table(5 , "x" , mult_collback)

#  mult_collback dans afficher_table(5 , "x" , mult_collback)  , permet a  la fonction afficher_table de faire 
# le calcule selon la fonction mult_collback

# def mult_collback(a , b):
    #return a * b # la fonction collback ici va enfaite returner a * b ele va multiplié le 1er et le deuxiéme chifre 
    
#fonctino callback


###############################################################FONCTION LAMDAS####################################################################
def afficher_table(n,operateur_str,operateur_cbk):
    for i in range(1, 10):
        print(i, operateur_str , n ,'=', operateur_cbk(i,n))
        
afficher_table(5 , "x" , lambda a , b : a * b)