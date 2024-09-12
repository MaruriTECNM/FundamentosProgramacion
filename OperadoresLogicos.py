numero=int(input("Ingresa un numero: "))
Evaluadores=[1,2,4,8,16,32,64,128,256,512,1024]
contador=0
while contador<10:
    print(((numero**contador)>=Evaluadores[contador]) and ((numero**contador)>=Evaluadores[contador]))
    contador+=1