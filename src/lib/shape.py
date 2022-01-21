import numpy as np

a=np.array([[1,2],[2,2]])

print(a.shape)
print(a.ndim)
print(a.itemsize)

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(b.shape)
print(b.ndim)
print(b.itemsize)

c=a+b

print(c.shape)
print(c.ndim)
print(c.itemsize)
