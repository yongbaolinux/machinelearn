#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image
imageHandler = Image.open('./4')
from knn import *
width,height = imageHandler.size
imgData = list(imageHandler.getdata())


level = 255 * 3 / 4
matrix  = zeros(width*height)
for j in range(height):
    for i in range(width):
        matrix_index = j*width+i
        if sum(imgData[matrix_index]) > level:
            matrix[matrix_index] = 0
        else:
            matrix[matrix_index] = 1

left_x = 0
left_y = 0
#left_y
for j in range(height):
    sum_  = 0
    for i in range(width):
        sum_ += int(matrix[j*width + i])
    if sum_  < 5:
        left_y += 1
    else:
        break
#left_x
for i in range(width):
    sum_ = 0
    for j in range(height):
        sum_ += int(matrix[j*width+i])
    if sum_ < 5:
        left_x += 1
    else:
        break

right_x = width -1
right_y = height-1
#right_y
for j in range(height-1,-1,-1):
    sum_ = 0
    for i in range(width):
        sum_ += int(matrix[j*width+ i])
    if sum_ < 3:
        right_y -= 1
    else:
        break

#righ_x
for i in range(width-1,-1,-1):
    sum_ = 0
    for j in range(height):
        sum_ += int(matrix[j*width + i])
    if sum_ < 5:
        right_x -= 1
    else:
        break

#spread 3 pixels
left_x  -= 10
left_y -= 10
right_x += 10
right_y += 10

##
goal_x = 32                                   #黑白点阵压缩图像宽度
goal_y = 32                                   #黑白点阵压缩图像高度
x_unit = (right_x -  left_x) / goal_x         #宽度循环块单位
y_unit = (right_y - left_y) / goal_y          #高度循环块单位

matrix_ = zeros(goal_x*goal_y)                #生成初始化都为0的矩阵 用来存放压缩后的图像信息
matrix_index = -1                             #压缩后图像存放矩阵索引

for y in range(left_y,left_y+goal_y*y_unit,y_unit):
    for x in range(left_x,left_x+goal_x*x_unit,x_unit):
        pixelSum = 0
        matrix_index += 1
        for j in range(y,y+y_unit):
            for i in range(x,x+x_unit):
                pixelSum += int(matrix[j*width+i])
        if pixelSum >= 1:
            matrix_[matrix_index] = 1
        else:
            matrix_[matrix_index] = 0

writeHandler = open('./goal.txt','w')
for k,v in enumerate(matrix_):
    writeHandler.write(str(int(v)))
    if ((k+1) % 32) == 0:
        writeHandler.write('\n')
writeHandler.close()

getFile('./trainingDigits','./goal.txt')


