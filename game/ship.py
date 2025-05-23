import pygame


# 定义飞船类
class Ship:
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.Surface((50, 50))  # 创建飞船表面
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # self.rect.center = (400, 500)  # 初始位置
        # 直接使用屏幕尺寸动态计算位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中储存小数值
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self): 
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值,而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        # 绘制飞船形状（三角形）
        pygame.draw.polygon(self.image, (0, 255, 0), [
            (0, 0), (0, 50), (50, 50),(50,0)
        ])  # 绿色三角形飞船

    def blitme(self):
        self.screen.blit(self.image,self.rect)