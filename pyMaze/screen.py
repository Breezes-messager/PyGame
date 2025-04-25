import pygame

from setting import Settings


class Screen:
    def __init__(self):
        # 创建设置
        p_setting = Settings()

        # 创建窗口
        self.screen = pygame.display.set_mode((p_setting.width, p_setting.height), pygame.RESIZABLE)  # 窗口大小
        pygame.display.set_caption("随机迷宫生成器")  # 横眉名字

        # 计算迷宫的网格尺寸
        self.grin_width = p_setting.width // p_setting.cell_size
        self.grin_height = p_setting.height // p_setting.cell_size

    def fill(self, color):
        """填充背景色"""
        self.screen.fill(color)
