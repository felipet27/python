"""
numero_1=input("Ingresa el primer numero: ")
numero_1=int(numero_1)
numero_2=input("Ingresa el segundo numero: ")
numero_2=int(numero_2)
suma=numero_1+numero_2
print("La suma de ambos numeros es: ")
print(suma)"""


try:
    numero_1=int(input("Ingrese el primero numero entero: "))
except:
    print("El numero ingresado no es un numero entero")
    exit()

try:
    numero_2=float(input("Ingrese el segundo numero flotante: "))
except:
    print("El numero ingresado no es un numero flotante")
    exit()

suma=numero_1+numero_2
print(type(numero_1),type(numero_2))
print("La suma de los numeros es: ")
print(suma)

"""
f=string
Nos sirve para concatenar numeros en salidas de texto 
"""

print(f"La suma de los numeros es:  {suma}")