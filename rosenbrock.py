# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation as amat

"this function: f(x,y) = (1-x)^2 + 100*(y - x^2)^2"


'''def Rosenbrock(x, y):
    #return np.power(1 - x, 2) + np.power(100 * (y - np.power(x, 2)), 2)
    return x**2+y**2


def show(X, Y, func=Rosenbrock):
    fig = plt.figure()
    ax = Axes3D(fig)
    X, Y = np.meshgrid(X, Y, sparse=True)
    Z = func(X, Y)
    plt.title("gradeAscent image")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow', )
    ax.set_xlabel('x label', color='r')
    ax.set_ylabel('y label', color='g')
    ax.set_zlabel('z label', color='b')
    amat.FuncAnimation(fig, Rosenbrock, frames=200, interval=20, blit=True)
    plt.show()

if __name__ == '__main__':
    X = np.arange(-2, 2, 0.1)
    Y = np.arange(-2, 2, 0.1)
    Z = Rosenbrock(X, Y)
    show(X, Y, Rosenbrock)'''


fig =  plt.figure()
ax = Axes3D(fig)
x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
x ,y= np.meshgrid(x, y, sparse=True)
#z = x**2 + y**2
z = (1-x)**2 + 100*(y-x**2)**2 #rosenbrock funcion
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow', )
plt.title("gradeAscent image")
ax.set_xlabel('x label', color='r')
ax.set_ylabel('y label', color='g')
ax.set_zlabel('z label', color='b')

#plt.show()

x0 = -1
y0= 0
step = 0.0008
goal = 0.001

#z0 = x0**2 + y0**2
z0 = (1-x0)**2 + 100*(y0-x0**2)**2

while (x0 >=-2) and (x0 <= 2) and (y0>=-2) and (y0<=2):
    #x1 = x0 - step*2*x0
    #y1 = y0 - step*2*y0
    #z1 = x1**2 + y1**2

    x1 = x0 - step *(-400*x0*(y0-x0**2)+2*x0-2)
    y1 = y0 - step *(200*(y0-x0**2))
    z1 = (1-x1)**2 + 100*(y1-x1**2)**2
    
    if abs(z1-z0) < goal:
        print x0,y0
        break;
    z0 = z1
    x0 = x1
    y0 = y1






