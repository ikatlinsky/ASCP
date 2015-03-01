# coding=utf-8
from neuron import Neuron
import neuron_utils as nu
import random as rnd

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
        :param x_list: список значений для всех нейронов, длина списка должна совпадать с числов нейронов в слое
        """
        if len(x_list) != len(self.neurons):
            raise ValueError("Size of neuron values list should be equal to number of neurons")

        return [self.neurons[i].get_value(x_list[i]) for i in range(len(x_list))]

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

    def set_weights_single(self, weights, i):
        """
        Залает веса для i-го нейрона
        :param weights: список значений весов, длина должна совпдать с длиной весов нейрона
        :param i: номер нейрона для присвоения новых весов, номер нейрона не должен быть больше количества весов
        :return новые веса для нейрона
        """
        if i > len(self.neurons):
            raise ValueError("There are no such neuron in layer")

        if len(weights) != len(self.neurons[i].weights):
            raise ValueError("Length of weights lisy should be equal")

        return self.neurons[i].set_weight(weights)


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
    print neuron_layer.get_value([[rnd.random() for _ in range(neuron_layer.get_neuron_size())] for _ in range(neuron_layer.get_size())])
    print "\n"

    # Замена весов всех нейронов
    print "Замена весов всех нейронов:"
    print neuron_layer.set_weights([nu.generate_random_list(neuron_layer.get_neuron_size()) for _ in range(neuron_layer.get_size())])
    print "\n"

    # Замена весов для одного нейрона
    print "Замена весов для одного нейрона:"
    print neuron_layer.set_weights_single(nu.generate_random_list(neuron_layer.get_neuron_size()), 2)
    print "\n"


def test_exceptions():
    NeuronLayer(0, 10, nu.linear_activation)
    NeuronLayer(5, 0, nu.linear_activation)


test()
# test_exceptions()