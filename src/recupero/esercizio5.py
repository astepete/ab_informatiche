import modulo as md

a=int(input("Inserire 1 per il calcolo dell'area del quadrato, 2 per quella del rettangolo, 3 per quella del cerchio, 4 per il triangolo rettangolo:"))

l=0.;m=0.

if(a==1):
  md.quadrato(l)
elif(a==2):
  md.rettangolo(l,m)
elif(a==3):
  md.cerchio(l)
else:
  md.triangolo(l,m)
  