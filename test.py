
from matplotlib.collections import Collection
import numpy as np
from collections  import Counter
board_1=np.array([0,0,0,0,1,1,1,1])
data=Counter(board_1)
print(data[1])