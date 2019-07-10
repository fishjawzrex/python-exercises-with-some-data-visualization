import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d 
x = np.round(np.random.random((1,50))*10)

y = np.round(np.random.random((1,50))*10)

z = np.round(np.random.random((1,50))*10)

w = np.round(np.random.random((50,50))*10)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('this is the x label bro')
ax.set_ylabel('wtf do you think? y label')
ax.set_zlabel('z label duh!')

ax.scatter(x,y,z, c='c', marker='o')
plt.show()