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


def print_scatter(sigma):
    input_signals = []
    constellation = []
    channel_passed = []
    final_signals = []

    h = complex(random.normal(0, 1), random.normal(0, 1)) / sqrt(2)
    for itr in range(0, 1000):
        n = complex(random.normal(0, sigma), random.normal(0, sigma)) / sqrt(2)
        x1 = randint(0, 1)
        x2 = randint(0, 1)
        input_signals.append(x1)
        input_signals.append(x2)
        modulated = gray(x1, x2)
        constellation.append(modulated)
        received_signal = h * modulated + n
        channel_passed.append(received_signal)
        demodulated = ml(received_signal / h)
        final_signals.append(demodulated[0])
        final_signals.append(demodulated[1])

    plt.scatter(constellation, channel_passed)
    plt.show()


print_scatter(sqrt(10))
print_scatter(sqrt(1))
print_scatter(sqrt(0.1))
