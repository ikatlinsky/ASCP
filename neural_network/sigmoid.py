import numpy as np

__author__ = 'ikatlinsky'


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def dsigmoid(x):
    return sigmoid(x) * (1.0 - sigmoid(x))