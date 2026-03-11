BEBIDAS = {"cafe": 4000, "te": 3500, "jugo": 5000}
print(f"cafe -> {BEBIDAS["cafe"]}\nte -> {BEBIDAS['te']}\njugo ->{BEBIDAS['jugo']}")
bebida = (
    input(
        "que bebida quieres?: "
    )
    .lower()
    .strip()
)
cantidad = int(input("Cuantos deseas comprar?: "))
print(f"El total a pagar es de: {cantidad*BEBIDAS[bebida]}")
