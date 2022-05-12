from pdb import Restart
import tkinter as tk  
from play import *
class gameGUI():
    def __init__(self,shape,sim_nums) -> None:
        self.root=tk.Tk()
        self.root.title('MCTS五子棋-YY')
        self.root.geometry('760x560')
        self.shape=shape
        self.sim_nums=sim_nums
        PIECE_SIZE=10
        piece_color='black'
        self.side_canvas = tk.Canvas(self.root, width = 220, height = 50)
        self.side_canvas.grid(row = 0, column = 1)
        self.side_canvas.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE,
                                110 + PIECE_SIZE, 25 + PIECE_SIZE,
                                fill = piece_color, tags = ("show_piece") )

        var = tk.StringVar()
        var.set("玩家执黑棋")
        person_label = tk.Label(self.root, textvariable = var, width = 12, anchor = tk.CENTER, 
                                font = ("黑体", 20) )
        person_label.grid(row = 1, column = 1)
        botton=tk.Button(self.root,width=10,height=5,text='开始游戏',command=self.begin)
        botton.grid(row=4,column=1)
        self.root.mainloop()
    def draw(self,c_board):
        for i in range(c_board.shape[0]):
            for j in range(c_board.shape[1]):
                if c_board[i][j]==1:
                    piece_color='white'
                    x=(540/self.shape * j+ 32)
                    y=(540/self.shape*i+38)
                    self.canvas.create_oval(x-10,y-10,x+10,y+10,
                                fill = piece_color)
                if c_board[i][j]==-1:
                    piece_color='black'
                    x=(540/self.shape * j+ 32)
                    y=(540/self.shape*i+38)
                    self.canvas.create_oval(x-10,y-10,x+10,y+10,
                                fill = piece_color)
                
    
    def callback(self,event):
        x=event.x
        y=event.y
        x=round((x-30)/(540/self.shape))
        y=round((y-30)/(540/self.shape))
        
        if x in range(self.shape)and y in range(self.shape):
            location=str(y)+','+str(x)
            move1 = get_action(self.c_state,location)
            self.c_state = self.c_state.move(move1)
            self.c_board = self.c_state.board
            self.draw(self.c_board)
            graphics(self.shape,self.c_board)
            flag=judge(self.c_state)
            if flag!=-1:
                self.end(flag)
                return None
            self.board_state = GameState(state=self.c_board, next_to_move=1)
            root = Node(state=self.board_state, parent=None)
            mcts = MCTSearch(root)
            best_node = mcts.best_action(self.sim_nums)
            self.c_state = best_node.state
            self.c_board = self.c_state.board
            self.draw(self.c_board)
            flag=judge(self.c_state)
            if flag!=-1:
                self.end(flag)
                return None
            return None
   
    def begin(self):
        self.canvas = tk.Canvas(self.root, bg = "saddlebrown", width = 540, height = 540)#对鼠标进行事件绑定，方便获取点击位置的坐标，下篇会用到
        self.canvas.grid(row = 0, column = 0, rowspan = 6)
        for i in range(self.shape):
            self.canvas.create_line(32, (540/self.shape * i + 38), (540/self.shape * (self.shape-1) + 32), (540/self.shape * i + 38))
            self.canvas.create_line((540/self.shape * i + 32), 38, (540/self.shape * i + 32), (540/self.shape * (self.shape-1) + 38))
            label = tk.Label(self.canvas, text = i, fg = "black", bg = "saddlebrown",
                        width = 2, anchor = tk.E)
            label.place(x = 2, y = 540/self.shape * i + 30)
            label = tk.Label(self.canvas, text = i, fg = "black", bg = "saddlebrown")
            label.place(x =540/self.shape * i + 30, y = 2)
        self.canvas.bind('<Button-1>',self.callback)
        self.c_state,self.c_board = human_frist_init(self.shape)#如若想电脑先走，则改为computer_frist_init(self.shape)
        self.draw(self.c_board)
    def end(self,info):
        self.root1=tk.Tk()
        self.root1.title('游戏结束')
        self.root1.geometry('200x200')
        lable=tk.Label(self.root1,text=info,width = 12, anchor = tk.CENTER, font = ("黑体", 20))
        lable.grid(row=1,column=1)
        button1=tk.Button(self.root1,text='关闭',font=('黑体',10),width=10,height=5,command=self.restart)
        button1.grid(row=3,column=1)
        self.root1.mainloop()
    def restart(self):
        self.root1.destroy()
        

if __name__=='__main__':
    ui=gameGUI(shape=8,sim_nums=10000)


#更改上述shape调整棋盘大小，更改game.py中GameState类中game_result函数中n调整胜利条件，3子，4子，5子
#sim_nums为MCTS模拟次数，次数越多，模型性能越好但时间消耗越大  ui界面显示无响应是因为MCTS程序还在simulation
#sim_nums为1000时下3*3棋盘的3子棋性能已经很好，反正我没赢过，一直都是平局，但是2000的8*8棋盘的5子棋还跟个智障差不多,改成8000之后效果不错，但是太耗时间了,还得多给它放放水
#棋盘越大，simulation时需要的时间越多

##我是通过输入一个棋盘状态来判断有没有赢家，但是这样的化棋盘上每一个子都得去判断有没有组成五子连珠
##如果更改为输入上一步棋盘状态和这一步走子的话，只需要判断这一步走子有没有构成物资连珠即可，应该会节省许多时间，但是需要更改的程序逻辑比较多，有时间的话可以试一下



















