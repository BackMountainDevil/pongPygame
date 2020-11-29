import pygame


class ball(pygame.sprite.Sprite):
    """
    乒乓球类，存放相关参数
    """

    radius = 10
    speedx = 7
    speedy = 5

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()  # 位置数据
        self.WIDTH = width
        self.HEIGHT = height

    def reset(self):
        self.rect.x = 490  # 球数据
        self.rect.y = 80
        self.speedx = 7
        self.speedy = 5
