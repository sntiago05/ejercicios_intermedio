servicios = ["masaje", "facial", "manicure"]
print(
    f"{'='*40} Servicios disponibles {'='*40}\n"
    + f"{'\n'.join(f"-> {i+1}. {s}" for i,s in enumerate(servicios))}"
    + f"\n{'='*80}"
)
servicio = input("escoge el servicio: ").strip().lower()
if servicio in servicios:
    print("Existe el servicio")
else:
    print("No sirve el servicio")
