#definisco due variabili intere
int1=5
int2=7
#definisco due variabili di tipo float
float1=3.14
float2=2.71
#definisco due variabili complesse
z1=complex(2,3)
z2=complex(7,9)
#definisco due variabili booleane
a=True
b=False
#definisco tre variabili di tipo stringa
str1="pippo"
str2="pluto"
str3="150.37"
#somma di interi
int3=int1+int2
print(int3)
#rapporto tra float
float3=float1/float2
print(float3)
#prodotto di complessi
z3=z1*z2
print(z3)
#and tra variabili booleane
c=a and b
print(c)
#concatenazione di stringhe
str4=str1+str2
print(str4)
#type casting implicito
#promuove la variabile int1 ad un float, così da poterla sommare a float2
c=int1+float2
#promuove la variabile float1 ad un complesso, così da poterla sommare a z2
d=float1*z2
print(c)
print(d)
#type casting esplicito
#converte la stringa str3 in un float, così da poterlo sommare con float2
e=float2+float(str3)
#creiamo un complesso a partire da due interi, così da sommarlo al complesso
z3=complex(int1 ,int2)+z2
