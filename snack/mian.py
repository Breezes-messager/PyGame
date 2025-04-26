import random

import pygame

pygame.init()

# 初始化窗口和变量
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
game_over = False  # 添加游戏结束状态
pygame.display.set_caption("简易贪吃蛇")

# 颜色定义
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 蛇的初始设置
snake_size = 20
snake_speed = 10
snake_body = [[400, 300]]  # 初始蛇头位置
snake_direction = 'RIGHT'
change_to = snake_direction

# 食物设置
food_pos = [random.randrange(1, (800 // snake_size)) * snake_size,
            random.randrange(1, (600 // snake_size)) * snake_size]
food_spawn = True

# 分数
score = 0
font = pygame.font.SysFont('arial', 20)


def show_game_over():
    go_text = font.render('game over! R regame', True, WHITE)
    screen.blit(go_text, (300, 300))


# 游戏主循环
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 按键控制
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_UP and snake_direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                    change_to = 'DOWN'
            else:
                if event.key == pygame.K_r:  # 按R键重新开始
                    game_over = False
                    snake_body = [[400, 300]]
                    snake_direction = 'RIGHT'
                    change_to = snake_direction
                    score = 0
                    food_pos = [random.randrange(1, (800 // snake_size)) * snake_size,
                                random.randrange(1, (600 // snake_size)) * snake_size]
                    food_spawn = True

    if not game_over:
        # 更新方向
        snake_direction = change_to

        # 移动蛇
        new_head = [snake_body[0][0], snake_body[0][1]]
        if snake_direction == 'RIGHT':
            new_head[0] += snake_size
        elif snake_direction == 'LEFT':
            new_head[0] -= snake_size
        elif snake_direction == 'UP':
            new_head[1] -= snake_size
        elif snake_direction == 'DOWN':
            new_head[1] += snake_size

        # 插入新头部
        snake_body.insert(0, new_head)

        # 检测是否吃到食物
        if snake_body[0][0] == food_pos[0] and snake_body[0][1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            # 如果没有吃到食物，移除尾部
            snake_body.pop()

        # 生成新食物
        if not food_spawn:
            food_pos = [random.randrange(1, (800 // snake_size)) * snake_size,
                        random.randrange(1, (600 // snake_size)) * snake_size]
            # 确保食物不会生成在蛇身上
            while food_pos in snake_body:
                food_pos = [random.randrange(1, (800 // snake_size)) * snake_size,
                            random.randrange(1, (600 // snake_size)) * snake_size]
            food_spawn = True

        # 边界检测和自身碰撞检测
        if (snake_body[0][0] >= 800 or snake_body[0][0] < 0 or
                snake_body[0][1] >= 600 or snake_body[0][1] < 0):
            game_over = True

        for block in snake_body[1:]:
            if snake_body[0][0] == block[0] and snake_body[0][1] == block[1]:
                game_over = True

    # 绘制
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], snake_size, snake_size))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))

    # 显示分数
    score_text = font.render(f'score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        show_game_over()

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()