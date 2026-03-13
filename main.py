import os

ejercicios = {}

for archivo in os.listdir("soluciones"):
    if archivo.endswith(".py") and archivo != "main.py":
        numero = archivo.split("_")[0]
        if numero.isdigit():
            ejercicios[int(numero)] = archivo

eleccion = None

while eleccion != "0":
    print("\n=== MIS EJERCICIOS ===")
    for numero, archivo in sorted(ejercicios.items()):
        nombre = archivo.replace(".py", "").split("_", 1)[1].replace("_", " ")
        print(f"{numero} - {nombre}")
    print("0 - Salir")

    eleccion = input("\nEscribe el número del ejercicio: ")

    if not eleccion.isdigit():
        print("Eso no es un número")
    elif int(eleccion) == 0:
        print("¡Hasta luego!")
    elif int(eleccion) not in ejercicios:
        print("Ese número no existe")
    else:
        archivo = ejercicios[int(eleccion)]
        print(f"\nEjecutando {archivo}...\n")
        os.system(f"python3 soluciones/{archivo}")
