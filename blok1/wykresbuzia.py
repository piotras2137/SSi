# wykresy

from matplotlib import pyplot as plt
import numpy as np

# wykres buzia
def zad3():

    # okreg
    theta = np.linspace(0, 2*np.pi, 25)
    r = 2
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # tworzenie wykresu
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, color="red", label='lamane')

    # oczy i nos
    points_x = [1, -1, 0]
    points_y = [1, 1, 0]
    plt.scatter(points_x, points_y, color='blue', label='punkty', marker='D')

    # usmiech
    x = np.linspace(-1, 1, 100)
    y = x**2-1
    plt.plot(x, y, color='yellow', label='sinus')


    # zakresy osi
    plt.xlim(-2, 2)
    plt.ylim(-3, 3)

    plt.legend()

    # wyswietlenie
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()


zad3()