import pygame


class PlayerInputController:  # 修正类名拼写错误，使用CapWords规范
    def __init__(self, player_settings):
        """
        初始化玩家输入控制器

        :param player_settings: 包含移动状态的对象（需要有moving_w, moving_s等属性）
        """
        self.player_settings = player_settings  # 改为小写开头的变量名，符合Python命名规范

    def handle_keyboard_events(self, event):
        """
        处理键盘事件，更新移动状态

        :param event: pygame事件对象
        :return: bool - 是否处理了有效按键事件
        """
        handled = False  # 使用更准确的变量名handled

        # 处理按键按下事件
        if event.type == pygame.KEYDOWN:
            handled = True
            if event.key in (pygame.K_w, pygame.K_UP):
                self.player_settings.moving_w = True  # 统一使用小写属性名
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                self.player_settings.moving_s = True
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                self.player_settings.moving_d = True
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                self.player_settings.moving_a = True
            else:
                handled = False

        # 处理按键释放事件
        elif event.type == pygame.KEYUP:
            handled = True
            if event.key in (pygame.K_w, pygame.K_UP):
                self.player_settings.moving_w = False
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                self.player_settings.moving_s = False
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                self.player_settings.moving_d = False
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                self.player_settings.moving_a = False
            else:
                handled = False

        return handled
