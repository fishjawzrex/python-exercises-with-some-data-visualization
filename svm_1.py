import mnist
import normed 
import n_net
import new_mat
import shift
from sklearn import svm
data = mnist.train_images()
#standardize training data 
#data = normed.normed(data)
#normalize training data 
#data = shift.shift(data)
data_2 = mnist.test_images()
#standardize test data 
#data_2 = normed.normed(data_2)
#normalize test data 
#data_2 = shift.shift(data_2)
training_data =  zip(data, mnist.train_labels())
test_data = zip(data_2, mnist.test_labels())

clf = svm.SVC(gamma=.001, C=100)
clf.fit(data, mnist.test_labels())
print('prediction:', clf.predict(data_2))
print('target:', mnist.test_labels())