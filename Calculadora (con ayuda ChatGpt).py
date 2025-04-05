# título de la app
print("\n Programa Calculadora Básica \n")

# funciones de las operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Error: División por cero"

# ingreso del primer número con validación
while True:
    try:
        Numero1 = float(input("Ingrese un número: \n"))
        break
    except ValueError:
        print("¡Error! Por favor ingrese un número válido.")

# selección de operación con validación
while True:
    Operacion = input("Elija una operación ( + - * / ) \n")
    if Operacion in ['+', '-', '*', '/']:
        break
    else:
        print("¡Error! Elija una operación válida.")

# ingreso del segundo número con validación
while True:
    try:
        Numero2 = float(input("Ingrese el segundo número: \n"))
        break
    except ValueError:
        print("¡Error! Por favor ingrese un número válido.")

# realización de la operación
if Operacion == "+":
    print(f"La suma entre {Numero1} y {Numero2} es igual a: {suma(Numero1, Numero2)}")
elif Operacion == "-":
    print(f"La resta entre {Numero1} y {Numero2} es igual a: {resta(Numero1, Numero2)}")
elif Operacion == "*":
    print(f"La multiplicación entre {Numero1} y {Numero2} es igual a: {multiplicacion(Numero1, Numero2)}")
elif Operacion == "/":
    print(f"La división entre {Numero1} y {Numero2} es igual a: {division(Numero1, Numero2)}")
