import math
import random

import pygame

pygame.init()

# 初始化窗口和变量
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
draw_over = False
circles = []  # 现在每个元素是((x,y), color)元组
min_distance = 20
draw = False
score = 0
font = pygame.font.SysFont('Arial', 32)


def is_valid_position(new_pos, existing_positions):
    """检查新位置是否与现有圆圈保持足够距离"""
    for pos, _ in existing_positions:  # 现在existing_positions中的每个元素是(pos, color)
        distance = math.sqrt((new_pos[0] - pos[0]) ** 2 + (new_pos[1] - pos[1]) ** 2)
        if distance < min_distance:
            return False
    return True


# 游戏主循环
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                circles = []
                score = 0
                draw = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for i, ((x, y), color) in enumerate(circles):  # 修改了这里的解构方式
                distance = math.sqrt((mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) ** 2)
                if distance <= 10:
                    print(f"点击到了第 {i + 1} 个圆圈！")
                    score += 1
                    circles.pop(i)  # 移除被点击的圆圈
                    break

    # 绘制和逻辑代码
    screen.fill((240, 240, 240))  # 浅灰色背景

    if not draw:
        circles = []  # 清空现有圆圈
        for i in range(20):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            while True:
                new_pos = (random.randint(10, 790), random.randint(10, 590))
                if is_valid_position(new_pos, circles):
                    circles.append((new_pos, color))
                    break
        draw = True

    # 绘制所有圆圈
    for (x, y), color in circles:
        pygame.draw.circle(screen, color, (x, y), 10)

    # 显示得分和提示
    score_text = font.render(f"score: {score}", True, (0, 0, 0))
    hint_text = font.render("please press R to replay", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))
    screen.blit(hint_text, (20, 60))

    # 如果所有圆圈都被消除，显示胜利信息
    if len(circles) == 0 and draw:  # 添加了and draw条件，避免初始时显示
        win_text = font.render("congratulation,you delete all circle! please press R to replay", True, (0, 100, 0))
        screen.blit(win_text, (200, 300))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()