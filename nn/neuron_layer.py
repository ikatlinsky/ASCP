# coding=utf-8
from neuron import Neuron
import neuron_utils as nu
import random as rnd
import numpy as np

__author__ = 'ikatlinsky'


class NeuronLayer:
    """
    Объект предстваляющий собой слой нейронов. Объединяет определенной количество нейронов в единое целое
    """
    neurons = []

    def __init__(self, layer_size, neuron_size, activation_function):
        """
        Создает слой нейронов исходя из заданных параметров
        :param layer_size: размер слоя - количество нейронов в слое
        :param neuron_size: длина параметров для нейронов - длина списка весов и значений
        :param activation_function: функция активации, которая будет присвоена всем нейрона в слое
        :return: новый объект слоя
        """
        if layer_size < 1:
            raise ValueError("Neuron layer size should be greater than 1")

        if neuron_size < 1:
            raise ValueError("Neuron size should be greater than 1")

        self.neurons = [Neuron(neuron_size, activation_function) for _ in range(layer_size)]

    def get_size(self):
        """
        Возвращает количество нейронов в слое
        :return количество нейронов
        """
        return len(self.neurons)

    def get_neuron_size(self):
        """
        Возвращает размер параметров нейронов
        :return количество нейронов
        """
        return len(self.neurons[0].weights)

    def get_value(self, x_list):
        """
        Возращает результат функции активации для каждого нейрона в слое, исходя их списка значений для каждого нейрона
        :param x_list: список значений для всех нейронов
        """

        return [self.neurons[i].get_value(x_list) for i in range(len(self.neurons))]

    def set_weights(self, weights_list):
        """
        Задает веса для всех нейронв исходя их входного списка
        :param weights_list: новые значения весов для нейронов, длина должна совпадать с числом нейронов, каждый
        подсписок должен совпадать по длине с длиной весов нейронов
        :return новые веса для нейронов
        """
        if len(weights_list) != len(self.neurons):
            raise ValueError("Size of weights list should be equal to number of neurons")

        return [self.neurons[i].set_weight(weights_list[i]) for i in range(len(weights_list))]

    def get_weights(self):
        return [self.neurons[i].weights for i in range(len(self.neurons))]

    def train(self, x, t):
        """
        Обучение слоя нейронов исходя из входязего сигнала x и ожидаемого резульата t.
        :param x: входной сигнал, длина списка значений сигнала равна числу синапсов кажжого нейрона
        :param t: ожидаемый результат, длина списка t равна числу нейронов в слое
        """
        if len(t) != len(self.neurons):
            raise ValueError()

        if len(x) != self.neurons[0].get_size():
            raise ValueError()

        delta = [1 for _ in range(len(t))]

        while not all(v == 0 for v in delta):
            out = self.get_value(x)
            delta = np.subtract(t, out)

            for i in range(len(self.neurons)):
                deltas = [delta[i] * x[j] for j in range(len(x))]
                self.neurons[i].add_to_weights(deltas)

    def predict(self, x):
        return self.get_value(x)


def test():
    """
    Тестирование создани объекта слоя и проведение основныъ операций
    """
    # Создаем слой нейронов
    neuron_layer = NeuronLayer(5, 5, nu.linear_activation)

    # Выводим нейроны в слое и их длину
    print "Выводим нейроны в слое и их длину:"
    print neuron_layer.neurons
    print len(neuron_layer.neurons)
    print "\n"

    # Выводим веса для каждого нейрона и их функцию активации
    print "Выводим веса для каждого нейрона и их функцию активации:"
    for neuron in neuron_layer.neurons:
        print "Neuron weights: %s and activation function: %s" % (neuron.weights, neuron.act_func)
    print "\n"

    # Результат действия функции активации
    print "Результат действия функции активации:"
    print neuron_layer.get_value([rnd.random() for _ in range(neuron_layer.get_neuron_size())])
    print "\n"

    # Замена весов всех нейронов
    print "Замена весов всех нейронов:"
    print neuron_layer.set_weights([nu.generate_random_list(neuron_layer.get_neuron_size()) for _ in range(neuron_layer.get_size())])
    print "\n"


def test_train():
    """
    Пример обучения слоя нейронной сети.
    """
    # Создаем слой нейронов
    nl = NeuronLayer(2, 3, nu.linear_activation)

    test_vector_0 = [0, 0, 0]
    test_vector_1 = [1, 0, 0]
    test_vector_2 = [1, 1, 1]
    test_vector_3 = [0, 0, 1]

    nl.train(test_vector_0, [0, 0])
    nl.train(test_vector_1, [1, 0])
    nl.train(test_vector_2, [1, 1])
    nl.train(test_vector_3, [0, 1])

    print "Проверка обученности нейрона: (должен возвращать [0, 0]):"
    print "Вектор %s. Значение %s" % (test_vector_0, nl.predict(test_vector_0))

    print "Проверка обученности нейрона: (должен возвращать [1, 0]):"
    print "Вектор %s. Значение %s" % (test_vector_1, nl.predict(test_vector_1))

    print "Проверка обученности нейрона: (должен возвращать [1, 1]):"
    print "Вектор %s. Значение %s" % (test_vector_2, nl.predict(test_vector_2))

    print "Проверка обученности нейрона: (должен возвращать [0, 0]):"
    print "Вектор %s. Значение %s" % (test_vector_3, nl.predict(test_vector_3))


#test()
#test_train()