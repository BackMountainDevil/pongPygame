import pygame


class ball(pygame.sprite.Sprite):
    """
    乒乓球类，存放相关参数
    """

    radius = 10
    speedx = 7
    speedy = 5

    def __init__(self, color, width, height, screensize):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()  # 位置数据
        (self.WIDTH, self.HEIGHT) = screensize

    def reset(self):
        self.rect.x = 490  # 球数据
        self.rect.y = 80
        self.speedx = 7
        self.speedy = 5

    def update(self):
        if (self.rect.y > self.HEIGHT or self.rect.y < 0):  # 上下边界
            self.speedy = -self.speedy
        elif self.rect.x > self.WIDTH:  # 右边界处理
            self.speedx = -self.speedx
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
