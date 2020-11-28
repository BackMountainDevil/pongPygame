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
from pygame.locals import K_DOWN, K_s, K_UP, K_w, K_SPACE
import time

# MUSICPATH
MHIT = "pong.ogg"  # 击球声音文件路径
MBEG = "maliaobegin.ogg"  # 开始音频
MFAIL = "fail.ogg"  # 游戏失败音频
MBAK = "tombk.ogg"  # 背景音乐音频

WIDTH = 808
HEIGHT = 640

CBACK = (110, 50, 230)
CBALL = (245, 245, 220)
CRKT = (200, 0, 0)
CFONT = (0, 0, 0)


def main():
    x = 80  # 球数据
    y = 10
    radius = 10
    speedx = 7
    speedy = 5

    rkty = 100  # 球拍数据，球拍默认位置
    rkth = 100  # 球拍默认宽度
    rkwh = 10  # 球拍厚度
    rkstep = 5  # 每次移动球拍的距离

    isUppress = False  # 键盘“上” 是否按下
    isDownpress = False  # 键盘“下” 是否按下

    isload = False  # 音乐是否载入
    ispause = False  # 是否暂停
    isfail = False
    score = 0  # 分数
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pong Pygame program')

    pygame.mixer.init()  # 初始化音频模块并载入音频文件
    try:
        mhit = pygame.mixer.Sound(MHIT)
        mbegin = pygame.mixer.Sound(MBEG)
        mfail = pygame.mixer.Sound(MFAIL)
        pygame.mixer.music.load(MBAK)
        isload = True
    except Exception as m:
        print("温馨提示： ", m, "， 请正确配置音频文件")
    if isload:  # 载入失败不会推出，后面不会有音乐罢了
        pygame.mixer.music.play()
        mbegin.play()

    while True:
        if isload and not pygame.mixer.music.get_busy():  # 循环播放背景音乐
            pygame.mixer.music.play()

        screen.fill(CBACK)  # 清空画面为背景色
        time.sleep(0.01)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:  # 键盘上下按钮响应
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_UP] or pressed_keys[K_w]:
                    isUppress = True  # 用标志来解决键盘一直按着的情况
                elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
                    isDownpress = True
                elif pressed_keys[K_SPACE]:  # 空格键 暂停
                    ispause = not ispause
                    if isfail:
                        isfail = False  # 重新开始，重置数据
                        x = 80
                        y = 10
                        speedx = 7
                        speedy = 5
                        rkty = 100
                        score = 0
                        if isload:
                            mbegin.play()

            elif event.type == pygame.KEYUP:  # 按键释放后将按下标志设置为 假
                isUppress = isDownpress = False

        if (not ispause) and (not isfail):  # 未暂停且未结束的情况下才处理移动
            if (rkty - rkstep >= 0) and isUppress:  # 球拍的边界处理，一直按着也能移动球拍
                rkty = rkty - rkstep
            if (rkty + rkth + rkstep <= HEIGHT) and isDownpress:
                rkty = rkty + rkstep

            if x > WIDTH:  # 球的边界处理
                speedx = -speedx
            elif x < (rkwh + radius):  # 左边界
                if (y > rkty) and (y < (rkty + rkth)):  # 球拍范围内
                    speedx = -speedx
                    score = score + 1  # 得分
                    if isload:  # 避免音频未正确加载导致的程序异常结束
                        mhit.play()
                else:  # 未击中球拍
                    ispause = True
                    isfail = True
                    if isload:
                        mfail.play()
            if (y > HEIGHT or y < 0):  # 上下边界
                speedy = -speedy
            x = x + speedx
            y = y + speedy

        pygame.draw.rect(screen, CRKT, (0, rkty, rkwh, rkth), 0)  # 画填充矩形：球拍
        pygame.draw.circle(screen, CBALL, (x, y), radius, 0)  # 画实心球

        # 找不到calibri字体就会使用pygame默认字体，都不支持中文
        ft = pygame.font.SysFont("calibri", 30)
        text = ft.render("Score: " + str(score), True, CFONT)
        screen.blit(text, (100, 0))
        if isfail:
            ftg = pygame.font.SysFont("calibri", 99)
            tover = ftg.render("Game Over", True, CFONT)
            trest = ft.render("Press SPACE to start again", True, CFONT)
            screen.blit(tover, (150, 200))
            screen.blit(trest, (220, 400))
        pygame.display.update()


if __name__ == '__main__':
    main()
