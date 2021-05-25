import numpy as np
import random
import sys



class Puissance_4_1:
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        
    def create_Game(self):
        jeu = np.zeros((self.row, self.col), dtype = "int")
        return jeu
    #joueur 1 "1"
    def player_1(self):
        # choisir colonne 
        a = int(input("Player 1 choose column number between 0 and {} = ".format(self.col-1)))
        print("column number plyer 1 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                # choisir une autre colonne 
                a = int(input())
                print("column number = ",a)
                col_inv = np.flipud(jeu[:,a])
                if col_inv[i] == 0:
                    col_inv[i] = 1
                    Game1.winner()
                    break
                else :
                    continue
                break
            if col_inv[i] == 0:
                col_inv[i] = 1
                Game1.winner()
                break
            else :
                continue
        col = np.flipud(col_inv)
        Game1.winner()
        Game1.player_choise()
        return jeu

    #joueur 2 "-1"
    def player_2(self):
        # choisir colonne
        a = int(input("Player 2 choose column number between 0 and {} = ".format(self.col-1)))
        print("column number player 2 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                # choisir une autre colonne 
                a = int(input())
                print("column number = ",a)
                col_inv = np.flipud(jeu[:,a])
                if col_inv[i] == 0:
                    col_inv[i] = -1
                    Game1.winner()
                    break
                else :
                    continue
                break
            if col_inv[i] == 0:
                col_inv[i] = -1
                Game1.winner()
                break
            else :
                continue
        col = np.flipud(col_inv)
        Game1.winner()
        Game1.player_choise()
        return jeu
    
    def winner(self):
        matrix_inv = np.flipud(jeu)
        for x in range(-self.row, self.row):
            diag_matrix = np.diag(jeu, x)
            diag_matrix_str = ','+','.join(str(each) for each in diag_matrix)
            diag_matrix_inv = np.diag(matrix_inv, x)
            diag_matrix_inv_str = ','+','.join(str(each) for each in diag_matrix_inv)
            if ',1,1,1,1' in diag_matrix_str:
                return print("The winner is player 1")
            if ',-1,-1,-1,-1' in diag_matrix_str:
                return print("The winner is player 2")
            if ',1,1,1,1' in diag_matrix_inv_str:
                return print("The winner is player 1")
            if ',-1,-1,-1,-1' in diag_matrix_inv_str:
                return print("The winner is player 2")
            
        for i,j in zip(range(0, self.row),range(0,self.col)):
            ligne = jeu[i, :]
            ligne_str = ','+','.join(str(each) for each in ligne)
            column = jeu[:, j]
            column_str = ','+','.join(str(each) for each in column)
            if ',1,1,1,1' in ligne_str:
                return print("The winner is player 1")
            if ',1,1,1,1' in column_str:
                return print("The winner is player 1")
            if ',-1,-1,-1,-1' in ligne_str :
                return print("The winner is player 2")
            if ',-1,-1,-1,-1' in column_str:
                return print("The winner is player 2")
            else:
                continue
        return jeu

    def player_choise(self):
        print("######## GAME ########")
        print(jeu)
        sum_col = np.sum(jeu,axis=0)
        turn_player = sum(list(sum_col))
        # si 0 not jeu Game Over
        if 0 not in jeu :
            return print("Full Game, Game Over")
        if len(str(Game1.winner())) == 4 :
            return print('End')
        #si turn_player = 0 c'est au player 1 de jouer, si turn_player = 1 c'est au player 2 de jouer
        if turn_player == 0:
            print("player 1")
            play = Game1.player_1()
        else:
            print("player 2")
            play = Game1.player_2()


class Puissance_4_2:
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        
    def create_Game(self):
        jeu = np.zeros((self.row, self.col), dtype = "int")
        return jeu
    #joueur 1 "1"
    def player_1(self):
        # choisir colonne
        a = int(input("Player 1 choose column number between 0 and {} = ".format(self.col-1)))
        print("column number plyer 1 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                # choisir une autre colonne 
                a = int(input())
                print("column number = ",a)
                col_inv = np.flipud(jeu[:,a])
                if col_inv[i] == 0:
                    col_inv[i] = 1
                    Game2.winner()
                    break
                else :
                    continue
                break
            if col_inv[i] == 0:
                col_inv[i] = 1
                Game2.winner()
                break
            else :
                continue
        col = np.flipud(col_inv)
        Game2.winner()
        Game2.player_choise()
        return jeu

    #joueur 2 "-1"
    def player_2(self):
        # choisir colonne aléatoirement
        a = random.randint(0,row)
        print("column number player 2 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                # choisir une autre colonne aléatoirement
                a = random.randint(0,row)
                print("column number = ",a)
                col_inv = np.flipud(jeu[:,a])
                if col_inv[i] == 0:
                    col_inv[i] = -1
                    Game2.winner()
                    break
                else :
                    continue
                break
            if col_inv[i] == 0:
                col_inv[i] = -1
                Game2.winner()
                break
            else :
                continue
        col = np.flipud(col_inv)
        Game2.winner()
        Game2.player_choise()
        return jeu
    
    def winner(self):
        matrix_inv = np.flipud(jeu)
        for x in range(-self.row, self.row):
            diag_matrix = np.diag(jeu, x)
            diag_matrix_str = ','+','.join(str(each) for each in diag_matrix)
            diag_matrix_inv = np.diag(matrix_inv, x)
            diag_matrix_inv_str = ','+','.join(str(each) for each in diag_matrix_inv)
            if ',1,1,1,1' in diag_matrix_str:
                return print("The winner is player 1")
            if ',-1,-1,-1,-1' in diag_matrix_str:
                return print("The winner is player 2")
            if ',1,1,1,1' in diag_matrix_inv_str:
                return print("The winner is player 1")
            if ',-1,-1,-1,-1' in diag_matrix_inv_str:
                return print("The winner is player 2")
            
        for i,j in zip(range(0, self.row),range(0,self.col)):
            ligne = jeu[i, :]
            ligne_str = ','+','.join(str(each) for each in ligne)
            column = jeu[:, j]
            column_str = ','+','.join(str(each) for each in column)
            if ',1,1,1,1' in ligne_str:
                return print("The winner is player 1")
            if ',1,1,1,1' in column_str:
                return print("The winner is player 1")
            if ',-1,-1,-1,-1' in ligne_str :
                return print("The winner is player 2")
            if ',-1,-1,-1,-1' in column_str:
                return print("The winner is player 2")
            else:
                continue
        return jeu

    def player_choise(self):
        print("######## GAME ########")
        print(jeu)
        sum_col = np.sum(jeu,axis=0)
        turn_player = sum(list(sum_col))
        # si 0 not jeu Game Over
        if 0 not in jeu :
            return print("Full Game, Game Over")
        if len(str(Game2.winner())) == 4 :
            return print('End')
        #si turn_player = 0 c'est au player 1 de jouer, si turn_player = 1 c'est au player 2 de jouer
        if turn_player == 0:
            print("player 1")
            play = Game2.player_1()
        else:
            print("player 2")
            play = Game2.player_2()


class Puissance_4_3:
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        
    def create_Game(self):
        jeu = np.zeros((self.row, self.col), dtype = "int")
        return jeu
    #joueur 1 "1"
    def player_1(self):
        # choisir colonne aléatoirement
        a = random.randint(0,row)
        print("column number plyer 1 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                # choisir une autre colonne aléatoirement
                a = random.randint(0,row)
                print("column number = ",a)
                col_inv = np.flipud(jeu[:,a])
                if col_inv[i] == 0:
                    col_inv[i] = 1
                    Game3.winner()
                    break
                else :
                    continue
                break
            if col_inv[i] == 0:
                col_inv[i] = 1
                Game3.winner()
                break
            else :
                continue
        col = np.flipud(col_inv)
        Game3.winner()
        Game3.player_choise()
        return jeu

    #joueur 2 "-1"
    def player_2(self):
        # choisir colonne aléatoirement
        a = random.randint(0,row)
        print("column number player 2 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                # choisir une autre colonne aléatoirement
                a = random.randint(0,row)
                print("column number = ",a)
                col_inv = np.flipud(jeu[:,a])
                if col_inv[i] == 0:
                    col_inv[i] = -1
                    Game3.winner()
                    break
                else :
                    continue
                break
            if col_inv[i] == 0:
                col_inv[i] = -1
                Game3.winner()
                break
            else :
                continue
        col = np.flipud(col_inv)
        Game3.winner()
        Game3.player_choise()
        return jeu
    
    def winner(self):
        # verification des diagonales et diagonales inverse
        matrix_inv = np.flipud(jeu)
        for x in range(-self.row, self.row):
            diag_matrix = np.diag(jeu, x)
            diag_matrix_str = ','+','.join(str(each) for each in diag_matrix)
            diag_matrix_inv = np.diag(matrix_inv, x)
            diag_matrix_inv_str = ','+','.join(str(each) for each in diag_matrix_inv)
            if ',1,1,1,1' in diag_matrix_str:
                return print("The winner is player 1")
            if ',-1,-1,-1,-1' in diag_matrix_str:
                return print("The winner is player 2")
            if ',1,1,1,1' in diag_matrix_inv_str:
                return print("The winner is player 1")
            if ',-1,-1,-1,-1' in diag_matrix_inv_str:
                return print("The winner is player 2")
        # vérification des lignes et colonnes   
        for i,j in zip(range(0, self.row),range(0,self.col)):
            ligne = jeu[i, :]
            ligne_str = ','+','.join(str(each) for each in ligne)
            column = jeu[:, j]
            column_str = ','+','.join(str(each) for each in column)
            if ',1,1,1,1' in ligne_str:
                return print("The winner is player 1")
            if ',1,1,1,1' in column_str:
                return print("The winner is player 1")
            if ',-1,-1,-1,-1' in ligne_str :
                return print("The winner is player 2")
            if ',-1,-1,-1,-1' in column_str:
                return print("The winner is player 2")
            else:
                continue
        return jeu

    def player_choise(self):
        print("######## GAME ########")
        print(jeu)
        sum_col = np.sum(jeu,axis=0)
        turn_player = sum(list(sum_col))
        # si 0 not jeu Game Over
        if 0 not in jeu :
            return print("Full Game, Game Over")
        if len(str(Game3.winner())) == 4 :
            return print('End')
        #si turn_player = 0 c'est au player 1 de jouer, si turn_player = 1 c'est au player 2 de jouer
        if turn_player == 0:
            print("player 1")
            play = Game3.player_1()
        else:
            print("player 2")
            play = Game3.player_2()



# choisir type jeu
game_type = int(input(""" 
Game type
    Human vs Human  ==> 1
    Human vs Bot    ==> 2 
    Bot vs Bot      ==> 3 
Choose game type : """))

# choix de la class à executer 
if game_type == 1:
    print('1')
    row = int(input("Please enter the number of lines = "))
    col = int(input("Please enter the number of columns = "))
    Game1 = Puissance_4_1(row, col)
    jeu = Game1.create_Game()
    Game1.player_choise()
if game_type == 2:
    print('2')
    row = int(input("Please enter the number of lines = "))
    col = int(input("Please enter the number of columns = "))
    Game2 = Puissance_4_2(row, col)
    jeu = Game2.create_Game()
    Game2.player_choise()
if game_type == 3:
    print('3')
    row = int(input("Please enter the number of lines = "))
    col = int(input("Please enter the number of columns = "))
    Game3 = Puissance_4_3(row, col)
    jeu = Game3.create_Game()
    Game3.player_choise()



if __name__ == "__main__":
    import doctest
    doctest.testmod()