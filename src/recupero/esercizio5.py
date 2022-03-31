#per poter utilizzare il modulo creato bisogna richiamarlo all'interno del programma
import modulo as md

#variabile che permette di scegliere quale funzione utilizzare
a=int(input("Inserire 1 per il calcolo dell'area del quadrato, 2 per quella del rettangolo, 3 per quella del cerchio, 4 per il triangolo rettangolo:"))

#inizializzazione a 0 delle variabili che entreranno nella funzione
l=0.;m=0.

#if che richiama la funzione scelta al punto precedente
if(a==1):
  md.quadrato(l)
elif(a==2):
  md.rettangolo(l,m)
elif(a==3):
  md.cerchio(l)
else:
  md.triangolo(l,m)
  