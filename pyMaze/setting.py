class Settings:
    def __init__(self):

        # 设置窗口大小
        self.width, self.height = 800, 600
        self.cell_size = 20  # 每个迷宫格大小
        # 每行每列格子数
        self.rows = self.height // self.cell_size
        self.cols = self.width // self.cell_size
        self.wall_thickness = 2  # 墙厚2像素


class ColorSetting:
    def __init__(self):
        # 定义颜色
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.wall_color = (100, 100, 100)


class PlayerSetting:
    def __init__(self, settings):
        # 玩家颜色
        self.player_color = (200, 200, 200)

        # 玩家初始位置（从第一个可走格子开始）
        self.player_x = settings.cell_size * 2
        self.player_y = settings.cell_size * 2

        # 玩家大小（建议小于cell_size以便移动）
        self.player_width = settings.cell_size - 4
        self.player_height = settings.cell_size - 4

        # 移动状态
        self.moving_w = False
        self.moving_s = False
        self.moving_a = False
        self.moving_d = False

        # 玩家移动速度（像素/秒）
        self.player_step = 200

        # 引用settings的尺寸
        self.screen_width = settings.width
        self.screen_height = settings.height
