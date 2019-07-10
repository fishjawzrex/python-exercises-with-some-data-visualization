'''exploring plotting 2d waves'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, .01)
y1 = np.sin(3*x)/x 
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x  

plt.xlabel('x values')
plt.ylabel('y = f(x)')
plt.title('Trigonometric 2D Waves', fontsize=20,
		  fontname='Times New Roman')
plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi])
plt.yticks()
plt.plot(x,y1)
plt.plot(x,y2,'r-')
plt.plot(x,y3, 'g')
plt.grid(True)
plt.show()