import cmath
from math import sqrt
from numpy import random
from random import randint
from statistics import mean
import matplotlib.pyplot as plt
import seaborn as sns


def gray(a, b):
    return complex(2 * a - 1, 2 * b - 1) / sqrt(2)


def ml(x):
    if x.real >= 0:
        if x.imag >= 0:
            return [1, 1]
        else:
            return [1, 0]
    else:
        if x.imag >= 0:
            return [0, 1]
        else:
            return [0, 0]


sigma_arr = [sqrt(10), 3, 2, 1, 0.5, 0.25, 0.1, sqrt(0.1)]
mean_arr = []
for sigma in sigma_arr:
    P_e = []
    for h_itr in range(0, 1000):
        h = complex(random.normal(0, 1), random.normal(0, 1)) / sqrt(2)
        err = 0
        for itr in range(0, 500):
            n = complex(random.normal(0, sigma), random.normal(0, sigma)) / sqrt(2)
            x1 = randint(0, 1)
            x2 = randint(0, 1)
            modulated = gray(x1, x2)
            received_signal = h * modulated + n
            demodulated = ml(received_signal / h)
            if demodulated[0] != x1:
                err += 1
            if demodulated[1] != x2:
                err += 1
        P_e.append(err / 1000)

    mean_arr.append(mean(P_e))

plt.scatter(sigma_arr, mean_arr)
plt.show()
