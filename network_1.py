import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()
data = digits.data
target = digits.target
target_names = digits.target_names
images = digits.images

np.random.seed(0)

def sigmoid(n):
	return 1/(1+np.e**(-n))
	
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

network = [int(x) for x in input("Enter the Layers:")]

test_image = images[26].ravel()
activation = test_image

a_list = []
for i in range(len(network)-1):
	w = np.random.rand(network[i],network[i+1])
	b = np.random.rand(network[i+1])
	e = np.transpose(w)
	z = np.matmul(e,activation) + b 
	#h = np.zeros(len(z))
	activation = sigmoid(z)#np.maximum(z,h)
	a_list.append(activation)
	
result = [0,0,0,0,0,0,1,0,0,0]

c = .5*(a_list[-1] - result)**2

print c 

