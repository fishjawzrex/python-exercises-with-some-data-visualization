from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#matplotlib inline
from sklearn import datasets
#Iris Dataset
iris = datasets.load_iris()
X = iris.data
#KMeans
km = KMeans(n_clusters=3)
km.fit(X)# at this point, the km object is changed/altered to the state of .fit(X)
#km.predict(X)
labels = km.labels_ # after applying the .fit(X) method to km, the .labels_ method is now activated and filled
#Plotting
fig = plt.figure()#1, figsize=(7,7))
ax = fig.add_subplot(111, projection = '3d')
#ax = Axes3D(fig, rect=[0, 0, 0.95, 1], elev=48, azim=134)
ax.scatter(X[:, 3], X[:, 0], X[:, 2],
          c=labels, edgecolor="k", s=50, alpha=.9) #.astype(np.float) cut from labels 
ax.set_xlabel("Petal width", color='gray')
ax.set_ylabel("Sepal length", color='gray')
ax.set_zlabel("Petal length", color='gray')
plt.title("USING SKLEARN TO IDENTIFY FEATURE CLUSTERS", fontsize=14, fontname='Times New Roman')
plt.show()

print(X)