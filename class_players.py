

class players:
    def __init__(self, a):
        self.a = a

    def choice (self):
        game_type = int(input("""Choose game type: 
    Human vs Human ==> 1
    Human vs Bot ==> 2 
    Bot vs Bot ==> 3 """))
        if game_type == 1:
            self.a =  int(input("Player 1 choose column number between 0 and {} = ".format(self.col-1)))

    #joueur 1 "1"
    def player_1(self, a):
        # choisir colonne aléatoirement
        a = int(input("Player 1 choose column number between 0 and {} = ".format(self.col-1)))
        #a = random.randint(0,row)
        print("column number plyer 1 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                a = int(input())
                #a = random.randint(0,row)
                print("a = ",a)
                col_inv = np.flipud(jeu[:,a])
                if col_inv[i] == 0:
                    col_inv[i] = 1
                    #print(jeu)
                    Game.winner()
                    break
                else :
                    continue
                break
            if col_inv[i] == 0:
                col_inv[i] = 1
                #print(jeu)
                Game.winner()
                break
            else :
                continue
                #player_2()
        col = np.flipud(col_inv)
        Game.winner()
        Game.player_choise()
        return jeu

    #joueur 2 "-1"
    def player_2(self):
        # choisir colonne aléatoirement
        a = int(input("Player 2 choose column number between 0 and {} = ".format(self.col-1)))
        #a = random.randint(0,row)
        print("column number player 2 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                a = int(input())
                #a = random.randint(0,row)
                print("a = ",a)
                col_inv = np.flipud(jeu[:,a])
                if col_inv[i] == 0:
                    col_inv[i] = -1
                    #print(jeu)
                    Game.winner()
                    break
                else :
                    continue
                break
            if col_inv[i] == 0:
                col_inv[i] = -1
                #print(jeu)
                Game.winner()
                break
            else :
                continue
                #player_1()
        col = np.flipud(col_inv)
        Game.winner()
        Game.player_choise()
        return jeu


