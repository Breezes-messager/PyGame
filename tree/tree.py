import math
import random

import pygame

# 初始化pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("随机分形树")

# 颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
GREEN = (0, 128, 0)

# 树干参数
start_pos = (width // 2, height)  # 起点在屏幕底部中央
length = 150  # 树干长度
angle = 0  # 0度表示垂直向上
max_depth = 5  # 最大递归深度
min_angle = 15  # 最小分叉角度
max_angle = 45  # 最大分叉角度

draw_fractal_tree = False


def draw_tree(start_pos, angle, length, depth):
    # 计算终点
    end_x = start_pos[0] - length * math.sin(math.radians(angle))
    end_y = start_pos[1] - length * math.cos(math.radians(angle))
    end_pos = (end_x, end_y)

    # 根据深度设置线条粗细和颜色
    thickness = max(1, int(5 * (0.7 ** depth)))
    color = BROWN if depth < max_depth - 1 else GREEN  # 末端树枝用绿色表示叶子

    pygame.draw.line(screen, color, start_pos, end_pos, thickness)

    # 递归终止条件
    if depth >= max_depth or length < 5:
        # 在末端画一个小圆点表示叶子
        if depth >= max_depth - 1:
            pygame.draw.circle(screen, GREEN, (int(end_x), int(end_y)), 2)
        return

    # 随机生成左右分支角度
    left_angle = angle - random.uniform(min_angle, max_angle)
    right_angle = angle + random.uniform(min_angle, max_angle)

    # 随机长度比例
    length_ratio = random.uniform(0.6, 0.8)

    # 画左右分支
    draw_tree(end_pos, left_angle, length * length_ratio, depth + 1)
    draw_tree(end_pos, right_angle, length * length_ratio, depth + 1)


# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # 按R键重新生成随机树
                max_depth = random.randint(4, 8)
                min_angle = random.randint(15, 25)
                max_angle = random.randint(30, 50)
                draw_fractal_tree = False
            elif event.key == pygame.K_UP:
                max_depth = min(10, max_depth + 1)  # 增加深度
                draw_fractal_tree = False
            elif event.key == pygame.K_DOWN:
                max_depth = max(3, max_depth - 1)  # 减少深度
                draw_fractal_tree = False

    screen.fill(WHITE)
    if not draw_fractal_tree:
        draw_tree(start_pos, angle, length, 0)  # 从深度0开始
        draw_fractal_tree = True
    # 显示当前参数
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"depth: {max_depth} angle: {min_angle}-{max_angle}° (R:random. UP or DOWN:depth)", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()