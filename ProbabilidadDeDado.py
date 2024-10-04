#Simula la probabilidad 10 000 tiradas de dados en un caso de D&D donde se da un dado a vencer.
#Nota: la probabilidad individual de este caso se evalua con 21-X/20, donde X es el valor a vencer.
import random
import os

Probabilidad=0
Arreglo=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#Arreglo de 20 valores que es donde se guardará la información
Dificultad=int(input("Introduce la dificultad del dado a evaluar, valores entre 1 y 20: "))#Se pide al usuario un numero a evaluar entre 1 y 20
while (Dificultad>20) or (Dificultad<1):#Si el usuario introduce un valor que no pertenezca al rango 1 a 20...
    Dificultad=int(input("La dificultad tiene que ser un valor de entre 1 y 20, introduzca la dificultad de nuevo: "))#Se le pide al usuario otro nuevo numero
print("El numero a vencer es: ", Dificultad)
i=0
while i<10000:#10 000 simulaciones
    numero=0
    i+=1
    Dado=random.randint(1,20)#Se asigna un valor de entre 1 y 20
    if Dado>=Dificultad:#Si el numero obtenido supera la dificultad
        numero+=1
        Arreglo[Dado-1]=Arreglo[Dado-1]+numero#Se le suma 1 a la posicion que tenga Dado-1 (porque los arreglos empiezan en 0)
i=Dificultad
while i <= 20:
    Arreglo[i-1]=Arreglo[i-1]/100#Los resultados se dividen entre 100 para obtener el %
    Probabilidad=Arreglo[i-1]+Probabilidad
    i+=1
print("La probabilidad de ganar esta tirada de dados es del ",format(Probabilidad,".2f"),"%, y la probabilidad individual de cada dado es:")#Se imprime el resultado general, format(x, .nf) se usa para delimitar los decimales.
i=Dificultad
while i <= 20:
    print(i,":", Arreglo[i-1],"%")#Se imprime la probabilidad individual de cada dado.
    i+=1
os.system('pause')
