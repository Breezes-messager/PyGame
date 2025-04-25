import pygame


class KeyboardController:
    def __init__(self):
        # 初始化按键状态字典
        self.key_states = {
            pygame.K_RIGHT: False,
            pygame.K_LEFT: False,
            pygame.K_UP: False,
            pygame.K_DOWN: False
        }

        # 可自定义的按键映射（如果需要支持自定义按键）
        self.key_mapping = {
            'right': pygame.K_RIGHT,
            'left': pygame.K_LEFT,
            'up': pygame.K_UP,
            'down': pygame.K_DOWN
        }

    def handle_events(self, events):
        """处理事件队列，更新按键状态"""
        for event in events:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key in self.key_states:
                    self.key_states[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key in self.key_states:
                    self.key_states[event.key] = False
        return True

    def is_pressed(self, key_name):
        """检查指定方向的按键是否被按下"""
        key = self.key_mapping.get(key_name)
        if key is not None:
            return self.key_states.get(key, False)
        return False

    def get_movement(self):
        """获取移动方向向量"""
        dx, dy = 0, 0
        if self.is_pressed('right'):
            dx += 1
        if self.is_pressed('left'):
            dx -= 1
        if self.is_pressed('up'):
            dy -= 1
        if self.is_pressed('down'):
            dy += 1
        return dx, dy


