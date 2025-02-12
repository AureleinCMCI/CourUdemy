# LES FONCTION : programme de QCM 

# Question : quelle est la capitale de la france ?

# (a) marseille
# (b) lyon
# (c) paris
# (d) bordeaux

# Vitre réponce : 
# bonne réponce mauvaise réponce 

# ecttt ... 4 question 

"""def Questionaire_Ville():
    userRéponce = input("Quelle est la capitale de la france ")
    if userRéponce == "paris":
        print("Bonne réponce")
    else:
        print("mauvaise réponce")
        
    if userRéponce == "paris":
        print("Bonne reponce")
    else : 
        print("Mauvaise reponce")
    userRéponce = input("Quelle est la capitale de l'Espagne ")
    if userRéponce == "madrid":
        print("Bonne reponce")
    else :
        print("bonne réponce")
        
    userRéponce = input("Quelle est la capitale du japon ")
    if userRéponce == "tokyo":
        print("Bonne reponce")
    else :
        print("bonne réponce")
Questionaire_Ville()"""""

"""def Questionaire_Ville():
    a = "paris"
    b = "chine"
    c = "lyon "
    d = "bordeaux"
    
    a2 = "tokio"
    b2 = "marachech"
    c2 = "singapour"
    
    a3 = "chine"
    b3 = "marachech"
    c3 = "singapour"
    
    point = 0
    
    print(f"Quel est la capitale de paris \n reponce a :  {a} \n reponce b ? : {b} \n reponce c ? {c} \n reponce d {d} ")
    UserReponce = input("Choissiez votre réponce : ")
    
    if UserReponce == a :
        print("Bonne reponce")
        point += 1
        
        SegondeQuestion = input(f"Quel est la capitale du japon ? :  \n reponce a :  {a2} \n reponce b ? : {b2} \n reponce c ? {c2} \n  ")
        if SegondeQuestion == a2 :
            print("Bonne reponce")
        point += 1
        
        TroisiemeQuestion = input(f"Quel est la capitale du maroc ? :  \n reponce a :  {a3} \n reponce b ? : {b3} \n reponce c ? {c3} \n ")
        if TroisiemeQuestion == a3:
            print("Bonne reponce")
            point += 1
            return
    else :
        print(f"mauvaise réponce la bonne reponce était {a}")
        
    print(f"vous avez un totale de {point} point  / 4")
    
Questionaire_Ville()"""

def Questionaire_Ville():
    
    a = "paris"
    b = "chine"
    c = "lyon "
    d = "bordeaux"
    
    a2 = "tokio"
    b2 = "marachech"
    c2 = "singapour"
    
    a3 = "chine"
    b3 = "marachech"
    c3 = "singapour"
    
    point = 0
    
    print(f"Quel est la capitale de paris \n reponce a :  {a} \n reponce b ? : {b} \n reponce c ? {c} \n reponce d {d} ")
    UserReponce = input("Choissiez votre réponce : ")
    
    
    print()
    if UserReponce == "a" :
        print("Bonne reponce")
        point += 1
        print(f"vous avez  {point}")
    else :
        print(f"mauvaise réponce la bonne reponce était {a}")
        
    print()
    SegondeQuestion = input(f"Quel est la capitale du japon ? :  \n reponce a :  {a2} \n reponce b ? : {b2} \n reponce c ? {c2} \n  ")
    if SegondeQuestion == "a2" :
        print("Bonne reponce")
        point += 1
        print(f"vous avez  {point}")
    else :
        print(f"mauvaise réponce la bonne reponce était {a2}")
    
    print()
    TroisiemeQuestion = input(f"Quel est la capitale du maroc ? :  \n reponce a :  {a3} \n reponce b ? : {b3} \n reponce c ? {c3} \n ")
    if TroisiemeQuestion == "b":
        print("Bonne reponce")
        point += 1
        print(f"vous avez  {point}")
    else :
        print(f"mauvaise réponce la bonne reponce était {a3}")
        
    print(f"vous avez un totale de {point} point  / 3")
    
Questionaire_Ville()



# correction 

def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse):
    #global score
    score = 0
    print("score:", score)
    print("QUESTION")
    print("  " + question)
    print("  (a)", r1)
    print("  (b)", r2)
    print("  (c)", r3)
    print("  (d)", r4)
    print()
    reponse = input("Votre réponse : ")
    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
        #score += 1
    else:
        print("Mauvaise réponse")
        
    print()


score = 10

poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)
