# Definir las condiciones iniciales
S = bool(int(input("¿Semáforo parpadeando? (1 para Sí, 0 para No): ")))
T = bool(int(input("¿Menos de 5 segundos que parpadea? (1 para Sí, 0 para No): ")))
A = bool(int(input("¿Ancho de la calle mas de 10 metros? (1 para Sí, 0 para No): ")))
P = bool(int(input("¿Estás cargando cosas pesadas que te hagan caminar lento? (1 para Sí, 0 para No): ")))
C = bool(int(input("¿Hay coches que vienen rápido? (1 para Sí, 0 para No): ")))
L = bool(int(input("¿Semáforo rojo o amarillo? (1 para Sí, 0 para No): ")))

# Calcular si debes caminar o no en una sola línea
W = S and T and L and not (A or P or C)

# Mostrar el resultado
print("Puedes cruzar la calle." if W else "No cruces la calle.")