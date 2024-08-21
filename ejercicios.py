"""
Realizar la carga del precio de un producto y la cantidad a llevar. 
Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)
"""
try:
    precio = int(input("Ingrese el precio del producto: "))
except:
    print("Error, debe ingresar un valor entero")
    exit()

try:
    cantidad = int(input("Ingrese la cantidad a llevar: "))
except:
    print("Error, debe ingresar un valor entero")
    exit()
    
total = precio * cantidad
print("El total a pagar es: ", total)
