# coding=utf-8
__author__ = 'ikatlinsky'


class Neuron(object):
    """
    Представляет собой нейрон, содержащий данные о его значениях и весах.
    """
    neurons = []
    weights = []

    def __init__(self, neurons, weights):
        # если длины списков не совпадает, то создаваемый объект не корректен - бросаем исключение
        if len(neurons) != len(weights):
            raise AssertionError("Length of neuron values and weights should be equal.", neurons, weights)

        self.neurons = neurons
        self.weights = weights

    def scalar_product(self):
        """
        Находит скалярное произведение значений и весов нейрона
        :return: скалярное произведение
        """
        return sum(p * q for p, q in zip(self.neurons, self.weights))

    def first_product(self):
        """
        Находит произведение первый элементов из списка значений и списка весов нейрона
        :return: произведение 1ых элементов
        """
        return self.neurons[0] * self.weights[0]

    def apply_activation(self, activation_function):
        """
        Применение функции активации к нейрону
        :param activation_function: функция активации нейрона: линейная, пороговая, сигмоидальная
        :return: результат действия функции активации
        """
        return activation_function(self)

    def __str__(self):
        return "Neuron values: %s, weight values: %s" % (self.neurons, self.weights)