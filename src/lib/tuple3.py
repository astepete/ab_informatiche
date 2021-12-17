#Basic operation with tuple

tup1=(1,2,3)
tup2=(4,5,6)
tup3=('Hi!',)

print("Lunghezza della tuple1: ", len(tup1))
print("Combinazione di tuple1 e tuple2:", tup1+tup2)
print("Moltiplicazione di tuple 3: ", tup3*4)
print("Vedere se è presente un elemento in tuple1",3 in tup1)
for x in tup1:
  print ("Stampa gli elementi di tuple1:", x)
