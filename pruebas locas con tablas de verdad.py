import pandas as pd
import numpy as np

# Crear un rango de números para las variables A y B
A = range(1, 5)  # Valores de 1 a 4
B = range(5, 9)  # Valores de 5 a 8

# Crear un DataFrame con las combinaciones de A y B
tabla_valores = pd.DataFrame({
    'A': A,
    'B': B,
    'A + B': [a + b for a, b in zip(A, B)],  # Suma de A y B
    'A * B': [a * b for a, b in zip(A, B)],  # Producto de A y B
    'A > B': [a > b for a, b in zip(A, B)]   # Comparación A > B
})

# Mostrar la tabla de valores
print(tabla_valores)