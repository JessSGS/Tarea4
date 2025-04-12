import numpy as np

locs = np.array([
    [0, 0, 0],
    [1, 1, 2],
    [0, 0, 0],
    [2, 1, 3],
    [5, 5, 4],
    [5, 0, 0],
    [5, 0, 0],
    [0, 0, 0],
    [2, 1, 3],
    [1, 3, 1]
])
generator = np.random.default_rng(1010)
weights = generator.normal(size=10)

# Diccionario con key = posición (tuple), value = (índice del pez, peso)
pos_map = {}
for i, (loc, w) in enumerate(zip(locs, weights)):
    key = tuple(loc)
    if key not in pos_map or w > weights[pos_map[key]]:
        pos_map[key] = i

# Índices de peces que sobreviven
survivors = sorted(pos_map.values())
print("Sobreviven:", survivors)
