import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def seno(x):
    sum = 0
    for n in range(10):
        coef = (-1)**n
        num = x**(2*n + 1)
        denom = factorial(2*n + 1)
        sum += ( coef ) * ( (num)/(denom) )
    return sum

def coseno(x):
    sum = 0
    for n in range(10):
        coef = (-1)**n
        num = x**(2*n)
        denom = factorial(2*n)
        sum += ( coef ) * ( (num)/(denom) )
    return sum

def tangente(x):
    return seno(x) / coseno(x)

def cotangente(x):
    return 1 / tangente(x)

def secante(x):
    return 1 / coseno(x)

def cosecante(x):
    return 1 / seno(x)

while True:
    print("Seleccione una opción:")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Cotangente")
    print("5. Secante")
    print("6. Cosecante")
    print("7. Salir")
    
    opcion = int(input())
    
    if opcion == 7:
        break
    
    valor = float(input("Ingrese el valor: "))
    
    if opcion == 1:
        print(f"sen({valor}) = {seno(valor)}")
    elif opcion == 2:
        print(f"cos({valor}) = {coseno(valor)}")
    elif opcion == 3:
        print(f"tan({valor}) = {tangente(valor)}")
    elif opcion == 4:
        print(f"cot({valor}) = {cotangente(valor)}")
    elif opcion == 5:
        print(f"sec({valor}) = {secante(valor)}")
    elif opcion == 6:
        print(f"csc({valor}) = {cosecante(valor)}")
1