# Intro
记录用python3的pygame做一个乒乓球游戏的每一小步，可从commit查看如何搭建起来的
# 使用方法
两种方法，自己选择其中一种即可
## 方法一：下载编译好的程序
win 或 linux见Releases,或者百度网盘
- [v0.0.0   提取码：64tb](https://pan.baidu.com/s/1gXiZ7HI2S1RdpVGpFuLWZg)

## 方法二：自行编译
### 准备环境
1. 安装python3 - 略
2. 安装pygame模块 - `pip3 install pygame`
3. (非必须，可跳过, 只是没声音、图片而已)下载音频和图片压缩包，解压放到代码相同目录下，[百度网盘 提取码: q6cw](https://pan.baidu.com/s/12QXF2530ymr_sdXAa-e43g)
### 开始玩耍
1. 下载代码
2. `python3 pong.py`, 开始游戏之后，按键盘W/S按键控制球拍上下移动，接住球即可继续游戏，没接住的话游戏结束。结束后按空格可以重新开始游戏
# 按键控制
空格： 暂停/开始  
W： 上  
S： 下
# License
GPL 3.0
# Log
从V0.0.0之前，显示图形和图形碰撞检测都是自己调用draw和粗略的进行距离判断，但是如果球多起来，对象的个体数一多起来，对象的种类多起来的时候，这个时候再为为一个类手写不同的碰撞检测方法就会是一个庞大又繁琐的工程，这个时候不得不提pygame里面提供的Sprite和Group了。

Sprite为我们提供了一个装载游戏对象的类，比如这里面的球拍和球，而Group则是Sprite的组合，可以轻松的对Group里面的各个sprite进行碰撞检测、删除、绘制。
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
- [python class Doc](https://docs.python.org/zh-cn/3/tutorial/classes.html)
- [pygame.sprite Doc](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite)
- [05a-Exercises-pygame-sprites](https://github.com/ILS-Z399/05a-Exercises-pygame-sprites)
- [pygame 的精灵使用](https://www.cnblogs.com/liquancai/p/13256388.html)
- [（一般误粗翻）Pygame 官方文档 - pygame.sprite](https://blog.csdn.net/Enderman_xiaohei/article/details/88218773)
- [random](https://www.runoob.com/python/func-number-random.html)
- [assert](https://www.runoob.com/python3/python3-assert.html)
- [logging](https://www.jianshu.com/p/feb86c06c4f4)
- [pygame.update()与pygame.flip()的区别](https://www.cnblogs.com/hiuhungwan/p/11180900.html)
- [Icofont-阿里巴巴](https://www.iconfont.cn/?spm=a313x.7781069.1998910419.d4d0a486a)
- [pygame库写游戏——入门<8>——动画和帧率](https://blog.csdn.net/weixin_40497712/article/details/78763922)
