# coding=utf-8
import matplotlib.pyplot as plot
import numpy as np
import numpy.linalg as la
import data_population_parsing as dpp

__author__ = 'ikatlinsky'

population = dpp.get_population_data()
population_ln = dpp.get_population_data(use_population_ln=True)


def plan_matrix(data):
    return [[1, element[0]] for element in data]


def data_vector(data):
    return [[element[1]] for element in data]

plan_matrix = plan_matrix(population)
y = data_vector(population)
y_ln = data_vector(population_ln)


def regression_coefficients(plan, y):
    u, s, v = la.svd(np.dot(np.transpose(plan), plan))
    inv_s = np.diag([1/d for d in s])
    # (V.invS.Transpose[U])
    c = np.dot(np.dot(v, inv_s), np.transpose(u))
    # (V.invS.Transpose[U]).Transpose[plan]
    c = np.dot(c, np.transpose(plan))
    # (V.invS.Transpose[U]).Transpose[plan].Transpose[{y}]
    c = np.dot(c, np.transpose([y]))

    return [c[0, 0, 0], c[1, 0, 0]]


def f(t, c):
    return c[0] + c[1] * t

# Линейная модель
print regression_coefficients(plan_matrix, y)
linear_model = regression_coefficients(plan_matrix, y)
plot.plot(population[:, 0], population[:, 1], linestyle='-', color='r')
plot.plot(population[:, 0], [f(t, linear_model) for t in population[:, 0]])
plot.show()

print "\n"

# Экспоненциальная модель
print regression_coefficients(plan_matrix, y_ln)
exp_model = regression_coefficients(plan_matrix, y)
plot.plot(population_ln[:, 0], population_ln[:, 1], linestyle='-', color='r')
plot.plot(population_ln[:, 0], [f(t, exp_model) for t in population_ln[:, 0]])
plot.show()