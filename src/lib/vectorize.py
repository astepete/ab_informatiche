import numpy as np

a=np.arange(0,4*np.pi,0.1)

#VECTORIZED VERSION

y=np.sin(a)*2

#SCALAR VERSION
z=np.zeros(len(a))
for i in range(len(a)):
  z[i]=np.sin(a[i])*2

print(y)
print(z)
