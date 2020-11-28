class ball():
    """
    乒乓球类，存放相关参数
    """
    x = 80  # 球数据
    y = 10
    radius = 10
    speedx = 7
    speedy = 5
    WIDTH = -1
    HEIGHT = -1

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height

    def reset(self):
        self.x = 80  # 球数据
        self.y = 10
        self.speedx = 7
        self.speedy = 5
