import pygame


class racket(pygame.sprite.Sprite):
    """
    球拍类，存放相关参数
    """

    rkth = 100  # 球拍默认宽度
    rkwh = 10  # 球拍厚度
    rkstep = 5  # 每次移动球拍的距离

    def __init__(self, color, size, img=False):
        pygame.sprite.Sprite.__init__(self)
        if img:     # 有图用图，忽略大小size设置，大小由图片大小确定
            try:
                self.image = pygame.image.load(img)
                self.rkwh = self.image.get_size()[0]   # 大小修正
                self.rkth = self.image.get_size()[1]
            except Exception as e:  # 图片文件发生错误用方块替代
                print("温馨提示： ", e, "， 请正确配置图片文件")
                self.image = pygame.Surface(size)
                self.width = size
                self.image.fill(color)
        else:       # 没图用方块替代
            self.image = pygame.Surface(size)
            (self.rkwh, self.rkth) = size
            self.image.fill(color)
        self.rect = self.image.get_rect()  # 位置数据

    def reset(self):
        self.rect.y = 100
