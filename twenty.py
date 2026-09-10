#Numpy arrays

import numpy as np  # type: ignore[import-not-found]
l1 =[1,2,3.5,"hi",4,5]
array1 = np.array(l1)
print(array1)
print(type(array1))


import numpy as np  # type: ignore[import-not-found]
l2 =[[1,2,3],[4,6,5],[7,8,9]]
arr2 = np.array(l2)
print(arr2)

#Range 
import numpy as np  # type: ignore[import-not-found]
arr1 =np.arange(1,10)
print(arr1)

import numpy as np  # type: ignore[import-not-found]
arr2 =np.arange(11,19).reshape((2,4))
print(arr2)

import numpy as np  # type: ignore[import-not-found]
arr3 = np.zeros((15,7))
print (arr3)

import numpy as np  # type: ignore[import-not-found]
arr4 = np.ones((5,5))
print (arr4)
