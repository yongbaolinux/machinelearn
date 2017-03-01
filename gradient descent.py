#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as pyplot

x = np.arange(-5, 5, 0.001)
y = x**3+x**2-x*10

pyplot.plot(x,y) 
pyplot.show()

'''start = 5
step = 0.001
goal = 0.00001

x = start
y0 = start**3+start**2-10*start
while  x<= end:
	y1 = (x+step)**3 + (x+step)**2-10*(x+step)
	if abs(y1 - y0) < goal:
		print x
	x = x + step
	y0 = y1;'''

#gradient descent
start = -3
alpha = 0.01
goal = 0.0001

y0 = start**3+start**2-10*start
x = start
while  (x > -5)  and (x < 5):
	x1 = x -  alpha * (3*x**2 + 2 * x - 10)
	y1 = x1**3+x1**2-10*x1
	if abs(y0 - y1) < goal:
		print x
		break;
	y0 = y1
	x = x1
