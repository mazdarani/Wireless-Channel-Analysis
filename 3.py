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
        for itr in range(0, 250):
            n = complex(random.normal(0, sigma), random.normal(0, sigma)) / sqrt(2)
            x1 = randint(0, 1)
            x2 = randint(0, 1)
            x3 = randint(0, 1)
            x4 = randint(0, 1)
            p1 = (x1 + x2 + x3) % 2
            p2 = (x1 + x2 + x4) % 2
            p3 = (x1 + x3 + x4) % 2
            modulated = [gray(x1, x2), gray(x3, x4), gray(p1, p2), gray(p3, 0)]
            received_signal = [h * modulated[i] + n for i in range(0, 4)]
            demodulated = [ml(received_signal[j] / h) for j in range(0, 4)]

            x1_ = demodulated[0][0]
            x2_ = demodulated[0][1]
            x3_ = demodulated[1][0]
            x4_ = demodulated[1][1]
            p1 = demodulated[2][0]
            p2 = demodulated[2][1]
            p3 = demodulated[3][0]
            p1_ = (x1_ + x2_ + x3_) % 2
            p2_ = (x1_ + x2_ + x4_) % 2
            p3_ = (x1_ + x3_ + x4_) % 2

            if p1 != p1_:
                if p2 != p2_:
                    if p3 != p3_:
                        x1_ = 1 - x1_
                    else:
                        x2_ = 1 - x2_
                elif p3 != p3_:
                    x3_ = 1 - x3_
            elif p2 != p2_ and p3 != p3_:
                x4_ = 1 - x4_

            if x1_ != x1:
                err += 1
            if x2_ != x2:
                err += 1
            if x3_ != x3:
                err += 1
            if x4_ != x4:
                err += 1
        P_e.append(err / 1000)

    mean_arr.append(mean(P_e))

plt.scatter(sigma_arr, mean_arr)
plt.show()
