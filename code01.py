
# code annee bissextile ou non ?
"""
def is_bisextile():
    print('entrer une annee :')
    year = input()
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

print(is_bisextile())
"""
#code IMC
"""
def imc():
    print('Pour calculer votre IMC')
    m = input('Entrer votre poids : ')
    t = input('Entrer votre taille : ')
    i = m / (t**2)
    print('Votre IMC est de :')
    print(i)
    if i <= 16.5:
        print('anorexie')
    elif 16.5 < i <= 18.5:
        print('maigreur')
    elif 18.5 < i <= 25:
        print('Corpulence normale')
    elif 25 < i <= 30:
        print('surpoids')
    elif 30 < i <= 35:
        print('obesite modere')
    elif 35< i <= 40:
        print('obesite eleve')
    elif i > 40:
        print('obesite morbide')
imc()
"""
# code arithetique alphabetique
"""
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def calcul_point(mot): # 1er code
    t = 0
    for lettre in mot:
        point_lettre = alphabet.index(lettre) + 1
        t = t + point_lettre
    print(t)
calcul_point(mot='bien')
"""
"""
def calcul_point2(): # 2eme code
    mot = raw_input('entrer un mot : ')
    t = 0
    for lettre in mot:
        point_lettre = alphabet.index(lettre) + 1
        t = t + point_lettre
    print(t)
calcul_point2()
"""
"""
def calcul_point3(): # 3eme code
    mot = raw_input('entrer un mot : ')
    t = 0
    for lettre in mot:
        point_lettre = ord(lettre) - ord('a') + 1
        t = t + point_lettre
    print(t)
calcul_point3()
"""
#code devine nombre
"""
import random

def devine_nombre():
    m = random.randint(0,100)
    for n in range(6):
        i = input('devine le nombre : ')
        if m > i:
            print('trop petit')
        elif m < i:
            print('trop grand')
    if i == m:
        print('gagne')
    else:
        print('perdue')
        print('la reponse etait : ')
        print(m)
devine_nombre()
"""
#code faire deviner un nombre
"""
def faire_deviner_nb():
    m = input()
        for n in range(6):
            d = input
"""

def build_list(i):
    new_list = []

    for compteur in range(i):
        new_list.append(False)
    new_list.append(True)
    for compteur in range(8-i):
        new_list.append(False)
    return new_list

new_list = build_list(0)
print(new_list)
