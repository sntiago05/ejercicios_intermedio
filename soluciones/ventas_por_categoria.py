categorias = {"alimento": 0, "juguete": 0, "accesorio": 0}
print("\n".join(f"{i+1}. {c}" for i, c in enumerate(categorias)))
for i in range(1, 11):
    print(f"venta numero {i}")
    categoria = input("ingresa la categoria: ")
    if categoria in categorias:
        valor = int(input("ingresa el valor de la compra: "))
        categorias[categoria] += 1

print("\n".join(f"{c} -> {categorias[c]}" for c in categorias))
mas_vendida = max(categorias, key=categorias.get) # type: ignore

print(f"Categoria mas vendida -> {mas_vendida} ({categorias[mas_vendida]})")
