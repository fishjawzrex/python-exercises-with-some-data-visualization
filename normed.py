import numpy as np
import new_mat
#import mnist 

#data = mnist.train_images()
def normed(d):
    '''THIS IS A FUNCTION THAT TRANSFORMS MATRIX DATA BY NORMALIZING AND 
    STANDARDIZING THE IMAGE, AND THEN APPENDING IT TO A LIST AND \
    RETURNING THE RESULT'''
    m,s = new_mat.ms(d)
    p = len(d)
    #Create an empty cache to append each image array after it has
    #been Normalized and Standardized
    normed_d = []
    for w in d:
        #Convert each matrix image array  into a float then
        #Normalize each matrix in mnist.train_images()
        f = w.astype(np.float32)#/255 
        #Standardize each image pixel value 
        z=(f-m)/s
        
        #Append to normed_d list 
        normed_d.append(z)

    return normed_d
    
#print np.mean(normed(data)[7]), np.std(normed(data)[7])