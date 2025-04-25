import random  # 导入random库，用于随机选择路径


class MazeGenerator:
    def __init__(self, settings):
        # 初始化迷宫生成器
        self.settings = settings  # 存储迷宫配置（如行列数）
        self.grid = []  # 存储迷宫网格，1表示墙，0表示通道
        self.visited = []  # 记录哪些格子已经被访问过
        self.stack = []  # 用于深度优先搜索(DFS)的栈
        self.maze = []  # 存储最终生成的迷宫（这个变量在代码中似乎没有使用）

    def init_grid(self):
        # 初始化网格和访问记录
        # 创建一个全是1（墙）的二维数组，大小为rows×cols
        self.grid = [[1 for _ in range(self.settings.cols)] for _ in range(self.settings.rows)]
        # 创建一个全是False（未访问）的二维数组，用于记录访问状态
        self.visited = [[False for _ in range(self.settings.cols)] for _ in range(self.settings.rows)]

    def generate_maze(self, start_row=0, start_col=0):
        # 生成迷宫的主函数，默认从(0,0)开始
        self.init_grid()  # 初始化网格
        self.stack = [(start_row, start_col)]  # 将起点放入栈
        self.visited[start_row][start_col] = True  # 标记起点为已访问

        while self.stack:  # 当栈不为空时循环
            current = self.stack[-1]  # 获取栈顶元素（当前所在位置）
            r, c = current  # 解包当前行列坐标
            neighbors = self.get_unvisited_neighbors(r, c)  # 获取未访问的邻居

            if neighbors:  # 如果有未访问的邻居
                next_cell = random.choice(neighbors)  # 随机选择一个邻居
                self.remove_wall(current, next_cell)  # 打通当前格子和邻居之间的墙
                self.visited[next_cell[0]][next_cell[1]] = True  # 标记邻居为已访问
                self.stack.append(next_cell)  # 将邻居压入栈，成为新的当前位置
            else:  # 如果没有未访问的邻居
                self.stack.pop()  # 回溯：弹出当前格子，回到上一个位置

        return self.grid  # 返回生成的迷宫

    def get_unvisited_neighbors(self, r, c):
        # 获取当前格子(r,c)未访问的邻居（距离2格的格子）
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # 四个方向（右、下、左、上）
        neighbors = []  # 存储合法的未访问邻居

        for dr, dc in directions:  # 遍历四个方向
            nr, nc = r + dr, c + dc  # 计算邻居坐标
            # 检查邻居是否在网格范围内且未被访问
            if (0 <= nr < self.settings.rows and
                    0 <= nc < self.settings.cols and
                    not self.visited[nr][nc]):
                neighbors.append((nr, nc))  # 如果合法就加入邻居列表

        return neighbors  # 返回所有合法的未访问邻居

    def remove_wall(self, current, next_cell):
        # 打通当前格子和下一个格子之间的墙
        r1, c1 = current  # 当前格子坐标
        r2, c2 = next_cell  # 下一个格子坐标
        # 计算并打通中间的墙（中点坐标）
        self.grid[(r1 + r2) // 2][(c1 + c2) // 2] = 0  # 将墙变为通道
        self.grid[r2][c2] = 0  # 将目标格子变为通道（因为
