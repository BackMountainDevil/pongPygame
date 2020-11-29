import pygame


class racket(pygame.sprite.Sprite):
    """
    球拍类，存放相关参数
    """

    rkth = 100  # 球拍默认宽度
    rkwh = 10  # 球拍厚度
    rkstep = 5  # 每次移动球拍的距离

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()  # 位置数据

    def reset(self):
        self.rect.y = 100
