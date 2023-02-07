def display_board(t):
    print(f""""
    Soyez les bienvenus au jeu de ==> TIC TAC TOE!
    
    TIC TAC TOE!
    *****************
    *   {t['0'][0]} | {t['0'][1]} | {t['0'][2]}   *
    *  ---|---|---  *
    *   {t['1'][0]} | {t['1'][1]} | {t['1'][2]}   *
    *  ---|---|---  *
    *   {t['2'][0]} | {t['2'][1]} | {t['2'][2]}   *
    *****************
    """)


def joueur_du_jeu(joueur):
    print(f"\t C'est le tour du joueur {joueur}...\n")
    row = input('\tEntrer la ligne: ')
    column = input('\tEntrer la colonne: ')
    while True :
        if int(row) > 3 or int(row) < 1 < 1:
            print("\tligne incorrecte")
        elif int(column) > 3 or int(column) < 1:
            print("\tcolonne incorrecte")
        else:
            break
        row = input('\tEntrer la ligne: ')
        column = input('\tEntrer la colonne: ')
    row = str(int(row) -1)
    column = str(int(column) -1)
    return row, column


def check_win(t):
    z = [0]
    x = [0]
    for i in range(0, 2):
        z.append(0)
        x.append(0)
    for j in range(0, 3):
        for i in range(0, 3):
            z[i] = 0
            x[i] = 0
        for i in range(0, 3):
            if t[str(i)][i].lower() == 'x':
                x[0] += 1
            if t[str(j)][i].lower() == 'x':
                x[1] += 1
            if t[str(i)][j].lower() == 'x':
                x[2] += 1
            if t[str(i)][i] == '0':
                z[0] += 1
            if t[str(j)][i] == '0':
                z[1] += 1
            if t[str(i)][j] == '0':
                z[2] += 1
        if 3 in z:
            return "\tPlayer 0 est le vainqueur"
        if 3 in x:
            return "\tPlayer X est le vainqueur"
    return False


def play(joueur, t):
    while True:
        index = joueur_du_jeu(joueur)
        ind = int(index[1])
        if t[index[0]][ind] == ' ':
            t[index[0]][ind] = joueur
            return t
        else:
            print('\tCase déjà occupée')

def Tic_Tac():
    t = {
        '0': [],
        '1': [],
        '2': []
    }
    for x in t:
        for i in range(0, 3):
            t[x].append(' ')

    # Nous commençons par le jour X
    joueur = '0'
    while True:
        if joueur == '0':
            joueur = 'X'
        else:
            joueur = '0'
        display_board(t)
        t = play(joueur, t)
        win = check_win(t)
        display_board(t)
        if win:
            print(win)
            return True
Tic_Tac()