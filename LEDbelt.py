# -*- coding: UTF-8 -*-
# 实验效果：控制WS2812单线RGB LED灯
# 接线：使用windows或linux电脑连接一块arduino主控板，ws2812灯接到D9口

import time
from pinpong.board import Board, Pin, NeoPixel  # 导入neopixel类

Board("uno").begin()  # 初始化，选择板型(uno、leonardo、xugu)和端口号，不输入端口号则进行自动识别
# Board("uno","COM36").begin()      #windows下指定端口初始化
# Board("uno","/dev/ttyACM0").begin() #linux下指定端口初始化
# Board("uno","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

NEOPIXEL_PIN = Pin(Pin.D9)
PIXELS_NUM = 60  # 灯数
BRIGHTNESS = 200

np = NeoPixel(NEOPIXEL_PIN, PIXELS_NUM)
np.brightness(NEOPIXEL_PIN, BRIGHTNESS)

# #NeoPixel.brightness(NEOPIXEL_PIN, BRIGHTNESS)
n = 0
np[0] = (0, 255, 0)  # 设置第一个灯RGB亮度
time.sleep(1)

while n < PIXELS_NUM:
    np[n] = (0, 255, 0)  # 设置第一个灯RGB亮度
    n = n + 1

    time.sleep(0.01)
