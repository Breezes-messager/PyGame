import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("移动小球")

running = True
speed = 5
x = 800 / 2
y = 600 / 2
dx, dy = speed, speed  # 新增：x和y方向的速度分量
clock = pygame.time.Clock()
points = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed += 1
                dx = speed if dx > 0 else -speed  # 保持方向，调整速度
                dy = speed if dy > 0 else -speed
            if event.key == pygame.K_DOWN:
                speed = max(1, speed - 1)  # 确保速度不小于1
                dx = speed if dx > 0 else -speed
                dy = speed if dy > 0 else -speed

    x += dx
    y += dy

    points.append((x,y))

    # 边界检查 + 反弹
    if x <= 10 or x >= 790:
        dx = -dx  # 碰到左右边界，x方向速度反向
    if y <= 10 or y >= 590:
        dy = -dy  # 碰到上下边界，y方向速度反向

    # 确保小球不会卡在边界
    x = max(10, min(x, 790))
    y = max(10, min(y, 590))

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 10)  # 确保坐标是整数
    for x1, y1 in points:
        pygame.draw.circle(screen, (0, 255, 0), (x1, y1), 2)
    # 显示当前速度
    font = pygame.font.SysFont(None, 36)
    speed_text = font.render(f"Speed: {speed}", True, (0, 0, 0))
    screen.blit(speed_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)  # 60FPS足够流畅

pygame.quit()
sys.exit()