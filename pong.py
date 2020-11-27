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
    x = 10  # 球数据
    y = 10
    radius = 10
    speedx = 7
    speedy = 5

    rkty = 100   # 球拍数据
    rkth = 100
    rkstep = 20

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pong Pygame program')

    while True:
        screen.fill(CBACK)      # 清空画面为背景色
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:    # 键盘上下按钮响应
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_UP]:
                    if rkty - rkstep >= 0:       # 球拍的边界处理
                        rkty = rkty - rkstep
                elif pressed_keys[K_DOWN]:
                    if rkty + rkth + rkstep <= HEIGHT:
                        rkty = rkty + rkstep

        pygame.draw.rect(screen, CRKT, (0, rkty, 10, rkth), 0)
        pygame.draw.circle(screen, CBALL, (x, y), radius, 0)    # 画实心球
        if(x > WIDTH or x < 0):     # 球的边界处理
            speedx = - speedx
        if(y > HEIGHT or y < 0):
            speedy = -speedy
        x = x + speedx
        y = y + speedy

        pygame.display.update()


if __name__ == '__main__':
    main()
