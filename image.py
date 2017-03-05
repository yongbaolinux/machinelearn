#!/usr/bin/python
# -*- coding: UTF-8 -*-

from numpy import *
from PIL import Image
imageHandler = Image.open('./2')
#print type(imageHandler)
#imageHandler.save('./2', "JPEG")
width,height = imageHandler.size
imgData = list(imageHandler.getdata())

goal_x = 32                     #黑白点阵压缩图像宽度
goal_y = 32                     #黑白点阵压缩图像高度
x_unit = width / goal_x         #宽度循环块单位
y_unit = height / goal_y        #高度循环块单位
level = 255 * 3 * x_unit * y_unit / 3  #定义黑白阀值 每一块的像素求和若大于该值 则定义为白 设为0 若小于该值 则定义为黑 设为1
matrix = zeros(goal_x*goal_y)   #生成初始化都为0的矩阵 用来存放压缩后的图像信息
matrix_index = -1;               #压缩后图像存放矩阵索引

for y in range(0,height,y_unit):
    for x in range(0,width,x_unit):
        pixelSum = 0
        matrix_index += 1
        for j in range(y,y+y_unit):
            for i in range(x,x+x_unit):
                pixelSum += sum(imgData[j*width+i])
        if pixelSum >= level:
            matrix[matrix_index] = 0
        else:
            matrix[matrix_index] = 1

writeHandler = open('./2.txt','w')
for k,v in enumerate(matrix):
    writeHandler.write(str(int(v)))
    if ((k+1) % 32) == 0:
        writeHandler.write('\n')
writeHandler.close()
