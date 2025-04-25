import sys

import pygame

from event import KeyboardController
from setting import Setting, Player

setting = Setting()
player = Player()
controller = KeyboardController()


def main():
    # 所有游戏初始化代码
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # 游戏主循环
    running = True
    while running:
        # 处理事件
        running = controller.handle_events(pygame.event.get())

        # 获取移动方向
        dx, dy = controller.get_movement()
        player.rect_x += dx * player.speed
        player.rect_y += dy * player.speed
        # 边界检查
        rect_x = max(0, min(player.rect_x, 800 - 200))
        rect_y = max(0, min(player.rect_y, 600 - 150))

        # 绘制
        screen.fill((200, 200, 200))
        pygame.draw.rect(screen, (255, 0, 0), (player.rect_x, player.rect_y, 200, 150))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()  # 确保完全退出


if __name__ == "__main__":
    main()
