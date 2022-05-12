import numpy as np
from mcts import Node,MCTSearch
from game import GameState,gameMove


def computer_frist_init(shape):
    state = np.zeros((shape, shape))
    initial_board_state = GameState(state=state, next_to_move=1)
    root = Node(state=initial_board_state, parent=None)
    mcts = MCTSearch(root)
    best_node = mcts.best_action(1000)
    c_state = best_node.state
    c_board = c_state.board
    return c_state,c_board

def human_frist_init(shape):
    state = np.zeros((shape, shape))
    initial_board_state = GameState(state=state, next_to_move=-1)
    root = Node(state=initial_board_state, parent=None)
    c_state=root.state
    c_board=c_state.board
    return c_state,c_board



def get_action(state,location):
    try:
        
        if isinstance(location, str):
            location = [int(n, 10) for n in location.split(",")]
        if len(location) != 2:
            return -1
        x = location[0]
        y = location[1]
        move = gameMove(x, y, -1)
    except Exception as e:
        move = -1
    if move == -1 or not state.is_move_legal(move):
        print("invalid move")
    return move


def judge(state):
    if state.is_game_over():
        if state.game_result == 1.0:
            return 'You lose'
        if state.game_result == 0.0:
            return "Tie!"
        if state.game_result == -1.0:
            return 'You win'
    else:
        return -1
def graphics(shape,c_board):
    for i in range(shape):
        print("")
        print("{0:3}".format(i).center(8)+"|", end='')
        for j in range(shape):
            if c_board[i][j] == 0:
                print('_'.center(8), end='')
            if c_board[i][j] == 1:
                print('X'.center(8), end='')
            if c_board[i][j] == -1:
                print('O'.center(8), end='')
    print("")
    print("______________________________")






# while True:
    
#     move1 = get_action(c_state,ui.callback)
#     c_state = c_state.move(move1)
#     c_board = c_state.board
#     # graphics(c_board)
#     ui.draw(c_board)
#     if judge(c_state)==1:
#         break
#     board_state = GameState(state=c_board, next_to_move=1)
#     root = Node(state=board_state, parent=None)
#     mcts = MCTSearch(root)
#     best_node = mcts.best_action(10)
#     c_state = best_node.state
#     c_board = c_state.board
#     # graphics(c_board)
#     if judge(c_state)==1:
#         break
    
       
        
