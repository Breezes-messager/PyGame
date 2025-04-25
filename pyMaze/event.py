import sys

import pygame

from PlayerInputController import PlayerInputController
from maze import MazeGenerator
from screen import Screen
from setting import Settings, PlayerSetting, ColorSetting


class EventHandler:
    def __init__(self):
        pygame.init()
        self.p_screen = Screen()
        self.p_setting = Settings()
        self.player_setting = PlayerSetting(self.p_setting)
        self.color_setting = ColorSetting()
        self.input_controller = PlayerInputController(self.player_setting)
        # 初始化迷宫
        self.maze_gen = MazeGenerator(self.p_setting)
        self.maze = self.maze_gen.generate_maze()
        # 创建字体对象用于显示FPS
        self.font = pygame.font.Font(None, 30)
        # 初始化FPS相关变量
        self.clock = pygame.time.Clock()
        self.fps = 0

    def draw_maze(self):
        """
        迷宫生成
        :return:生成迷宫
        """
        cell_size = self.p_setting.cell_size
        wall_color = self.color_setting.wall_color

        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                if self.maze[row][col] == 1:  # 1表示墙
                    pygame.draw.rect(
                        self.p_screen.screen,
                        wall_color,
                        (col * cell_size, row * cell_size, cell_size, cell_size)
                    )

    # 处理按键事件
    def update_fps(self):
        """
        计算fps
        :return: fps
        """
        # 使用 clock.get_fps() 直接获取更准确的FPS
        self.fps = self.clock.get_fps()
        fps_text = f"FPS: {int(self.fps)}"
        return self.font.render(fps_text, True, self.color_setting.WHITE)

    def handle_events(self):
        """
        处理Pygame事件循环

        返回值:
            bool: 如果收到退出信号(QUIT或ESC键)返回False，否则返回True

        功能说明:
            1. 处理系统退出事件（窗口关闭）
            2. 处理键盘ESC键退出事件
            3. 将其他键盘事件交给输入控制器处理
        """
        for event in pygame.event.get():
            # 处理窗口关闭事件
            if event.type == pygame.QUIT:
                return False

            # 处理键盘事件
            if event.type == pygame.KEYDOWN:
                # ESC键作为退出快捷键
                if event.key == pygame.K_ESCAPE:
                    return False

            # 所有事件都传递给输入控制器处理
            self.input_controller.handle_keyboard_events(event)

        # 如果没有退出事件，返回True继续游戏循环
        return True

    def move_player(self, dt):
        print("\n--- 移动状态 ---")
        print(f"按键状态: W:{self.player_setting.moving_w} S:{self.player_setting.moving_s} "
              f"A:{self.player_setting.moving_a} D:{self.player_setting.moving_d}")

        dx, dy = 0, 0
        speed = self.player_setting.player_step * dt
        print(f"计算速度: {speed:.2f} px/frame (dt={dt:.4f}s)")

        # 方向计算
        if self.player_setting.moving_w: dy -= speed
        if self.player_setting.moving_s: dy += speed
        if self.player_setting.moving_a: dx -= speed
        if self.player_setting.moving_d: dx += speed

        new_x = self.player_setting.player_x + dx
        new_y = self.player_setting.player_y + dy

        print(f"位置变化: dx={dx:.2f}, dy={dy:.2f}")
        print(f"新坐标: ({new_x:.2f}, {new_y:.2f})")

        # 边界检查
        max_x = self.player_setting.screen_width - self.player_setting.player_width
        max_y = self.player_setting.screen_height - self.player_setting.player_height

        self.player_setting.player_x = max(0, min(new_x, max_x))
        self.player_setting.player_y = max(0, min(new_y, max_y))

    def main(self):
        running = True
        last_time = pygame.time.get_ticks()  # 初始化时间记录

        while running:
            # 计算帧时间 (dt)
            current_time = pygame.time.get_ticks()
            dt = (current_time - last_time) / 1000.0  # 转换为秒
            last_time = current_time
            # 处理事件
            running = self.handle_events()
            # 移动玩家
            self.move_player(dt)
            # 填充背景
            self.p_screen.fill(self.color_setting.BLACK)
            # 绘制迷宫
            self.draw_maze()
            # 绘制玩家
            pygame.draw.rect(self.p_screen.screen,
                             self.player_setting.player_color,
                             (self.player_setting.player_x,
                              self.player_setting.player_y,
                              self.player_setting.player_width,
                              self.player_setting.player_height)
                             )

            # 更新并显示FPS
            fps_surface = self.update_fps()
            self.p_screen.screen.blit(fps_surface, (10, 10))
            # 在渲染代码后添加坐标显示
            coord_text = f"Player: ({self.player_setting.player_x:.1f}, {self.player_setting.player_y:.1f})"
            coord_surface = self.font.render(coord_text, True, (255, 255, 255))
            self.p_screen.screen.blit(coord_surface, (10, 40))  # 显示在FPS下方
            # 更新显示
            pygame.display.flip()

            # 控制帧率
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    handler = EventHandler()
    handler.main()  # 正确调用实例方法
