import os#Libreria utilizada para la pausa
def primeCheck(isPrime):#Funcion para evaluar si un numero es primo de forma iterativa
    counter=0
    evaluator=0
    primeCounter=0
    while counter<=isPrime:#Mientras que el contador sea menor o igual al isPrime
        counter+=1#Contador+1
        evaluator=(isPrime%counter)#Se le asigna el residuo de isPrime
        if evaluator==0:#Si el residuo es 0
            primeCounter+=1#Entonces el numero es divisble por el valor actual de Counter
        else:#Sino
            primeCounter=primeCounter#Se conserva el valor.
    if primeCounter>2:#Si encontró más de dos divisores
        return 0#Falso
    else:
        return 1#Verdadero

def primeNumber(prime):#Funcion para encontrar todos los divisores de un numero
    primedivisors=[]#Creacion de arreglo vacio
    primeEvaluator=0
    counter=0
    while counter<=prime:#Mientras que el contador sea menor que el numero entrante
        counter+=1#Contador +1
        primeEvaluator=(prime%counter)#Se evalua el residuo del numero entrante (prime)
        if primeEvaluator==0:#Si dio 0 (es decir, es divisible)
            primedivisors.append(counter)#Se le añade al arreglo       
    return primedivisors#Al final regresa el arreglo al programa principal.


number=int(input("Ingresa un numero a evaluar: "))#Pedir al usuario un numero a evaluar
if number<=0:#Si el usuario ingresa un numero negativo
    number=abs(number)#Se convierte en positivo (su valor absoluto)
if primeCheck(number)==0:#Si la funcion retorna 0
    print("El numero",number,"no es primo y sus divisores son: ",primeNumber(number))#El numero no era primo, y se muestran sus divisores
else:
    print("El numero",number,"es primo y sus divisores son: ",primeNumber(number))#Si la funcion retorna 1, el numero era primo y se muestran sus dos unicos divisores
os.system('pause')#Pausa al sistema.
