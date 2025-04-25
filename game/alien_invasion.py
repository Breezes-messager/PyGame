import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    # 设置实例化
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船实例
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组
    bullets = Group()

    while True:
        # 监测输入设备
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船信息
        ship.update()
        bullets.update()
        # 图形的绘制
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
