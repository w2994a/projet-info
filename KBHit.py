from kbhit import KBHit

etat = [False,False,False,True,False,False,False,False,False]
i = 3

def print_etat(rep3):
    etat_str = ''
    for element in rep3:
        if element == True:
            etat_str = etat_str + '+'
        else:
            etat_str = etat_str + '-'
    print(etat_str)
    return

print_etat(rep3=etat)

def renitialisation():
    i = 0
    return

def move_right(i):
    etat[i] = True
    etat[i-1] = False
    print_etat(rep3=etat)
    print(i)
    return

def move_left(i):
    etat[i] = True
    etat[i+1] = False
    print_etat(rep3=etat)
    print(i)
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

            if c_ord == 100 and i < 8: # D
                i += 1
                move_right(i)

            if c_ord == 113 and i > 0: # Q
                i -=1
                move_left(i)

            if c_ord == 100 and i > 8: # D
                renitialisation(i)


            if c_ord == 113 and i <= 0: # Q
                i = 8
                move_left(i)
