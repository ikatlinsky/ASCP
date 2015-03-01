# coding=utf-8
import numpy as np
import random as rnd
import neuron_utils as nu

__author__ = 'ikatlinsky'


class Neuron():
    """

    """
    weights = []
    act_func = lambda x: x

    def __init__(self, size, act_func):
        """

        :param size:
        :param act_func:
        :return:
        """
        if size < 1:
            raise ValueError("Length of neuron weights should be greater than 0")

        self.weights = [rnd.random() for _ in range(size)]
        self.act_func = act_func

    def get_value(self, x):
        """

        :param x:
        :return:
        """
        if len(x) != len(self.weights):
            raise AssertionError("Length of neuron values and weights should be equal.", x, self.weights)

        scalar = np.dot(x, self.weights)
        return self.act_func(scalar)

    def set_weight(self, weights):
        """

        :param weights:
        :return:
        """
        if len(weights) != len(self.weights):
            raise AssertionError("Length of neuron weights should be equal.", self.weights)

        self.weights = weights
        return self.weights

    def add_to_weights(self, weights):
        """

        :param weights:
        :return:
        """
        if len(weights) != len(self.weights):
            raise AssertionError("Length of neuron weights should be equal.", self.weights)

        self.weights = np.add(self.weights, weights)
        return self.weights


def test():
    """

    :return:
    """
    n = Neuron(5, nu.linear_activation)
    print "Веса нейрона: %s" % n.weights

    x = nu.generate_random_list(5)
    print "Входной вектор нейрона: %s" % x

    print "Применяем функцию активации: %s" % n.get_value(x)

    w = nu.generate_random_list(5)
    print "Заменяем веса: %s" % n.set_weight(w)

    print "Изменяем веса: %s" % n.add_to_weights(x)

test()

