import math

print("Inserisci il numero intero da voler convertire:")
var = int(input())

oct=oct(var)
hex=hex(var)
bin=bin(var)

print("Le rappresentazioni ottale, esadecimanle e binaria del numero inserito sono:\n",oct,hex,bin)