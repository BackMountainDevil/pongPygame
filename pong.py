#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  pong.py
@Time    :  2020/11/27 20:23:15
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  基于py3-pygame的乒乓球游戏
'''
import pygame
from pygame.locals import K_DOWN, K_UP
import time

WIDTH = 808
HEIGHT = 640

CBACK = (110, 50, 230)
CBALL = (245, 245, 220)
CRKT = (200, 0, 0)


def main():
    x = 80  # 球数据
    y = 10
    radius = 10
    speedx = 7
    speedy = 5

    rkty = 100  # 球拍数据，球拍默认位置
    rkth = 100  # 球拍默认宽度
    rkwh = 10   # 球拍厚度
    rkstep = 5  # 每次移动球拍的距离

    isUppress = False  # 键盘“上” 是否按下
    isDownpress = False  # 键盘“下” 是否按下

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pong Pygame program')

    while True:
        screen.fill(CBACK)  # 清空画面为背景色
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:  # 键盘上下按钮响应
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_UP]:
                    isUppress = True  # 用标志来解决键盘一直按着的情况
                elif pressed_keys[K_DOWN]:
                    isDownpress = True
            elif event.type == pygame.KEYUP:  # 按键释放后将按下标志设置为 假
                isUppress = isDownpress = False

        if (rkty - rkstep >= 0) and isUppress:  # 球拍的边界处理，一直按着也能移动球拍
            rkty = rkty - rkstep
        if (rkty + rkth + rkstep <= HEIGHT) and isDownpress:
            rkty = rkty + rkstep

        pygame.draw.rect(screen, CRKT, (0, rkty, rkwh, rkth), 0)  # 画填充矩形：球拍
        pygame.draw.circle(screen, CBALL, (x, y), radius, 0)  # 画实心球
        if x > WIDTH:  # 球的边界处理
            speedx = -speedx
        elif x < (rkwh + radius):   # 左边界
            if (y > rkty) and (y < (rkty + rkth)):  # 球拍范围内
                speedx = -speedx
            else:   # 未击中球拍
                pygame.quit()
                return 0
        if (y > HEIGHT or y < 0):   # 上下边界
            speedy = -speedy
        x = x + speedx
        y = y + speedy

        pygame.display.update()


if __name__ == '__main__':
    main()
