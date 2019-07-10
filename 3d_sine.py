'''exploring plotting 2d waves'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x = np.arange(-2*np.pi, 2*np.pi, .01)
y = np.arange(-2*np.pi, 2*np.pi, .01)
def f1(x,y):
	return np.sin(3*x)/x + np.sin(3*y)/y 
def f2(x,y):
	return np.sin(2*x)/x + np.sin(2*y)/y 
def f3(x,y):
	return np.sin(x)/x + np.sin(y)/y 
 
x,y = np.meshgrid(x,y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('x values', color='gray')
ax.set_ylabel('y values', color='gray')
ax.set_zlabel('z = Trig_function(x,y)', color='gray')

ax.set_title('3D Surface Plot', fontsize=20,
		  fontname='Times New Roman')
ax.set_xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi])
ax.set_yticks(())
ax.plot_surface(x,y,f1(x,y), rstride=1, cstride=1, cmap=plt.cm.hot)#, color='r')
#ax.plot_surface(x,y,f2(x,y))
#ax.plot_surface(x,y,f3(x,y), color='y')
plt.show()