# -*- coding: utf-8 -*-
# 导入必要的库
import sys  # 导入sys系统库，用于退出程序

import pygame  # 导入pygame游戏开发库

# 初始化Pygame所有模块
pygame.init()  # 初始化pygame，这是使用pygame前的必要步骤

# 设置初始窗口大小
initial_width, initial_height = 800, 600  # 定义窗口初始宽度和高度
# 创建可调整大小的窗口，pygame.RESIZABLE参数使窗口可以调整大小
screen = pygame.display.set_mode((initial_width, initial_height), pygame.RESIZABLE)
pygame.display.set_caption("可自由缩放的Pygame窗口")  # 设置窗口标题


# 定义颜色常量(使用RGB格式)
WHITE = (255, 255, 255)  # 白色
BLACK = (0, 0, 0)  # 黑色
BLUE = (0, 0, 255)  # 蓝色

# 创建时钟对象用于控制帧率
clock = pygame.time.Clock()
# 主循环控制变量，当running为False时退出程序
running = True

# 主游戏循环
while running:
    # 事件处理循环
    for event in pygame.event.get():  # 获取所有待处理的事件
        if event.type == pygame.QUIT:  # 如果检测到关闭窗口事件
            running = False  # 设置running为False以退出主循环
        elif event.type == pygame.VIDEORESIZE:  # 如果检测到窗口大小改变事件
            # 重新设置窗口大小为调整后的大小，保持RESIZABLE属性
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)  # 来自 VIDEO RESIZE 事件的宽度和高度

    # 获取当前窗口的实际尺寸
    current_width, current_height = screen.get_size()  # 返回当前窗口的宽和高

    # 清屏操作，用白色填充整个窗口
    screen.fill(WHITE)

    # 绘制一个随窗口大小变化的蓝色边框矩形
    rect_width = current_width * 0.8  # 矩形宽度为窗口宽度的80%
    rect_height = current_height * 0.8  # 矩形高度为窗口高度的80%
    # 计算矩形左上角坐标，使其居中显示
    rect_x = (current_width - rect_width) / 2
    rect_y = (current_height - rect_height) / 2
    # 绘制矩形(表面, 颜色, 矩形参数, 边框宽度=2)
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height), 2)

    # 创建字体对象，None表示使用默认字体，36是字号
    font = pygame.font.SysFont(None, 36)
    # 渲染显示窗口尺寸的文本(文本内容, 抗锯齿, 颜色)
    text = font.render(f"123: {current_width} x {current_height}", True, BLACK)
    # 将文本绘制到屏幕上(文本对象, 位置坐标)
    screen.blit(text, (20, 20))

    # 更新整个显示表面，将所有绘制内容显示到屏幕上
    pygame.display.flip()
    # 控制游戏帧率为60FPS
    clock.tick(60)

# 退出Pygame，释放资源
pygame.quit()
# 安全退出Python程序
sys.exit()
