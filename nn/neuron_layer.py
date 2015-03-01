# coding=utf-8
from neuron import Neuron
import neuron_utils as nu

__author__ = 'ikatlinsky'


class NeuronLayer:
    """

    """
    neurons = []

    def __init__(self, layer_size, neuron_size, activation_function):
        """

        :param layer_size:
        :param neuron_size:
        :param activation_function:
        :return:
        """
        if layer_size < 1:
            raise ValueError("Neuron layer size should be greater than 1")

        if neuron_size < 1:
            raise ValueError("Neuron size should be greater than 1")

        self.neurons = [Neuron(neuron_size, activation_function) for _ in range(layer_size)]

    def get_size(self):
        """
        """
        return len(self.neurons)

    def get_value(self, x_list):
        """

        :param x_list:
        """
        if len(x_list) != len(self.neurons):
            raise ValueError("Size of neuron values list should be equal to number of neurons")

        return [self.neurons[i].get_value(x_list[i]) for i in range(len(x_list))]

    def set_weights(self, weights_list):
        """

        :param weights_list:
        """
        if len(weights_list) != len(self.neurons):
            raise ValueError("Size of weights list should be equal to number of neurons")

        [self.neurons[i].set_weight(weights_list[i]) for i in range(len(weights_list))]

    def set_weights(self, weights, i):
        """

        :param weights:
        :param i:
        """
        if i > len(self.neurons):
            raise ValueError("There are no such neuron in layer")

        if len(weights) != len(self.neurons[i].weights):
            raise ValueError("Length of weights lisy should be equal")

        self.neurons[i].set_weight(weights)


def test():
    """

    :return:
    """
    # Создаем слой нейронов
    neuron_layer = NeuronLayer(5, 5, nu.linear_activation)

    # Выводим нейроны в слое и их длину
    print neuron_layer.neurons
    print len(neuron_layer.neurons)

    # Выводим веся для каждого нейрона и их функцию активации
    for neuron in neuron_layer.neurons:
        print "Neuron weights: %s and activation function: %s" % (neuron.weights, neuron.act_func)


def test_exceptions():
    NeuronLayer(0, 10, nu.linear_activation)
    NeuronLayer(5, 0, nu.linear_activation)


test()
# test_exceptions()