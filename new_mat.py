import numpy as np
#import mnist
#data = mnist.train_images()
#store = data[0]
def ms(data):
    for i in range(len(data)):
        if i==0:
            new_mat = data[i]
        else:
            np.vstack((new_mat,data[i]))
 
    #print new_mat

    m = np.mean(new_mat)
    s = np.std(new_mat)

    return m,s 

    
#print ms(data)