# coding=utf-8
__author__ = 'ikatlinsky'

from neuron_functions import neuron, sigma_activation, linear_activation, step_activation
from neuron import Neuron

x = (1, 3, 10)
w = (0.6, 0.3, 0.1)

print "Создаем корректный объект нейрона:"
n = Neuron(x, w)
print n,
print "\n"

print "Применяем линейную функцию активации:"
print "neuron(linear_activation, n): %f" % neuron(linear_activation, n)
print "n.apply_activation(linear_activation): %f" % n.apply_activation(linear_activation)
print "\n"

print "Применяем пороговую функцию активации:"
print "neuron(step_activation, n): %f" % neuron(step_activation, n)
print "n.apply_activation(step_activation): %f" % n.apply_activation(step_activation)
print "\n"

print "Применяем сигмоидальную функцию активации:"
print "neuron(sigma_activation, n): %f" % neuron(sigma_activation, n)
print "n.apply_activation(sigma_activation): %f" % n.apply_activation(sigma_activation)
print "\n"

# print "Тестируем исключительные ситуации:"

# print "Создаем нейрон с разной длиной занчений и весов:"
# n2 = Neuron((1, 2, 3), (3, 4))
# print "\n"

# print "Подаем функции активации объект не типа Neuron:"
# neuron(sigma_activation, (1, 2, 3))





