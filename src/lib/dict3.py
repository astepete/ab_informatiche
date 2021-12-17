# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

#remove a particular item
print(squares.pop(4))
print(squares)

#remove an arbitrary item
print(squares.popitem())
print(squares)

#remove all items
squares.clear()
print(squares)

#delete the dictionary itself
del squares
print(squares)