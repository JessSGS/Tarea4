import numpy as np

# Crear arreglo 10x10x10 lleno de ceros
array = np.zeros((10, 10, 10), dtype=int)

# Condiciones: i impar, j par, k primo
primes = [2, 3, 5, 7]

for i in range(10):
    for j in range(10):
        for k in primes:
            if i % 2 == 1 and j % 2 == 0:
                array[i, j, k] = 1

print("Arreglo modificado en posiciones específicas.")
