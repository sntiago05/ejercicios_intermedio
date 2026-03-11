edad = int(input("ingresa tu edad: "))
if edad < 12:
    precio = 8000
elif 12 <= edad <= 59:
    precio = 12000
else:
    precio = 9000

print(f"El precio a pagar es de: ${precio}")
