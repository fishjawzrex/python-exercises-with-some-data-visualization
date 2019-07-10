import numpy as np
#import mnist
#data = mnist.train_images()

def shift(n):
    drum = []
    q = np.amax(n)
    t = np.amin(n)
    for obj in n:
        f = obj.astype(np.float32)
        z=((f-t)/(q-t))
        drum.append(z)
    return drum
    
#print shift(data)

    
