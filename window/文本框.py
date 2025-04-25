import sys

import pygame

# 初始化Pygame
pygame.init()

# 设置窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame文本框示例")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)

# 加载支持中文的字体文件
font_path = "C:\\Windows\\Fonts\\msyh.ttc"  # 替换为你的字体文件路径
font = pygame.font.Font(font_path, 36)


class TextBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.text = ""
        self.txt_surface = font.render("", True, BLACK)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 如果点击了文本框矩形区域
            if self.rect.collidepoint(event.pos):
                # 切换活动状态
                self.active = not self.active
            else:
                self.active = False
            # 改变当前颜色
            self.color = LIGHT_BLUE if self.active else GRAY

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)  # 回车时打印文本
                    # self.text = ""  # 可以清空文本框
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]  # 删除最后一个字符
                else:
                    self.text += event.unicode  # 添加字符
                # 重新渲染文本
                self.txt_surface = font.render(self.text, True, BLACK)

    def update(self):
        # 如果文本太长，调整宽度
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # 绘制文本框
        pygame.draw.rect(screen, self.color, self.rect, 2)
        # 绘制文本
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # 绘制光标（如果活动）
        if self.active and pygame.time.get_ticks() % 1000 < 500:
            cursor_pos = self.txt_surface.get_width() + 5
            pygame.draw.line(screen, BLACK,
                             (self.rect.x + cursor_pos, self.rect.y + 5),
                             (self.rect.x + cursor_pos, self.rect.y + self.rect.h - 5), 2)


# 创建文本框
input_box = TextBox(100, 100, 200, 32)
# 可以创建多个文本框
input_box2 = TextBox(100, 200, 200, 32)

# 主循环
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 处理文本框事件
        input_box.handle_event(event)
        input_box2.handle_event(event)

    # 更新文本框
    input_box.update()
    input_box2.update()

    # 绘制
    screen.fill(WHITE)

    # 绘制标签
    label = font.render("用户名:", True, BLACK)
    screen.blit(label, (20, 105))

    label2 = font.render("密码:", True, BLACK)
    screen.blit(label2, (20, 205))

    # 绘制文本框
    input_box.draw(screen)
    input_box2.draw(screen)

    # 显示提示
    hint = font.render("点击文本框输入，回车确认", True, BLACK)
    screen.blit(hint, (100, 300))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
