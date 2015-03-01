# coding=utf-8

import math
import random as rnd

__author__ = 'ikatlinsky'


def linear_activation(u):
    """
    Линейная функция активации нейрона:
            _
           |   u <= 0 -> 0
    f(u)= <|   u >= 1 -> 1
           |_  u

    :param n: neuron.Neuron - нейрон
    :return: результат действия функции активации
    """
    if u <= 0:
        return 0
    elif u >= 1:
        return 1
    else:
        return u


def sigma_activation(u):
    """
    Сигмоидальная функция активации нейрона:

                   1
    f(u,t) = ----------------
             (1 + exp(t * u))

    :param n: neuron.Neuron - нейрон
    :return: результат действия функции активации
    """
    return 1 / (1 + math.exp(-0.2 * u))


def generate_random_list(size):
    return [rnd.random() for _ in range(size)]
