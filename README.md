# Intro
记录用python3的pygame做一个乒乓球游戏的每一小步，可从commit查看如何搭建起来的
# 使用方法
## 准备环境
1. 安装python3 - 略
2. 安装pygame模块 - `pip3 install pygame`
3. (非必须，可跳过)找一段1s的乒乓球击球音频，转换为ogg格式或者wvb格式，然后修改代码中的音频路径`MUSICPATH`，找不到这里有一个[pong.ogg（ 提取码: ipew）](https://pan.baidu.com/s/1xugjDaw7tcCEM5SnfRYdDA )
## 开始
1. 下载代码
2. `python3 pong.py`, 游戏启动之后，按键盘上下按键控制球拍上下移动，接住球即可继续游戏，没接住的话游戏结束。
# License
GPL 3.0
# References
- [ grantjenks /free-python-games ](https://github.com/grantjenks/free-python-games)
- [python按键按住不放持续响应代码](https://blog.csdn.net/baidu_39560388/article/details/84612605)
- [Pygame：播放声音和音效](https://blog.csdn.net/w15977858408/article/details/104283348)
- [Do not use bare except, specify exception instead (E722)](https://www.flake8rules.com/rules/E722.html)
- [python 查看错误类型](https://blog.csdn.net/weixin_44737399/article/details/89092300)