# numpy intro start

import numpy as np;
n1 = np.array([12,34,54]) # single dimension array
n2 = np.array([[12,23,45],[32,445,56]]) # multi dimensional array
print(n2)

print(type(n1))

n3 = np.zeros((2,9)) # zeros will print in arrays 2 --> row 
print(n3)

# intializing the numpy array with same number
n4= np.full((5,3,),7)
print(n4)

# numpay array with range
n5=np.arange(10,20,5)  # [10 11 12 13 14 15 16 17 18 19]
print(n5)

# numpy array with random numbers
n6=np.random.randint(1,200,12)
print(n6)


