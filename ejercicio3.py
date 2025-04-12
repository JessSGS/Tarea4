import numpy as np

# Generar puntajes aleatorios entre 0 y 100 para 10 personas
generator = np.random.default_rng(1010)
love_scores = np.round(generator.uniform(low=0, high=100, size=10))

# Crear matriz de diferencias absolutas
diff_matrix = np.abs(love_scores[:, None] - love_scores[None, :])

print("Puntajes del amor:", love_scores)
print("Matriz de diferencias absolutas:\n", diff_matrix)
