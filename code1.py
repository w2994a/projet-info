"""
def is_bisextile(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

print(is_bisextile(2000))
print(is_bisextile(2009))
print(is_bisextile(1900))
print(is_bisextile(2018))
"""
"""
def is_bisextile(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

print(is_bisextile(2000))
print(is_bisextile(2009))
print(is_bisextile(1900))
print(is_bisextile(2018))
"""
"""
etat = [False,False,False,True,False,False,False,False,False]

def print_etat(rep3):
    etat_str = ''
    for element in rep3:
        if element == True:
            etat_str = etat_str + '1'
        else:
            etat_str = etat_str + '-'
    print(etat_str)
    return

print_etat(rep3=etat)
"""
#code IMC

def imc():
    print('Entrer votre masse :')
    m = input()
    print('Entrer votre taille :')
    t = input()
    i = m / (t**2)
    print('Votre IMC est de :')
    print(i)
    if i <= 16:
        print('anorexie')
    if 16.5 < i <= 18.5:
        print('maigreur')
    if 18.5 < i <= 25:
        print('Corpulence normale')
    if 25 < i <= 30:
        print('surpoids')
    if 30 < i <= 35:
        print('obesite modere')
    if 35< i <= 40:
        print('obesite eleve')
    if i > 40:
        print('obesite morbide')
imc()

"""
A l'aide de deux boucles, définir une liste qui contient 5 fois l'élément False, une fois l'élément True puis trois fois l'élément False. En quoi cela peut-il vous aider à passer de la représentation 1 à la représentation 3 ?
"""

def build_list(i):
    new_list = []

    for compteur in range(i):
        new_list.append(False)
    new_list.append(True)
    for compteur in range(8-i):
        new_list.append(False)

    return new_list

new_list = build_list(5)
if new_list == [False, False, False, False, False, True, False, False, False]:
    print("test OK")
else:
    print("test KO")
