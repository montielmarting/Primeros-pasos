import pandas as pd
import numpy as np

# Solicitar al usuario el monto de inversión
monto_inversion = float(input("Ingrese el monto de inversión disponible: "))

# Solicitar datos manualmente para cada criptomoneda
n = int(input("¿Cuántas criptomonedas desea analizar? "))
data = []

for i in range(n):
    print(f"\nIngrese los datos para la criptomoneda {i + 1}:")
    moneda = input("Nombre de la criptomoneda: ")
    precio_min = float(input("Precio mínimo histórico: "))
    precio_max = float(input("Precio máximo histórico: "))
    precio_actual = float(input("Precio actual: "))
    data.append([moneda, precio_min, precio_max, precio_actual])

# Crear un DataFrame con los datos ingresados
df = pd.DataFrame(data, columns=['Moneda', 'Precio_Mínimo', 'Precio_Máximo', 'Precio_Actual'])

# Calcular métricas clave
df['Variabilidad'] = (df['Precio_Máximo'] - df['Precio_Mínimo']) / df['Precio_Mínimo'] * 100  # Porcentaje de variación
df['Potencial_Retorno'] = (df['Precio_Máximo'] - df['Precio_Actual']) / df['Precio_Actual'] * 100  # Retorno esperado
df['Monto_Comprable'] = monto_inversion / df['Precio_Actual']  # Cantidad de monedas que se pueden comprar
df['Recomendación'] = np.where(df['Potencial_Retorno'] > 50, 'Comprar', 'No Comprar')  # Regla simple

# Mostrar resultados
print("\nResultados del análisis:")
print(df)

# Guardar los resultados en un archivo CSV (opcional)
#df.to_csv("resultados_analisis.csv", index=False)
#print("\nLos resultados se han guardado en 'resultados_analisis.csv'.")