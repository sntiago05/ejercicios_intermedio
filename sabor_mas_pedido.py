SABORES = {"vainilla": 0, "chocolate": 0, "fresa": 0}
continuar = input("Deseas ingresar pedido? 1. si 2. no").strip()
i = 1
while continuar == "1":
    for j in range(1, 6, 1):
        print(f"Hola cliente {i} pedido numero {j}")
        option = int(input(f"Escoge un sabor 1.vainilla 2.chocolate 3.fresa"))
        sabor = ""
        match option:
            case 1:
                sabor = "vainilla"
            case 2:
                sabor = "chocolate"
            case 3:
                sabor = "fresa"
            case _:
                print("ingresa una opcion valida")
        SABORES[sabor] += 1
    i += 1
    continuar = input("Deseas ingresar otro pedido? 1.si 2.no")

for sabor in SABORES:
    print(f"sabor: {sabor} cantidad -> {SABORES[sabor]}")
