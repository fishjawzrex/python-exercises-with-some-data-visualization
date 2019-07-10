'''THIS SCRIPT USES LINEAR REGRESSION TO SHOW THE
CORRELATION BETWEEN AGES OF PATIENTS AND THE PROGRESSION
OF THE DISEASE, DIABETES'''

import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn import datasets

#load diabetes dataset 
diabetes = datasets.load_diabetes()

#select all but the last 20 samples as the training set 
#with data and targets
x_train = diabetes.data[:-20]
y_train = diabetes.target[:-20]
#select the last 20 samples as the test data 
x_test = diabetes.data[-20:]
y_test = diabetes.target[-20:]
#use the first column/feature(age)
x0_test = x_test[:,0]
x0_train = x_train[:,0]
x0_test = x0_test[:,np.newaxis]
x0_train = x0_train[:,np.newaxis]
#import linear_model folder and LinearRegression class 
linreg = linear_model.LinearRegression()

#fit data 
linreg.fit(x0_train,y_train)
y = linreg.predict(x0_test)

#plot data 
plt.scatter(x0_test,y_test,color='k')
plt.plot(x0_test,y,color='b',linewidth=3)
plt.show()
