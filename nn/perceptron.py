# coding=utf-8
"""
Класс описывающий структуру многослойной нейронной сети - персептрон.
"""
import neuron_layer as nl
import numpy as np
import neuron_utils as nu

__author__ = 'ikatlinsky'


class Perceptron:
    layers = []
    layers_x = []

    def __init__(self, size, layers_size, weights_size, act_functions):
        """
        Создает объект многослойной нейронной сети по входным параметрам.
        :param size: количество слоев в нейронной сети
        :param layers_size: количество нейрон в каждом слое сети
        :param weights_size: длина списка входных параметров для кажжого нейрона в слое
        :param act_functions: функции активации для каждого слоя, длина списка должна совпадать с числом слоев в сети
        :return: новый объект нейронной сети
        """
        if size < 0:
            raise ValueError()

        if size != len(act_functions):
            raise ValueError()

        self.layers = [nl.NeuronLayer(layers_size, weights_size, act_functions[i]) for i in range(size)]

    def get_value(self, x_list):
        """
        Возвращает результат действия нейронной сети на входной вектор сигнала x_list.
        :param x_list: входной вектор сигнала
        :return: ответ нейронной сети на входящий сигнал
        """
        if len(x_list) != self.layers[0].neurons[0].get_size():
            raise ValueError("Size of neuron values list should be equal to number of neurons")

        new_x_list = x_list

        for i in range(len(self.layers)):
            self.layers_x.append(new_x_list)
            new_x_list = self.layers[i].get_value(new_x_list)

        return new_x_list

    def set_weights(self, deltas):
        """
        Обновляет веса в нейронной сети исходя их вектора невязки deltas.
        :param deltas: вектор невязки
        """
        for i in range(len(self.layers) - 1, -1, -1):
            weights = self.layers[i].get_weights()
            delta_w = [np.multiply(self.layers_x[i][j], deltas) for j in range(self.layers[i].get_size())]

            new_weights = np.add(weights, delta_w)
            self.layers[i].set_weights(new_weights)

    def train(self):
        raise NotImplementedError()

    def check(self):
        raise NotImplementedError()


def test():
    """
    Тестирование создания нового слоя, вычисление ответа нейронной сети на входнйо сигнал и изменение весов
    в каждом слое сети.
    :return:
    """
    p = Perceptron(2, 3, 3, [nu.linear_activation, nu.linear_activation])

    print "Вычисление значения дл нейронной сети:"
    print p.get_value([0.1, 0.2, 0.1])
    print "\n"

    print "Веса нейронов в слоях до изменения"
    for i in range(len(p.layers)):
        print "Слой %s. Веса %s" % (i + 1, p.layers[i].get_weights())
    print "\n"

    print "Веса нейронов в слоях после изменения"
    p.set_weights([0.2, 0, 1.5])
    for i in range(len(p.layers)):
        print "Слой %s. Веса %s" % (i + 1, p.layers[i].get_weights())
    print "\n"

test()