print(f"{'='*20} Lista de animales {'='*20}")
print("--> Perro\n---> Gato\n---> Conejo")
tipo = input("Ingresa el tipo: ").lower().strip()
if tipo == "perro":
    print("Te recomendamos concentrados especial para perros y comprarle un juguetito")
elif tipo == "gato":
    print("Te recomendamos comprar lata de comida para gatos y una bola de estambre")
elif tipo == "conejo":
    print("Te recomendamos darle zanahorias y ponerle mucha atencion")
else:
    print("Opcion no valida")
