def rett_unif(int_temp,pos_iniz):
  v=float(input("Inserisci la velocità:"))
  s=v*int_temp+pos_iniz
  return(s)

def unif_acc(int_temp,pos_iniz):
  v0=float(input("Inserisci la velocità iniziale:"))
  a=float(input("Inserisci l'accelerazione:"))
  s=0.5*a*int_temp**2+v0*int_temp+s0
  return(s)


Delta_t = float(input("Inserisci l'intervallo temporale: "))
s0=float(input("Inserisci la posizione iniziale:"))
a=int(input("Seleziona 0 per moto rettilineo uniforme o 1 per moto uniformemente accelerato:"))

if (a==0):
  print(rett_unif(Delta_t,s0))
else:
  print(unif_acc(Delta_t,s0))
