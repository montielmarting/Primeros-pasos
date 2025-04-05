
    # solicitamos el valor de presion del sensor
Presion = int(input("Ingresar Valor de Presion "))

    # Compara la presión, si es igual a 15 da la alarma, si es mas alta da Alarma Urgente
if Presion == 15:
    print ("Alarma: La presion está en 15")
elif Presion > 15:
    print("Alarma Urgente: La presión supera 15")
else: print("Presión OK")