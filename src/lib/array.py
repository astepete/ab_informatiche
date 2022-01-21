import numpy as np

v=np.array([1,2,3,4])
list1=[1,2,3,4]
tupla=(5,6,7,8)

a=np.array(list1) #from a list

b=np.array(tupla) #from a tupla

c=np.array([list1,tupla]) #from a list and from a tupla

print(v.dtype)

print(a)
print(a.dtype)

print(b)
print(b.dtype)

print(c)
print(c.dtype)
