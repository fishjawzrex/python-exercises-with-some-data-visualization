'''KNearestNeighbors'''

import numpy as np
from sklearn import datasets
np.random.seed(0)
iris=datasets.load_iris()
x = iris.data
y = iris.target
i = np.random.permutation(len(iris.data))
x_train = x[i[:-10]]
y_train = y[i[:-10]]
x_test = x[i[-10:]]
y_test = y[i[-10:]]
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
#KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#           metric_params=None, n_jobs=None, n_neighbors=5, p=2,
#           weights='uniform')
j = knn.predict(x_test)
print j
print y_test