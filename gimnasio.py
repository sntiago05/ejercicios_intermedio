edad = int(input("Ingresa la edad del cliente: "))

if edad < 13:
    print("No puede ingresar")
elif 13 <= edad <= 17:
    print("Clase juvenil")
elif 18 <= edad <= 59:
    print("Clase general")
else:
    print("Clase senior")
