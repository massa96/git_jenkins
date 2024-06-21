import random
import time

def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def addition(a,b):
    return a+b
def soustraction(a,b):
    return a-b

point = 0
gagner = True
print("Bienvenue dans le jeu de mathématiques !")
print("Vous allez devoir répondre à 5 questions de mathématiques.")
print("Si vous répondez correctement à une question, vous gagnez 1 point")
print("Si vous répondez incorrectement à une question, vous perdez 1 point")

while gagner:
        a = random.randint(1,10)
        b= random.randint(1,10)
        tabsigne=['+','-','*','/']
        signe = random.randint(1,4)

        s= tabsigne[signe-1]
        if s == "+" :
            print( a ,"", s,"", b)
            saisi =int(input(" = "))
            if saisi == addition(a,b):
                point += 1
                print("Bravo ! ")
            else :
                gagner = False
                print("Erreur ! Le resultat est : ",addition(a,b),"votre max de point est ", point)
        elif s == "-" :
            print( a ,"", s,"", b)
            saisi =int(input(" = "))
            if saisi == soustraction(a,b):
                point += 1
                print("Bravo ! ")
            else :
                gagner = False
                print("Erreur ! Le resultat est : ",soustraction(a,b),"votre max de point est ", point)
        elif s == "*" :
            print( a ,"", s,"", b)
            saisi =int(input(" = "))
            if saisi == multiplication(a,b):
                point += 1
                print("Bravo ! ")
            else :
                gagner = False
                print("Erreur ! Le resultat est : ",multiplication(a,b),"votre max de point est", point)
        elif s == "/":
            print(a ,"", s,"", b)
            saisi =float(input(" = "))
            if saisi == round(division(a,b),2):
                point += 1
                print("Bravo ! ")
            else :
                gagner = False
                print("Le resultat est : ",round(division(a,b),2) ,"votre max de point est ", point)


    


