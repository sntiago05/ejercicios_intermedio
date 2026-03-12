asistencia = int(input("ingresa tu asistencia de este mes"))
if asistencia < 5:
    print("Asistencia baja")
elif 5 <= asistencia <= 8:
    print("Asistencia media")
elif asistencia >= 9:
    print("Asistencia alta")
