# Intro
记录用python3的pygame做一个乒乓球游戏的每一小步，可从commit查看如何搭建起来的
# 使用方法
两种方法，自己选择其中一种即可
## 方法一：下载编译好的程序
见Releases

## 方法二：自行编译
### 准备环境
1. 安装python3 - 略
2. 安装pygame模块 - `pip3 install pygame`
3. (非必须，可跳过, 只是没声音而已)下载音频文件，自行查找乒乓球击球音效、开场音效、失败音效、背景音效，然后转换为ogg格式或者wvb格式，然后修改代码中的几个音频路径`MUSICPATH`，找不到这里有一份压缩好的[音频素材包（ 提取码: nadg）](https://pan.baidu.com/s/10R6ryFxi_YD-UpVQpiHsiQ)
### 开始玩耍
1. 下载代码
2. `python3 pong.py`, 开始游戏之后，按键盘上下按键控制球拍上下移动，接住球即可继续游戏，没接住的话游戏结束。结束后按空格可以重新开始游戏
# 按键控制
空格： 暂停/开始  
上/W： 上  
下/S： 下
# License
GPL 3.0
# References
- [ grantjenks /free-python-games ](https://github.com/grantjenks/free-python-games)
- [python按键按住不放持续响应代码](https://blog.csdn.net/baidu_39560388/article/details/84612605)
- 格式转换工具：[FF Multi Converter](https://github.com/ilstam/FF-Multi-Converter)
- [魔音MUSIC](http://moyimusic.com/)
- [Pygame：播放声音和音效](https://blog.csdn.net/w15977858408/article/details/104283348)
- [Do not use bare except, specify exception instead (E722)](https://www.flake8rules.com/rules/E722.html)
- [python 查看错误类型](https://blog.csdn.net/weixin_44737399/article/details/89092300)
- [pygame获取系统中的字体](https://blog.csdn.net/weixin_45951701/article/details/107425502)
- [Pygame添加静态文字详解](https://blog.csdn.net/cool99781/article/details/106752516)
- [PyGame字体](https://blog.csdn.net/Hubz131/article/details/86740969)
- [Python int与string之间的转化](https://www.cnblogs.com/nzbbody/p/3581048.html)
- [pyinstaller将python程序打包成windows系统下的可执行文件 - exe文件](https://blog.csdn.net/weixin_43031092/article/details/109162262)
