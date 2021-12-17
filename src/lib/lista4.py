a = []
a.extend(range(1, 10))
b=[el*2 for el in a]
print(b)

l=[1,2]
l2=['a','b']
l3=[4,5]
f=[(e1,e2,e3) for e1 in l for e2 in l2 for e3 in l3]
print(f)
