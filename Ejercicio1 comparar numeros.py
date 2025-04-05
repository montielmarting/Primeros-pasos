    #defino 2 variables enteras y pido al usuario que las ingrese

Valor1= int(input("Ingrese un numero "))
Valor2= int(input("ingrese otro numero "))

    #uso funciones condicionantes para que desp de comparar imprima la opcion que corresponde
if Valor1 > Valor2:
    print(Valor1," es mayor")
elif Valor1 < Valor2:
    print(Valor2,"es mayor")
else: print("los numeros son iguales")
