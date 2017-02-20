#!/usr/bin/python
# -*- coding: UTF-8 -*-
from  matplotlib import pyplot as plt
def  runplot():
	plt.figure()
	plt.title('price and diameter data')
	plt.xlabel('diameter(inch)')
	plt.ylabel('price(dollar)')
	plt.axis([0,30,0,25])
	plt.grid(True)
	return plt
plot = runplot()
x = [[6],[8],[10],[14],[18]]
y = [[7],[9],[13],[17.5],[18]]
plot.plot(x,y,'k.')

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)			#training
x2 = [[0],[8],[10],[15],[20]]
y2 =  model.predict(x2)	#predict
y3 = [14.25,14.25,14.25,14.25,14.25]
y4 = y2 * 0.5 + 5
plot.plot(x2,y2,'g-.')
#plot.plot(x2,y3,'r-.')
#plot.plot(x2,y4,'y-.')

# model.fit(x[1:-1],y[1:-1])		#retraining
# y5 =  model.predict(x2)		#repredict
# plot.plot(x2,y5,'o-.')
yr = model.predict(x)
for index,i in enumerate(x):
	plot.plot([i,i],[y[index],yr[index]],'o-')
#plot.show()
import numpy
print numpy.mean((model.predict(x) - y) ** 2)




# import numpy as np
# import matplotlib.pyplot as plt
# plt.figure(1) # 创建图表1
# plt.figure(2) # 创建图表2
# ax1 = plt.subplot(211) # 在图表2中创建子图1
# ax2 = plt.subplot(212) # 在图表2中创建子图2
# x = np.linspace(0, 3, 100)
# for i in xrange(5):
#     plt.figure(1)  #❶ # 选择图表1
#     plt.plot(x, np.exp(i*x/3))
#     plt.sca(ax1)   #❷ # 选择图表2的子图1
#     plt.plot(x, np.sin(i*x))
#     plt.sca(ax2)  # 选择图表2的子图2
#     plt.plot(x, np.cos(i*x))
# plt.show()



