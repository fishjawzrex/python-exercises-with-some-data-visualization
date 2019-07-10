#this is the code to run the network

import mnist
#import normed 
import n_net
#import new_mat
#import shift
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
net = n_net.Network([784,30,10])
training_data =  zip(data, mnist.train_labels())
test_data = zip(data_2, mnist.test_labels())
net.SGD(training_data,10,100,0.00000195,test_data=test_data)