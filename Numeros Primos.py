import os
def primeCheck(isPrime):
    counter=0
    evaluator=0
    primeCounter=0
    while counter<=isPrime:
        counter+=1
        evaluator=(isPrime%counter)
        if evaluator==0:
            primeCounter+=1
        else:
            primeCounter=primeCounter
    if primeCounter>2:
        return 0
    else:
        return 1

def primeNumber(prime):
    primedivisors=[]
    primeEvaluator=0
    counter=0
    while counter<=prime:
        counter+=1
        primeEvaluator=(prime%counter)
        if primeEvaluator==0:
            primedivisors.append(counter)       
    return primedivisors

def main():
    number=int(input("Ingresa un numero a evaluar: "))
    if number<=0:
        number=abs(number)
    if primeCheck(number)==0:
        print("El numero",number,"no es primo y sus divisores son: ",primeNumber(number))
    else:
        print("El numero",number,"es primo y sus divisores son: ",primeNumber(number))
    os.system('pause')