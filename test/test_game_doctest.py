import numpy as np
import random
import unittest
import sys

"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> Puissance_4_1(6,7)
True

>>> Puissance_4_2(6,7)
True

>>> Puissance_4_3(6,7)
True
"""




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
        # choisir colonne al??atoirement
        a = random.randint(0,row)
        print("column number player 2 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                # choisir une autre colonne al??atoirement
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
        # choisir colonne al??atoirement
        a = random.randint(0,row)
        print("column number plyer 1 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                # choisir une autre colonne al??atoirement
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
        # choisir colonne al??atoirement
        a = random.randint(0,row)
        print("column number player 2 = ", a)
        #inverser les lignes de la colonne a
        col_inv = np.flipud(jeu[:,a])
        for i in range(0,self.row):
            if 0 not in col_inv:
                print("Column number {} is full, choose another column".format(a))
                # choisir une autre colonne al??atoirement
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
        # v??rification des lignes et colonnes   
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



if __name__ == "__main__":
    import doctest
    doctest.testmod()