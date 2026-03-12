horas = int(input("Cuantas horas estuvo en el parqueadero?: "))
PRIMERA_HORA = 5000
HORA_ADICIONAL = 3000

if horas > 1:
    total = PRIMERA_HORA + (horas - 1) * HORA_ADICIONAL
else:
    total = PRIMERA_HORA

print(f"El total a pagar es de {total}")
