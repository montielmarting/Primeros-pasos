    # titulo de la app
print(" \n Programa Calculadora Básica \n")

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    return a / b
    #ingreso del primer numero
Numero1= float(input("ingrese un numero: \n"))

    # pedido de formula
Operacion= (input("elija una operacion ( + - * / ) \n"))

if Operacion== ("+"):
    Opc= 1
elif Operacion== ("-"):
    Opc= 2
elif Operacion== ("*"):
    Opc= 3
elif Operacion== ("/"):
    Opc= 4
else:
    print("Elija una formula válida")

    #ingreso del segundo numero
Numero2= float(input("ingrese segundo numero: \n"))
    #realizacion de operacion
if Opc== 1:
    print("La suma entre", Numero1, "y", Numero2,"es igual a: ", suma(Numero1,Numero2))
if Opc== 2:
    print("La resta entre", Numero1, "y", Numero2,"es igual a: ", resta(Numero1,Numero2))
if Opc== 3:
    print("La multiplicación entre", Numero1, "y", Numero2,"es igual a: ", multiplicacion(Numero1,Numero2))
if Opc== 4:
    print("La división entre", Numero1, "y", Numero2,"es igual a: ", division(Numero1,Numero2))
