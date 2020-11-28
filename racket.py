class racket():
    """
    球拍类，存放相关参数
    """
    rkty = 100  # 球拍数据，球拍默认位置
    rkth = 100  # 球拍默认宽度
    rkwh = 10  # 球拍厚度
    rkstep = 5  # 每次移动球拍的距离

    def reset(self):
        self.rkty = 100
