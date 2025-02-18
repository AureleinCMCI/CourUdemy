# trie par selection ! 

"""liste = [5,4,7,6]

#Élément	5	4	7	6	6	3	2	1	8	7	9	10	45	75	758
#  Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14
#Lindex est egale a = , donc l'index de la liste est = a liste[i]

for unsorted_index in range(0,len(liste)-1):
  elementMinimal = liste[unsorted_index] #unsorted_index demare a 0 
  elementMinimal_index = unsorted_index
  for i in range(unsorted_index+1,len(liste)):
    if liste[i] < elementMinimal:
      elementMinimal = liste[i]
      elementMinimal_index = i
  liste[elementMinimal_index] = liste[unsorted_index]
  liste[unsorted_index] = elementMinimal

print("sorted",liste)"""
############################################################EXERCICE######################################""""
import random


def generate_random_list(nobmreDelement, NombreMinimum, NombreMaximum):
    liste_aleatoire = [random.randint(NombreMinimum, NombreMaximum) for _ in range(nobmreDelement)]  # Utiliser min et max, pas 0 et 10
    return liste_aleatoire

# Appel de la fonction avec des arguments
ma_liste = generate_random_list(10, 0, 100)# 
print(ma_liste)

def selection_sort():
  for unsorted_index in range(len(ma_liste)-1):
      NombreMinimum = ma_liste[unsorted_index]
      NombreMinimum_index = unsorted_index
      for i in range(unsorted_index+1,len(ma_liste)):
        if ma_liste[i] < NombreMinimum:
          NombreMinimum = ma_liste[i]
          NombreMinimum_index = i
      ma_liste[NombreMinimum_index] = ma_liste[unsorted_index]
      ma_liste[unsorted_index] = NombreMinimum
  print("sorted",ma_liste)
ma_liste = selection_sort()

############################### CORECTION ################################################################################""

def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l

def selection_sort(l):
    for unsorted_index in range(0, len(l)-1):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i          #   V            m
        l[min_index] = l[unsorted_index]   #  [5, 8, 10, 2, 5]
        l[unsorted_index] = min            #  [1, 8, 10, 2, 5]

l = generate_random_list(100, -1000, 1000)
print("UNSORTED:", l)

selection_sort(l)

print("SORTED:  ", l)