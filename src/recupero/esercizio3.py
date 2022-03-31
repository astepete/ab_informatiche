#questa funzione permette di calcolare lo spazio percorso nel caso di moto rettilineo uniforme, richiedendo in ingresso il valore della velocità
def rett_unif(int_temp,pos_iniz):
  v=float(input("Inserisci la velocità:"))
  s=v*int_temp+pos_iniz
  return(s)


#questa funzione permette di calcolare lo spazio percorso nel caso di moto uniformemente accelerato, richiedendo in input il valore della velocità iniziale e dell'accelerazione
def unif_acc(int_temp,pos_iniz):
  v0=float(input("Inserisci la velocità iniziale:"))
  a=float(input("Inserisci l'accelerazione:"))
  s=0.5*a*int_temp**2+v0*int_temp+s0
  return(s)

#chiediamo all'utilizzatore di inserire l'intervallo temporale in cui si svolge il moto
Delta_t = float(input("Inserisci l'intervallo temporale: "))
#chiediamo all'utilizzatore di inserire il valore della posizione iniziale
s0=float(input("Inserisci la posizione iniziale:"))
#variabile che permette di scegliere quale funzione utilizzare
a=int(input("Seleziona 0 per moto rettilineo uniforme o 1 per moto uniformemente accelerato:"))


#if per richiamare la funzione selezionata al passo precedente
if (a==0):
  print(rett_unif(Delta_t,s0))
else:
  print(unif_acc(Delta_t,s0))
