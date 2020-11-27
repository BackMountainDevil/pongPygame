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
import time

WIDTH = 808
HEIGHT = 640

CBACK = (110, 50, 230)
CBALL = (245, 245, 220)


def main():
    x = 10
    y = 10
    radius = 10
    speedx = 7
    speedy = 5

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pong Pygame program')

    while True:
        screen.fill(CBACK)
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
        pygame.draw.circle(screen, CBALL, (x, y), radius, 0)
        if(x > WIDTH or x < 0):
            speedx = - speedx
        if(y > HEIGHT or y < 0):
            speedy = -speedy
        x = x + speedx
        y = y + speedy

        pygame.display.update()


if __name__ == '__main__':
    main()
