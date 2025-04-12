import numpy as np

# Generar arreglo aleatorio de enteros entre 0 y 100
generator = np.random.default_rng(1010)
scores = np.round(generator.integers(low=0, high=101, size=10))

print("Original:", scores)

# Reemplazar los tres primeros < 60
indices = np.where(scores < 60)[0][:3]
scores[indices] = 0

print("Modificado:", scores)
