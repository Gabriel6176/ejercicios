##programa para calcular vacaciones##

Nombre_empleado = input("Diga el nombre del empleado: ")
Clave_departamento = int(input("Diga la clave del departamento (1-2-3): "))
Antigüedad_empleado = int(input("Cuantos años de antiguedad tiene el empleado?: "))

if Clave_departamento == 1:
    if Antigüedad_empleado > 1 and Antigüedad_empleado < 2:
        print ("El empleado ", Nombre_empleado, " tiene derecho a 6 dias de vacaciones")
    elif Antigüedad_empleado >= 2 and Antigüedad_empleado < 7:
        print ("El empleado ", Nombre_empleado, " tiene derecho a 14 dias de vacaciones")
    elif Antigüedad_empleado >= 7:
        print ("El empleado ", Nombre_empleado, " tiene derecho a 20 dias de vacaciones")
    else:
        print("El empleado no tiene derecho a dias de vacaciones")

elif Clave_departamento == 2:
    if Antigüedad_empleado > 1 and Antigüedad_empleado < 2:
        print ("El empleado ", Nombre_empleado, " tiene derecho a 7 dias de vacaciones")
    elif Antigüedad_empleado >= 2 and Antigüedad_empleado < 7:
        print ("El empleado ", Nombre_empleado, " tiene derecho a 15 dias de vacaciones")
    elif Antigüedad_empleado >= 7:
        print ("El empleado ", Nombre_empleado, " tiene derecho a 22 dias de vacaciones")
    else:
        print("El empleado no tiene derecho a dias de vacaciones")

elif Clave_departamento == 3:
    if Antigüedad_empleado > 1 and Antigüedad_empleado < 2:
        print ("El empleado ", Nombre_empleado, " tiene derecho a 10 dias de vacaciones")
    elif Antigüedad_empleado >=2 and Antigüedad_empleado < 7:
        print ("El empleado ", Nombre_empleado, " tiene derecho a 20 dias de vacaciones")
    elif Antigüedad_empleado >=7:
        print ("El empleado ", Nombre_empleado, " tiene derecho a 30 dias de vacaciones")
    else:
        print("El empleado ", Nombre_empleado, " no tiene derecho a dias de vacaciones")

else:
    print("El numero de departamento es incorrecto, intente nuevamente")
