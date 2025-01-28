import numpy as np
import matplotlib.pyplot as plt

n_values = [500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]

for n in n_values:

    s = np.random.randint(1, 7, n) + np.random.randint(1, 7, n)
    h, h2 = np.histogram(s, bins=range(2, 14))
    plt.bar(h2[:-1], h / n)
    plt.title(f"Dice Sum Distribution (n = {n})")
    plt.xlabel("Sum")
    plt.ylabel("Probability")
    plt.show()


