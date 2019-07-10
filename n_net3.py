import mnist

import numpy as np

class Network(object):
    def __init__(self, layers):
        self.layers = layers
        self.biases = [np.random.randn(y,1) for y
                        in layers[1:]]
        self.weights = [np.transpose(np.random.randn(x,y))
                        for x,y
                        in zip(layers[:-1],layers[1:])]
        self.num_layers = len(layers)
        print self.weights
    def SGD(self, training_data, mini_batch_size, 
            epochs, eta, test_data=None):
        #if test_data.all():
        n_test = len(test_data)
        n = len(training_data)
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
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x.ravel()[:,None] #create extra dimension
        activations = [x.ravel()] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            #the shape of q looks fine (30L,)
            q = np.dot(w, activation)
            q[:,None] #reshape q from (30L,) to (30L, 1L)
            #why is z shaped (30L,30L)?
            z =  q + b 
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # backward pass
        #print self.cost_derivative(activations[-1], y)
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])#set first delta 
        nabla_b[-1] = delta#set last dC/db to delta vector 
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        #print activations[-1].shape 
        #calculate nabla_b, nabla_w for the rest of the layers
        for g in range(2, self.num_layers):
            z = zs[-g]
            sp = sigmoid_prime(z)           
            delta = np.dot(self.weights[-g+1].transpose(), delta)* sp
            nabla_b[-g] = delta
            nabla_w[-g] = np.dot(delta, activations[-g-1][:, None].transpose())
        #print nabla_w[1]
        #print nabla_w.shape  
        return (nabla_b, nabla_w)
        
     
    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        a = a[:, None]
        for b, w in zip(self.biases, self.weights):
            #print a.shape, 'a_1'
            #print b.shape, 'b'
            #print w.shape, 'w'
            a = sigmoid(np.dot(w, a)+b)
            #print len(a), a.shape 
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

