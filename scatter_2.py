import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

a = np.random.random((1,50))
b = np.random.random((1,50))
c = np.random.random((1,50))
'''
x = np.random.random((1,20))*2
y = np.random.random((1,20))*2
z = np.random.random((1,20))*2
az = np.random.random((1,10))*.5
bz= np.random.random((1,10))*.5
cz = np.random.random((1,10))*.5'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('random x values')
ax.set_ylabel('random y label')
ax.set_zlabel('z label')
ax.set_title('this is a random scatter plot',
              fontsize=20, 
			  fontname='Times New Roman')

ax.scatter(a,b,c, marker='o',
		   c='r', s=50, edgecolor='k', alpha=1)
#ax.scatter(x,y,z, marker='^', c='b', s=50, edgecolor='k', alpha=.6)
#ax.scatter(az,bz,cz, marker='*', c='y', s=50, edgecolor='k', alpha=.6)
plt.show()
