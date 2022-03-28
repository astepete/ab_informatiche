def quadrato(l):
  l=float(input("Inserire il lato del quadrato:"))
  print("L'area del quadrato e':",l**2)

def rettangolo(a,b):
  a=float(input("Inserire base del rettangolo:"))
  b=float(input("Inserire l'altezza:"))
  print("L'area del rettangolo e':", a*b)

def cerchio(r):
  r=float(input("Inserire il raggio del cerchio:"))
  pi=3.1415926535
  print("L'area del cerchio e':",pi*r**2)

def triangolo(c,C):
  c=float(input("Inserire il cateto minore del triangolo:"))
  C=float(input("Inserire il cateto maggiore:"))
  print("L'area del triangolo rettangolo e':", c*C*0.5)