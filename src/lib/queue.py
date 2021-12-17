stack=[1,2,3,4]
print('Initial stack:', stack)

for i in range(5,7):
   stack.append(i)
print("Append:", stack)
stack.pop()
print("Pop:", stack)

queue=['a','b','c','d']
print("Initial Queue:", queue)
queue.append('e')
queue.append('f')
print("Append:", queue)
queue.pop(0)
print("Pop:", queue)
