'''this file is intended to practice the use
of pyplot in matlab.'''

#import packages/modules
import matplotlib.pyplot as plt
import numpy as np

#use the axis class in the plt package to set
#the frame/dimensions of the canvas
plt.axis([0,5,0,20])
#set label and title 
plt.title('My first plot', fontsize=20,	
		   fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values', color='gray')

#show grid 
plt.grid(True)

#label the points/coordinates
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.figtext(2,3,'hello')

#use latex and bbox 
plt.text(1.1,12, '$y = x^2$', fontsize=20, 
		 bbox={'facecolor':'yellow', 'alpha':0.2})
		 
#add legend
plt.legend(['First Series'])
		 		 
#plot figure
plt.plot(np.arange(1,5),np.arange(1,5)**2,'ro')#[1,4,9,16]
#display figure 
plt.show()