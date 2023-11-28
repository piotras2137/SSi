import pandas as pd
from matplotlib import pyplot as plt

class  Probki:
    def __init__(self, sciezka="iris.txt", sciezkatypy="iris-type.txt"):
        self.sciezka = sciezka
        self.sciezkatypy = sciezkatypy
        self.typy = None
        self.klasy = None
        self.dane = None
    
    
    def zamien_klasy(self, kolumna, dane):
        class_mapping = {
            1: self.klasy.split(',')[0],
            2: self.klasy.split(',')[1],
            3: self.klasy.split(',')[2]
        }
        dane[kolumna] = dane[kolumna].map(class_mapping)


    def wczytaj(self):
        try:
            typy = []
            with open(self.sciezkatypy, "r") as plik_atrybuty:
                lines = plik_atrybuty.readlines()
                for line in lines:
                    line = line.strip("\n")
                    x = line.split()
                    if x[-1] == "n":
                        typy.append(x[0])
                    if x[-1] == "s":
                        typy.append(x[0])      
                        start = x[0].find("(")
                        koniec =  x[0].find(")")
                        self.klasy = x[0][start:koniec]
                        self.klasy = ",".join(val.split('=')[1] for val in self.klasy.split(','))
            self.typy = typy
        except:
            print("nie mozna wczytac pliku z typami ", self.typy )

        try: 
            self.dane = pd.read_csv(self.sciezka, delimiter='\t', header=None, names=self.typy)
            self.zamien_klasy(self.typy[-1], self.dane)
        except:
            pass

    def wykresy(self):
        if self.dane is None:
            raise ValueError("Brak danych. Wczytaj najpierw dane.")

        # Extract the columns
        kolumna_1 = self.dane[self.typy[0]]
        kolumna_2 = self.dane[self.typy[1]]
        kolumna_3 = self.dane[self.typy[2]]
        kolumna_4 = self.dane[self.typy[3]]

        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        # pierwszy wykres
        axs[0, 0].scatter(kolumna_3, kolumna_4, color='blue', marker='v')
        axs[0, 0].set_title(f'x = {self.typy[2]}, y = {self.typy[3]}')

        # drugi wykres
        axs[0, 1].scatter(kolumna_2, kolumna_4, color='green', marker='o')
        axs[0, 1].set_title(f'x = {self.typy[1]}, y = {self.typy[3]}')

        # trzeci wykres
        axs[1, 0].scatter(kolumna_1, kolumna_4, color='yellow', marker='s')
        axs[1, 0].set_title(f'x = {self.typy[0]}, y = {self.typy[3]}')

        # czwarty wykres
        axs[1, 1].scatter(kolumna_2, kolumna_3, color='red', marker='x')
        axs[1, 1].set_title(f'x = {self.typy[1]}, y = {self.typy[2]}')

        plt.show()


x = Probki()

x.wczytaj()
print(x.dane)
x.wykresy()