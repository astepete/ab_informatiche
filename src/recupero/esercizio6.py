#importiamo una libreria di python per vedere il funzionamento delle funzioni richieste
import math

#stampiamo a video gli attributi della libreria python math
print(dir(math))

#definiamo due variabili: la prima è un intero, la seconda è una stringa
a=3
b="pippo"

#utilizziamo la funzione type per vedere il tipo di variabile che passiamo nell'argomento
print(type(a))
print(type(b))

#richiamiamo due funzioni della libreria math e, utilizzando l'help scopriamo le informazioni contenute in esse
help(math.acos)
help(math.log10)