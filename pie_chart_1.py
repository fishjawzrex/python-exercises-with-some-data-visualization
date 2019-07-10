'''The purpose of this code is to demostrate 
the use of a pie chart in Python for data 
visualization'''

import numpy as np
import matplotlib.pyplot as plt

chart = [38,23,54,56,12,43]
labels = ['Food', 'Gas', 'Water', 'Rent',
		  'Insurance', 'Electricity']
colors = ['yellow','green','red',
		  'blue', 'cyan', 'magenta']
explode = [.3, 0,0,0,0,0]
plt.title('Sample Budget Pie Chart', fontsize=20,
		  fontname='Times New Roman')

plt.pie(chart,colors=colors, labels=labels, 
		shadow=True, explode=explode)
plt.axis('equal')
plt.show()