import numpy as np
import random as rnd

__author__ = 'ikatlinsky'


def std(array):
    array = np.asanyarray(array)

    n = len(array)
    square_list = [np.power(el, 2) for el in array]
    s = np.sum(square_list)
    s = np.sqrt(s)
    a = n / s

    return [el * a for el in array]

ar = [[1, 2, 3], [4, 5, 6], [7, 8, 6], [4, 6, 8], [2, 5, 6]]
print std(ar)


def choose_svn(a, amount):
    if amount > 1:
        raise ValueError("Amount should be less than 1.")

    n = len(a)
    size = int(n * amount)

    return [[el, 1] for el in rnd.sample(a, size)]


print choose_svn(ar, 0.5)