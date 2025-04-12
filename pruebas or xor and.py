
S = True # semaforo parpadeando
T = True  # hace menos de 5 segundos
A = True  # ancho calle menor a 10 metros
P = False  # Cargando cosas pesadas que me hagan caminar lento
C = False  # Coches que vienen rapido
L = True  # semaforo rojo o amarillo
W = bool  # Caminar o cruzar la calle

W = S and T and L and A and not (P or C)
if W == True:
    print("Puedes cruzar la calle")
    
else: print("No cruces la calle")

#fin