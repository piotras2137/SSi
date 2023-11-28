import numpy as np
import matplotlib.pyplot as plt
import random

def get_func(x):
    return np.sin(x / 10.0) * np.sin(x / 200)

def one_plus_one(rozrzut, wsp_przyrostu, l_iteracji, zakres_zmiennosci):
    x = random.uniform(*zakres_zmiennosci)
    y = get_func(x)
    t = np.linspace(0, 100, 1000)

    plt.plot(t, get_func(t), color='blue')
    for i in range(l_iteracji):
        x_pot = np.clip(x + random.uniform(-rozrzut, rozrzut), *zakres_zmiennosci)
        y_pot = get_func(x_pot)

        if y_pot >= y:
            x, y = x_pot, y_pot
            rozrzut *= wsp_przyrostu
        else:
            rozrzut /= wsp_przyrostu

        plt.scatter(x, y, color='red', s=100)
        plt.title(f'Numer iteracji: {i}, x: {x}, y: {y}, rozrzut: {rozrzut}')
        plt.pause(0.1)
        plt.clf()
        plt.plot(t, get_func(t), color='blue')

    plt.scatter(x, y, color='red', s=100)
    plt.title("Finałowy wykres")
    plt.show()

# Przykładowe wywołanie
one_plus_one(10, 1.1, 100, (0, 100))