# coding=utf-8
import numpy as np
import random as rnd
import neuron_utils as nu

__author__ = 'ikatlinsky'


class Neuron():
    """
    Класс представляет собой обхект - нейрон. параметрами класса являются функция активации и список весов
    """
    weights = []
    act_func = lambda x: x

    def __init__(self, size, act_func):
        """
        Создает объект - нейрон.ю исходя из входных параметров: длина списка весов, функция активации.
        Изначальные значения весов задаются произвольно.
        :param size: размер списка весов, должен быть больше 0
        :param act_func: функция активации нейрона
        :exception ValueError
        :return: новый объект нейрон
        """
        if size < 1:
            raise ValueError("Length of neuron weights should be greater than 0")

        self.weights = [rnd.random() for _ in range(size)]
        self.act_func = act_func

    def get_value(self, x):
        """
        Возвращает результат действия функции активации на нейрон при заданных значениях :param x
        :param x: значения нейрона, при кторых необходимо получить результатю Длина списка знаяений
        должна совпадать с длиной списка весов.
        :exception ValueError
        :return: результат действия функции активации
        """
        if len(x) != len(self.weights):
            raise ValueError("Length of neuron values and weights should be equal.", x, self.weights)

        scalar = np.dot(x, self.weights)
        return self.act_func(scalar)

    def set_weight(self, weights):
        """
        Задает новые значения для весов нейрона.
        :param weights: список весов, длина списка должна совпадать с текущей длиной весов
        :exception ValueError
        :return: новые значния весов
        """
        if len(weights) != len(self.weights):
            raise ValueError("Length of neuron weights should be equal.", self.weights)

        self.weights = weights
        return self.weights

    def add_to_weights(self, weights):
        """
        Добавляет к текущим значениям весов поправку
        :param weights: список весов поправки, длина списка должна совпадать с текущкй длиной весов
        :exception ValueError
        :return: новые значения весов
        """
        if len(weights) != len(self.weights):
            raise ValueError("Length of neuron weights should be equal.", self.weights)

        self.weights = np.add(self.weights, weights)
        return self.weights


def test():
    """
    Тестирования процесса создания нейрона, вычисления результата функции активации, замены весов и изменения весов
    :return:
    """
    n = Neuron(5, nu.linear_activation)
    print "Веса нейрона: %s" % n.weights
    print "\n"

    x = nu.generate_random_list(5)
    print "Входной вектор нейрона: %s" % x
    print "\n"

    print "Применяем функцию активации: %s" % n.get_value(x)
    print "\n"

    w = nu.generate_random_list(5)
    print "Заменяем веса: %s" % n.set_weight(w)
    print "\n"

    print "Изменяем веса: %s" % n.add_to_weights(x)
    print "\n"

test()

