print("Sumadora")
while True:
    a= input("Ingrese un numero (o presione ENTER para salir) \n")
    if a=="":
        print("Hasta la proxima")
        break
    a= float(a)
    b= float(input("Ingrese otro numero \n"))
    Resultado= a + b
    print(Resultado)