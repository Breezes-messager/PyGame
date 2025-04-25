import sys

import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("交互式绘图板 - 按1(红)/2(绿)/3(蓝)切换颜色")

# 颜色定义
COLORS = {
    pygame.K_1: (255, 0, 0),  # 红色
    pygame.K_2: (0, 255, 0),  # 绿色
    pygame.K_3: (0, 0, 255)  # 蓝色
}
# 形状定义
SHAPE = {
    pygame.K_r: "矩形",
    pygame.K_c: "圆形"
}

current_color = COLORS[pygame.K_1]
shape_type = SHAPE[pygame.K_r]

points = []
running = True
clock = pygame.time.Clock()  # 添加时钟控制

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(f"检测到按键: {event.key}")  # 调试输出
            if event.key == pygame.K_SPACE:
                points = []
            elif event.key in COLORS:
                current_color = COLORS[event.key]
                color_names = {
                    pygame.K_1: "红色",
                    pygame.K_2: "绿色",
                    pygame.K_3: "蓝色"
                }
                pygame.display.set_caption(
                    f"当前颜色: {color_names[event.key]} - 按1/2/3切换"
                )
            elif event.key in SHAPE:
                shape_type = SHAPE[event.key]
                shape_names = {
                    pygame.K_r: "矩形",
                    pygame.K_c: "圆形"
                }
                pygame.display.set_caption(
                    f"当前颜色: {shape_names[event.key]} - 按1/2/3切换"
                )

    # 绘图逻辑
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        points.append((mouse_x, mouse_y, current_color, shape_type))

    # 渲染
    screen.fill((255, 255, 255))
    for mouse_x, mouse_y, color, shape_type in points:
        if shape_type == "圆形":
            pygame.draw.circle(screen, color, (mouse_x, mouse_y), 5)
        if shape_type == "矩形":
            pygame.draw.rect(screen, color, (mouse_x, mouse_y, 5, 5), 5)
    pygame.display.flip()
    clock.tick(240)  # 限制帧率

pygame.quit()
sys.exit()