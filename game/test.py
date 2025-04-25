import pygame
from pygame.locals import *

# 初始化 Pygame
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("太空飞船")


# 定义飞船类
class Ship:
    def __init__(self):
        self.image = pygame.Surface((50, 50))  # 创建飞船表面
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)  # 初始位置
        self.speed = 20
        # 绘制飞船形状（三角形）
        pygame.draw.polygon(self.image, (0, 255, 0), [
            (25, 0), (0, 50), (50, 50)
        ])  # 绿色三角形飞船

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

# 创建飞船实例
ship = Ship()

# 主循环
running = True
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            ship.move_left()
        if keys[K_RIGHT]:
            ship.move_right()
        if event.type == QUIT:
            running = False

    # 填充背景
    screen.fill((0, 0, 0))

    # 绘制飞船
    screen.blit(ship.image, ship.rect)

    # 更新显示
    pygame.display.flip()

pygame.quit()
