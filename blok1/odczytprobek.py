# odczyt próbek
def str_to_int_float_str(str):
    try:
        if float(str).is_integer() == True:
            return int(str)
        else:
            return float(str)
    except:
        return str



def wczytaj_baze_probek_z_tekstem(nazwa_pliku: str, nazwa_pliku_z_opisem_atr: str):
    probki = []
    czy_atr_symb = []
    nazwy_atr = []
   
    try:
        with open(nazwa_pliku_z_opisem_atr) as plik_atrybuty:
            lines = plik_atrybuty.readlines()
            for line in lines:
                line = line.strip("\n")
                x = line.split()
                nazwy_atr.append(x[0])
                if x[1]!="s":
                    czy_atr_symb.append(False)
                else:
                    czy_atr_symb.append(True)
    except:
        print("nie mozna wczytac pliku z opisem atrybutow: ", nazwa_pliku_z_opisem_atr)
        exit(1)

    try:
        with open(nazwa_pliku, 'r') as plik:
            lines = plik.readlines()
            print(lines)
            for line in lines:
                line = line.strip("\n")
                x = line.split()
                x = [str_to_int_float_str(i) for i in x]
                probki.append(x)
    except:
        print("nie mozna wczytac pliku z probkami: ", nazwa_pliku)
        exit(1)

    return probki, czy_atr_symb, nazwy_atr


probki, czy_atr_symb, nazwy_atr = wczytaj_baze_probek_z_tekstem("iris.txt", "iris-type.txt")


print(probki)
print(czy_atr_symb)
print(nazwy_atr)

probki, czy_atr_symb, nazwy_atr = wczytaj_baze_probek_z_tekstem("iris.txt", "iris-type.txt")

print(probki)
print(czy_atr_symb)
print(nazwy_atr)


