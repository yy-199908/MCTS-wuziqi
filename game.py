import numpy as np
from collections  import Counter


class gameMove(object):
    def __init__(self, x, y, value):
        self.x= x
        self.y = y
        self.value = value

    def __repr__(self):
        return "x:" + str(self.x) + " y:" + str(self.y) + " v:" + str(self.value)


class GameState(object):
    x = 1
    o = -1

    def __init__(self, state, next_to_move=1):
        self.board = state
        self.board_size = state.shape[0]
        self.next_to_move = next_to_move
        
    @property
    def game_result(self):
        n=5
        # rowsum = np.sum(self.board, 0)
        # colsum = np.sum(self.board, 1)
        # diag_sum_tl = self.board.trace()
        # diag_sum_tr = self.board[::-1].trace()

        # if any(rowsum == self.board_size) or any(
        #                 colsum == self.board_size) or diag_sum_tl == self.board_size or diag_sum_tr == self.board_size:
        #     return 1.
        # elif any(rowsum == -self.board_size) or any(
        #                 colsum == -self.board_size) or diag_sum_tl == -self.board_size or diag_sum_tr == -self.board_size:

        #     return -1.
        # elif np.all(self.board != 0):
        #     return 0.
        # else:
        #     return None
        self.board_1=[]
        
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board_1.append(self.board[i][j])
        self.board_1=np.array(self.board_1)
        # data=Counter(self.board_1)
        # if data[1]<5 and data[-1]<5:
        #     return None
        
        for i in range(len(self.board_1)):
            if self.board_1[i]==0:
                continue
            if i%self.board.shape[1]<=(self.board.shape[0]-n):
                sum_row=np.sum(self.board_1[i:i+n])
                if sum_row==n:
                    return 1
                elif sum_row==-n:
                    return-1 
            if i//self.board.shape[1]<=(self.board.shape[1]-n):
                sum_col=np.sum(self.board_1[np.arange(i,i+self.board.shape[0]*(n-1)+1,self.board.shape[0])])
                if sum_col==n:
                    return 1
                elif sum_col==-n:
                    return-1 
            if i%self.board.shape[0]<=(self.board.shape[1]-n) and i//self.board.shape[1]<=(self.board.shape[0]-n):
                sum_right=np.sum(self.board_1[np.arange(i,i+self.board.shape[0]*(n-1)+n,self.board.shape[0]+1)])
                if sum_right==n:
                    return 1
                elif sum_right==-n:
                    return-1 
            if i%self.board.shape[0]>=(n-1) and i//self.board.shape[1]<=(self.board.shape[0]-n):
                sum_left=np.sum(self.board_1[np.arange(i,i+self.board.shape[0]*(n-1)-n+2,self.board.shape[0]-1)])
                if sum_left==n:
                    return 1
                elif sum_left==-n:
                    return-1 
        if np.all(self.board_1!=0):
            return 0
        return None
       


    def is_game_over(self):
        return self.game_result != None

    def is_move_legal(self, move):
        # check if correct player moves
        if move.value != self.next_to_move:
            return False

        if move.x<0 or move.x>=self.board_size:
            return False

        if move.y<0 or move.y>=self.board_size:
            return False
        # finally check if board field not occupied yet
        return self.board[move.x, move.y] == 0

    def move(self, move):
        if not self.is_move_legal(move):
            raise ValueError("move " + move + " on board " + self.board + " is not legal")
        new_board = np.copy(self.board)
        new_board[move.x, move.y] = move.value
        next_to_move = GameState.o if self.next_to_move == GameState.x else GameState.x
        return GameState(new_board, next_to_move)

    def get_legal_actions(self):
        indices = np.where(self.board == 0)
        return [gameMove(coords[0], coords[1], self.next_to_move) for coords in list(zip(indices[0], indices[1]))]
