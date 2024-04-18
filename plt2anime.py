# # 加载数据
# _FIM = np.load("./FIM.npy")
# _gt = np.load("./gt.npy")
# _passive = np.load("./passive.npy")
# _proposed = np.load("./proposed.npy")
# _Active = np.load("./Active-ORB-SLAM2.npy")


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# 加载数据
_est = np.load("./source/Active-ORB-SLAM2.npy")
_gt = np.load("./source/gt.npy")

# 创建画布
fig, ax = plt.subplots()
ax.set_xlim(-2, 1)
ax.set_xlabel("X(m)")
ax.set_ylim(-2, 10)
ax.set_ylabel("Y(m)")


# 初始化函数
def init():
    ax.plot([], [], 'r-', lw=2, label='estimated')
    ax.plot([], [], 'k--', lw=2, label='ground truth')
    ax.legend()
    return ax.lines

# 更新函数，每个frame下的line
def update(frame):
    start_idx = frame * 1
    end_idx = min(start_idx + 1, len(_est))
    
    ax.lines[0].set_data(_est[:end_idx, 0], _est[:end_idx, 1])
    ax.lines[1].set_data(_gt[:end_idx, 0], _gt[:end_idx, 1])
    
    return ax.lines

# 设置动画参数
ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True)

# 保存动画为视频文件
writer = FFMpegWriter(fps=10)
ani.save('Active2gt.mp4', writer=writer)

plt.show()
