需要的包：

- numpy
- tkinkter
- collections



game.py包含了实现游戏状态和落子的类

mcts.py包含了实现MCT节点和MCTS搜索的类

play.py包含了实现对弈的类

gameui.py包含了实现GUI的类





直接运行gameui.py即可

`ui=gameGUI(shape,sim_nums)`前一个参数为棋盘大小，后一个参数为每走一步MCTS simulation的次数。

- 更改上述shape调整棋盘大小，更改game.py中GameState类中game_result函数中n调整胜利条件，3子，4子，5子

- sim_nums为MCTS模拟次数，次数越多，模型性能越好但时间消耗越大  ui界面显示无响应是因为MCTS程序还在simulation

-  sim_nums为1000时下3x3棋盘的3子棋性能已经很好，反正我没赢过，一直都是平局，但是2000的8x8棋盘的5子棋还跟个智障差不多,改成8000之后效果不错，但是太耗时间了,还得多给它放放水

- 棋盘越大，simulation时需要的时间越多

我是通过输入一个棋盘状态来判断有没有赢家，但是这样的话棋盘上每一个子都得去判断有没有组成五子连珠，如果更改为输入上一步棋盘状态和这一步走子的话，只需要判断这一步走子有没有构成污渍连珠即可，应该会节省许多时间，但是需要更改的程序逻辑比较多，有时间的话可以试一下