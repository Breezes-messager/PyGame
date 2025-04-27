import math
import random

import pygame

pygame.init()

# 初始化窗口和变量
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
draw_over = False
circles = []
min_distance = 20


def is_valid_position(new_pos, existing_positions):
    """检查新位置是否与现有圆圈保持足够距离"""
    for pos in existing_positions:
        distance = math.sqrt((new_pos[0] - pos[0]) ** 2 + (new_pos[1] - pos[1]) ** 2)
        if distance < min_distance:
            return False
    return True


# 游戏主循环
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # 获取点击位置
            print(mouse_pos)

            for i, (x, y) in enumerate(circles):
                distance = math.sqrt((mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) **2 )
                if distance <= 10:
                    print(f"点击到了第 {i + 1} 个圆圈！")
                    circles.pop(i)  # 移除被点击的圆圈
                    break

    # 绘制和逻辑代码
    screen.fill((240, 240, 240))  # 浅灰色背景
    while len(circles) < 20:
        new_pos = (random.randint(10, 790), random.randint(10, 590))
        if is_valid_position(new_pos, circles):
            circles.append(new_pos)

    # 绘制所有圆圈
    for x, y in circles:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
