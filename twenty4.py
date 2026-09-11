#Sorting

import numpy as np #type: ignore
x= np.array([1,2,3,4,5,6,7,8,9])
y = np.sort(x)
print(y)

import numpy as np #type: ignore
x= np.array([1,2,3,4,5,6,7,8,9])
y = np.argsort(x)
print(y)



import numpy as np #type: ignore
x= np.array([1,2,3,4,5,6,7,8,9])
y = np.sort(x)[::-1]
print(y)


import numpy as np #type: ignore
x= np.array([[1,7,3],
             [4,9,6],
             [2,5,8]])
y =np.sort(x)
print(x)

import numpy as np #type: ignore
x= np.array([[1,7,3],
             [4,9,6],
             [2,5,8]])
y =np.sort(x)
print(y)

import numpy as np #type: ignore
x= np.array([[1,7,3],
             [4,9,6],
             [2,5,8]])
y =np.sort(x,axis=0)
print(y)

import numpy as np #type: ignore
x= np.array([[1,7,3],
             [4,9,6],
             [2,5,8]])
y =np.sort(x,axis=1)
print(y)

import numpy as np #type: ignore
x= np.array([[1,7,3],
             [4,9,6],
             [2,5,8]])
x.sort()
print(x)