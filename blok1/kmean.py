import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
cmap = ['red', 'green', 'black', 'blue', 'pink','magenta','yellow']

def k_mean(samples, sample_names, m, iters):
    df_names = pd.read_csv(sample_names, sep="\t", header=None)
    df = pd.read_csv(samples, delim_whitespace=True, header=None, names=df_names[0])

    df_array = df.values  # Konwersja DataFrame do NumPy array

    # Inicjalizacja centrów
    centers = df.sample(m).values

    for _ in range(iters):
        # Przypisanie próbek do najbliższego centrum
        distances = np.sqrt(((df_array - centers[:, np.newaxis])**2).sum(axis=2))
        closest = np.argmin(distances, axis=0)

        # Rysowanie punktów
        for j in range(m):
            points = df_array[closest == j]
            if len(points) > 0:
                plt.scatter(*points.T, marker='s', facecolors=cmap[j], edgecolors=cmap[j])
                centers[j] = points.mean(axis=0)

        # Rysowanie centrów
        plt.scatter(*centers.T, marker='o', s=120, color=cmap[:m])
        plt.show()


k_mean("spirala.txt", "spirala-type.txt", 4, 5)

