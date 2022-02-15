import numpy as np

a=np.array(range(1,9))

print("Shape", a.shape)

c_style=a.reshape((2,2,2),order='C')

f_style=a.reshape((2,2,2),order='F')

print("C-style", c_style)

print("Fortran-style", f_style)

c_style=c_style.reshape((2,4))
print("Reshape C-style", c_style)

f_style=f_style.reshape((2,4))
print("Reshape F-style", f_style)
