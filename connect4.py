from copy import deepcopy
import os

class Connect4:
    def __init__(self, row=6, col=7):
        self.row = row
        self.col = col
        self.board = [[0]*col for _ in range(row)]
        self.value = None


    def successors(self, val):
        if self.value is not None:
            return []

        succ = []
        for i in range(self.col):
            try:
                succ.append(self.make_move(i, val))
            except ValueError:
                pass

        if not len(succ) and self.value is None:
            self.value = 0

        return succ

    def _valid_pos(self, i, j):
        return not (i < 0 or i >= self.row or j < 0 or j >= self.col)


    def make_move(self, col, val):
        col-=1
        if self.board[0][col] != 0:
            raise ValueError("Illegal Move on full column")

        indx = None
        for i in range(self.row-1,-1,-1):
            if self.board[i][col] == 0:
                indx = i
                break

        c4 = Connect4(self.row, self.col)
        c4.board = deepcopy(self.board)
        c4.board[indx][col] = val

        #check win
        winner_was_found = False
        for i in range(indx-4, indx+4):
            if self._valid_pos(i,col):
                winner = True
                for j in range(4):
                    if not self._valid_pos(i+j,col) or c4.board[i+j][col] != val:
                        winner = False
                        break
                        
                if winner:
                    c4.value = float('inf') if val == 1 else float('-inf')
                    winner_was_found = True
                    break
        
        if winner_was_found:
            return c4
        

        for i in range(col-4, col+4):
            if self._valid_pos(indx,i):
                winner = True
                for j in range(4):
                    if not self._valid_pos(indx,i+j) or c4.board[indx][i+j] != val:
                        winner = False
                        break
                        
                if winner:
                    c4.value = float('inf') if val == 1 else float('-inf')
                    winner_was_found = True
                    break

        if winner_was_found:
            return c4


        for i in range(col-4, col+4):
            if self._valid_pos(indx,i):
                winner = True
                for j in range(4):
                    if not self._valid_pos(indx + j,i+j) or c4.board[indx+j][i+j] != val:
                        winner = False
                        break
                        
                if winner:
                    c4.value = float('inf') if val == 1 else float('-inf')
                    winner_was_found = True
                    break

        if winner_was_found:
            return c4
        
        #check win
        for i in range(indx-4, indx+4):
            if self._valid_pos(i,col):
                winner = True
                for j in range(4):
                    if not self._valid_pos(i + j,col+j) or c4.board[i+j][col+j] != val:
                        winner = False
                        break
                        
                if winner:
                    c4.value = float('inf') if val == 1 else float('-inf')
                    winner_was_found = True
                    break
        
        if winner_was_found:
            return c4


        return c4



    def pretty_print(self):
        char_arr = [" ", "O", "X"]

        print("-"*(self.col*4+1))
        for row in self.board:
            print("|",end=" ")
            for entry in row:
                print(char_arr[entry],end=" | ")
            print()
        
        print("-"*(self.col*4+1))
        print(" ",end="")
        for i in range(1,self.col+1):
            print(f" {i}  ", end="")
        print()
