personas = []
categorias = {"bajo": 0, "medio": 0, "alto": 0}

for i in range(1, 6):
    name = input("Ingresa el nombre: ")
    dias_asistidos = int(input("Cuantos dias asististe esta semana?: "))
    minutos_promedio = float(input("Cuantos minutos por medio entrenas por dia?: "))
    personas.append(
        {
            "nombre": name,
            "dias_asistidos": dias_asistidos,
            "minutos_promedio": minutos_promedio,
        }
    )

for persona in personas:
    dias = persona["dias_asistidos"]
    if dias < 3:
        categorias["bajo"] += 1
    elif 3 <= dias <= 4:
        categorias["medio"] += 1
    elif dias > 5:
        categorias["alto"] += 1

print(f"{'\n'.join(f'{c} compromiso -> {categorias[c]}'for c in categorias)}")
