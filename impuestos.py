try:
    impuestos=int(input("Ingresa tu sueldo:"))
except:
    print("Error, ingresa un número entero")
    exit

if impuestos >= 10000 :
    print("Usted debe pagar impuestos")
else:
    print("Usted no debe pagar impuestos")
    