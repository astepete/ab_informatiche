#Slicing operator

L=['spam','Spam','SPAM!']

print(L[2]) #Offset start at zero

print(L[-2]) #Negative: count from the right

print(L[1:]) #Slicing fetches sections

#Another example

a=[0,1,2,3,4,5,6,7]

print(a[0:6])

print(a[1:6:2])

print(a[1::2]) #no stop means until the end of the list

print(a[::2]) #no start means from the first item of the list

print(a[6:0:-2]) #Slicing can also be negative: starts from index 6, ends to index 0 going back with step 2


