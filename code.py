'''
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
'''
'''
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
'''
'''
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
'''
