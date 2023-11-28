import numpy as np
import matplotlib.pyplot as plt


test_patterns = [    np.array([
        [-1, 1, -1, -1, -1],
        [-1, 1, -1, -1, -1],
        [-1, 1, -1, -1, -1],
        [-1, 1, -1, -1, -1],
        [-1, 1, -1, -1, -1]
    ]),
    np.array([
        [1, 1, -1, -1, 1],
        [-1, 1, -1, 1, -1],
        [-1, 1, 1, 1, -1],
        [-1, 1, -1, 1, -1],
        [1, 1, -1, -1, 1]
    ]),
    np.array([
        [-1, -1, -1, -1, -1],
        [-1, -1, 1, -1, -1],
        [1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1],
        [-1, -1, 1, -1, -1]
    ]),
    np.array([
        [-1, 1, 1, 1, 1],
        [1, -1, 1, 1, 1],
        [1, -1, 1, 1, 1],
        [1, -1, 1, 1, 1],
        [1, -1, 1, 1, 1]
    ])]
'''
for pattern in test_patterns:
    plt.matshow(pattern, cmap="gray_r")
'''
patterns = [    np.array([
        [1, 1, -1, -1, -1],
        [-1, 1, -1, -1, -1],
        [-1, 1, -1, -1, -1],
        [-1, 1, -1, -1, -1],
        [-1, 1, -1, -1, -1]
    ]),
    np.array([
        [1, -1, -1, -1, 1],
        [-1, 1, -1, 1, -1],
        [-1, -1, 1, -1, -1],
        [-1, 1, -1, 1, -1],
        [1, -1, -1, -1, 1]
    ]),
    np.array([
        [-1, -1, 1, -1, -1],
        [-1, -1, 1, -1, -1],
        [1, 1, 1, 1, 1],
        [-1, -1, 1, -1, -1],
        [-1, -1, 1, -1, -1]
    ])
]
'''
for pattern in patterns:
    plt.matshow(pattern, cmap = "gray_r"
                '''

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size ** 2
        self.weights = np.zeros((self.size, self.size))

    def learn(self, pattern):
        pattern = np.array(pattern).flatten()
        pattern = 2 * pattern - 1  # Zamiana 0 na -1 i 1 na 1
        self.weights = np.outer(pattern, pattern) / self.size
        np.fill_diagonal(self.weights, 0)  # Zerowanie przekątnej

    def recognize(self, pattern, max_iter=10):
        pattern = np.array(pattern).flatten()
        for _ in range(max_iter):
            pattern = np.sign(np.dot(self.weights, pattern))
            pattern[pattern == 0] = -1  # Zamiana 0 na -1 w przypadku braku wyraźnego kierunku

        return pattern



network = HopfieldNetwork(len(patterns[0]))



for i in range(len(test_patterns)):
    p = patterns[i if i < len(patterns) else 0]
    t = test_patterns[i]

    network.learn(p)
    r = network.recognize(test_patterns[i])

    fig, ax = plt.subplots(1, 3)
    ax[0].matshow(p, cmap='gray_r')
    ax[0].set_title("Pattern")
    ax[1].matshow(t, cmap='gray_r')
    ax[1].set_title("Test")
    ax[2].matshow(r.reshape(5, 5), cmap='gray_r')
    ax[2].set_title("Result")

plt.show()