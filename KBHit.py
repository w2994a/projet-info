from kbhit import KBHit

etat = [[False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False ]]

x = 0
y = 0


def print_etat(rep3): #etat du jeu
    etat_str = ''
    for ligne in rep3:
        for element in ligne:
            if element == True:
                etat_str = etat_str + '+'
            else:
                etat_str = etat_str + '-'
        etat_str = etat_str + '\n'
    print(etat_str)
    return

print_etat(rep3=etat) # afficher l'etat du jeu

def move_right(): # deplacement a droite
    x += 1
    return

def move_left(): # deplacement a gauche
    x -= 1
    return

def move_up(): # deplacement en haut
    y += 1
    return

def move_down(): # deplacement en bas
    y -= 1
    return

if __name__ == "__main__":

    kb = KBHit()

    print('Hit any key, or ESC to exit')

    while True:

        if kb.kbhit():
            c = kb.getch()
            c_ord = ord(c)
            print(c)
            print(c_ord)
            if c_ord == 27: # ESC
                break

            if c_ord == 100: # D
                move_right(x)

            if c_ord == 113: # Q
                move_left(x)

            if c_ord == 122: # z
                move_up(x)

            if c_ord == 115: # s
                move_down(x)
