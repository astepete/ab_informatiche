import time

a = []
a.extend(range(1, 1000))

b = []
b.extend(range(1, 100))

T1=time.time()
s=a+b
T2=time.time()

print("execution time: :" , T2-T1)

T3=time.time()
a.extend(b)
T4=time.time()

print("extend execution time:", T4-T3)
