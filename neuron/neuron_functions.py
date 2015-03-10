# coding=utf-8
import math
from neuron import Neuron

__author__ = 'ikatlinsky'


def neuron(activation, *args):
    return activation(*args)


def scalar_prod(x, w):
    return sum(p * q for p, q in zip(x, w))


def linear_activation(n):
    """
    Линейная функция активации нейрона:
            _
           |   u <= 0 -> 0
    f(u)= <|   u >= 1 -> 1
           |_  u

    :param n: neuron.Neuron - нейрон
    :return: результат действия функции активации
    """
    u = __prepare_for_activation(n)

    if u <= 0:
        return 0
    elif u >= 1:
        return 1
    else:
        return u


def step_activation(n):
    """
    Пороговая функция активации нейрона:
                _
               |   u >= t -> 1
    f(u, t) = <|
               |_  0

    :param n: neuron.Neuron - нейрон
    :return: результат действия функции активации
    """
    u = __prepare_for_activation(n)
    t = - n.first_product()

    if u >= t:
        return 1
    else:
        return 0


def sigma_activation(n):
    """
    Сигмоидальная функция активации нейрона:

                   1
    f(u,t) = ----------------
             (1 + exp(t * u))

    :param n: neuron.Neuron - нейрон
    :return: результат действия функции активации
    """
    u = __prepare_for_activation(n)

    return 1 / (1 + math.exp(-0.2 * u))


def __prepare_for_activation(n):
    if not isinstance(n, Neuron):
        raise TypeError("Входной параметр функции активации должен иметь тип [%s]" % Neuron.__name__)
    u = n.scalar_product()
    return u