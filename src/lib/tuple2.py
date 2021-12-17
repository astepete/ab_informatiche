tup=('physics','chemistry',1997,2000)
print (tup)
del tup
print("After deleting tup:")
print(tup)

#In general tuple cannot be modified. This produces an exception raised, because after del tup, tuple does not exist anymore.