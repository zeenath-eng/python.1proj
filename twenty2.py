#Indexing in numpy

import numpy as np  # type: ignore 
arr1 =np.array([1,2,3,4,5])
print(arr1[0])
print(arr1[-1])


import numpy as np  # type: ignore 
arr2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr2[:3])

#Slicing in numpy
import numpy as np #type: ignore
arr =np.array([1,2,3,4,5,6,7,8,9])
print(arr[1:9:2])
print(arr[1:5])
print(arr[-1:-5:-1])
print(arr[-1:-5:-2])
print(arr[::2])
print(arr[::-2])
print(arr[::-1])

import numpy as np #type: ignore
arr =np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr[1,])
print(arr[:,])
print(arr[1:3,2:5])
print(arr[1:3, ])
print(arr[:,1:3])
print(arr[1:3, 1])