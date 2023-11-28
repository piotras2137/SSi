import numpy as np
import matplotlib.pyplot as plt

patterns = [
    np.array([
        [0, 0, 0, 1],  
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0, 1, 1, 1],  
        [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]),
    np.array([
        [1, 1, 1, 0],  
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 0]
    ])
]

test_patterns = [
    np.array([
        [0, 0, 0, 0],  
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 1, 1, 1],  
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1]
    ]),
    np.array([
        [1, 1, 1, 1],  
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 1]
    ])
]


def oblicz_minimalna_odleglosc(punkt, macierz):
    odleglosci = [np.sqrt((pax - pbx) ** 2 + (pay - pby) ** 2)
                  for (pay, pax), val_pa in np.ndenumerate(punkt)
                  for (pby, pbx), val_pb in np.ndenumerate(macierz)
                  if val_pa == 1 and val_pb == 1]
    return min(odleglosci, default=np.inf)

def miara_niepodobienstwa(BA, BB):
    return sum(oblicz_minimalna_odleglosc(np.array([(pay, pax)]), BB) for (pay, pax), val_ba in np.ndenumerate(BA) if val_ba == 1)

def miara_podobienstwa_obustronnego(BA, BB):
    return -(miara_niepodobienstwa(BA, BB) + miara_niepodobienstwa(BB,BA))


for test in test_patterns:
    miary  = []
    for pattern in patterns:
        miary.append([miara_podobienstwa_obustronnego(test,pattern)])
    fig, ax = plt.subplots(1,2)
    ax[0].matshow(test, cmap='gray_r')
    ax[0].set_title("Bitmapa testowa")
    
    ax[1].matshow(patterns[miary.index(max(miary))], cmap='gray_r')
    ax[1].set_title("Bitmapa wzorcowa")
    plt.show()
    