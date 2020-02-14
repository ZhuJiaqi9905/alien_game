import pygame
from pygame.sprite import Sprite 

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        #让Ship继承Sprite，以便创建飞船编组
        super(Ship, self).__init__()
        '''初始化飞船并设置初始位置'''
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像，并获取外接矩形
        self.image = pygame.image.load('.\\images\\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将每个飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx #飞船中心的x坐标
        self.rect.bottom = self.screen_rect.bottom #飞船底部的y坐标
        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        #在飞船的属性bot属性中存储小数值
        self.bot = float(self.rect.bottom)
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def blitme(self):
        '''在指定位置上绘制飞船'''
        self.screen.blit(self.image, self.rect)
    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left == True and self.rect.left  > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.bot += self.ai_settings.ship_speed_factor
        if self.moving_up == True and self.rect.top > 0:
            self.bot -= self.ai_settings.ship_speed_factor
        self.rect.bottom = self.bot
        self.rect.centerx = self.center

    def center_ship(self):
        '''让飞船底部居中'''
        self.center = float(self.screen_rect.centerx)
        self.bot = float(self.screen_rect.bottom)
