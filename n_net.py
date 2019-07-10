'''THIS SCRIPT IS A NEURAL NETWORK DESIGNED USING STOCHASTIC GRADIENT DESCENT AND 
BACK-PROPAGATION TO TRAIN ITSELF TO RECOGNIZE HAND-WRITTEN DIGITS FROM THE MNIST 
DATABASE'''

''' import mnist dataset: each image object is represented
by a 784x784 matrix of numbers each number representing a
pixel value on a gradient from white to black'''
import mnist

'''import numpy library'''
import numpy as np


from matplotlib import pyplot as plt

'''USE NUMPY.RANDOM.SEED TO SET/KEEP INITIAL CONDITIONS IN ORDER TO TEST INPUTS'''

np.random.seed(0)

# CREATE NETWORK CLASS
class Network(object):
    #METHOD FOR INITIALIZING THE DEPTH OF THE NETWORK AND THE 
    #SIZE OF EACH LAYER
    def __init__(self, layers):
        self.layers = layers
        self.biases = [np.random.randn(y,1) for y
                        in layers[1:]]
        self.weights = [np.transpose(np.random.randn(x,y))
                        for x,y
                        in zip(layers[:-1],layers[1:])]
        self.num_layers = len(layers)

            
    
    def SGD(self, training_data, mini_batch_size, 
            epochs, eta, test_data=None):
        
        n_test = len(test_data)
        n = len(training_data)
        cache_x = []
        cache_y = []
        for j in range(epochs):
            np.random.shuffle(training_data)
            mini_batches = [training_data[k:k+mini_batch_size]
                            for k in range(0,n,mini_batch_size)]
            
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print "Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test)
            else:
                print "Epoch {0} complete".format(j)
            cache_x.append(j)
            cache_y.append(self.evaluate(test_data))
        
        plt.title('NETWORK PERFORMANCE', fontsize=20,	
		          fontname='Times New Roman')
        plt.xlabel('Epoch', color='gray')
        plt.ylabel('Success Rate', color='gray')
        plt.plot(cache_x,cache_y)
        plt.show()
        
    #ADJUST/UPDATE THE WEIGHTS IN EACH MINIBATCH
    def update_mini_batch(self, mini_batch, eta):
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        for x,y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x,y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
            self.weights = [w-(eta/len(mini_batch))*nw
                            for w, nw in zip(self.weights, nabla_w)]
            self.biases = [b-(eta/len(mini_batch))*nb
                           for b, nb in zip(self.biases, nabla_b)]
                                
    def backprop(self,x,y):
        #CREATE ZERO MATRIX IN SHAPE OF WEIGHTS AND BIASES
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x.ravel()[:,None] #create extra dimension
        activations = [x.ravel()] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        counter_1 = 0
        for b, w in zip(self.biases, self.weights):
           
            q = np.dot(w, activation)
            q[:,None] #reshape q from (30L,) to (30L, 1L)
            
            z =  q + b 
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
            counter_1 += 1
        # backward pass
       
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])#set first delta 
        
        nabla_b[-1] = delta#set last dC/db to delta vector 
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
       
        for g in range(2, self.num_layers):
            z = zs[-g]
            sp = sigmoid_prime(z) 
           
            v = activations[-g-1]            
            if g+1 == self.num_layers:
                v = activations[-g-1][:, None]
                
            
            delta = np.dot(self.weights[-g+1].transpose(), delta)* sp
            nabla_b[-g] = delta
            nabla_w[-g] = np.dot(delta, v.transpose())
            
        return (nabla_b, nabla_w)
        
     
    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        a = a[:, None]
        for b, w in zip(self.biases, self.weights):

            a = sigmoid(np.dot(w, a)+b)
           
        return a
        
    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = [(np.argmax(self.feedforward(x.ravel())), y)
                        for (x, y) in test_data]#compares the most 
        #activated node in last layer with target value(y)
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        return (output_activations-y)

#### Miscellaneous functions
def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))

