# coding=utf-8
import matplotlib.pyplot as plot
import numpy as np
import numpy.linalg as la
import data_population_parsing as dpp
import data_different_sources_parsing as ddsp

__author__ = 'ikatlinsky'


def plan_matrix(data):
    return [[1, element[0]] for element in data]


def data_vector(data):
    return [element[1] for element in data]


def regression_coefficients(plan, y):
    print y
    u, s, v = la.svd(np.dot(np.transpose(plan), plan))
    inv_s = np.diag([1/d for d in s])
    # (V.invS.Transpose[U])
    c = np.dot(np.dot(v, inv_s), np.transpose(u))
    # (V.invS.Transpose[U]).Transpose[plan]
    c = np.dot(c, np.transpose(plan))
    # (V.invS.Transpose[U]).Transpose[plan].Transpose[{y}]
    c = np.dot(c, np.transpose([y]))

    return [c[0, 0], c[1, 0]]


def regression_coefficients_hyper(data):
    data = np.asanyarray(data)
    t0 = 2016
    y = [np.log(val) for val in data[:, 1]]
    x = [np.log(t0 - val) for val in data[:, 0]]

    print y

    r = 10
    c2 = 0
    while r > 5 and (-1 - c2) < 0.1:
        t0 += 1
        pl_m = [[1, np.log(t0 - val[0])] for val in data]
        u, s, v = la.svd(np.dot(np.transpose(pl_m), pl_m))
        inv_s = np.diag([1/d for d in s])
        # (V.invS.Transpose[U])
        c = np.dot(np.dot(v, inv_s), np.transpose(u))
        # (V.invS.Transpose[U]).Transpose[plan]
        c = np.dot(c, np.transpose(pl_m))
        # (V.invS.Transpose[U]).Transpose[plan].Transpose[{y}]
        c = np.dot(c, np.transpose([y]))

        r = 0

        for i in range(len(data)):
            r += np.power(y[i] - c[0, 0] - c[1, 0] * x[i], 2)

        r = np.sqrt(r)
        c2 = c[1, 0]

    return [c[0, 0], t0]


def f(t, c):
    return c[0] + c[1] * t

# single source data
population = dpp.get_population_data()
population_ln = dpp.get_population_data(use_population_ln=True)

plan_matrix_ss = plan_matrix(population)
y = data_vector(population)
y_ln = data_vector(population_ln)

# multiple sources data
population_ds = ddsp.get_data_from_different_sources()[0]
population_ds_ln = ddsp.get_data_from_different_sources(use_population_ln=True)[0]

plan_matrix_ds = plan_matrix(population_ds)
y_ds = data_vector(population_ds)
y_ds_ln = data_vector(population_ds_ln)


def show_plots_for_single_source():
    print "Коэффициенты линейной модели: %s" % regression_coefficients(plan_matrix_ss, y)
    print "Коэффициенты линейной модели: %s" % regression_coefficients(plan_matrix_ss, y_ln)

    plot.figure(1, figsize=(19, 10), dpi=80)

    # Линейная модель
    linear_model = regression_coefficients(plan_matrix_ss, y)
    plot.subplot(211)
    plot.plot(population[:, 0], population[:, 1], linestyle='-', color='r')
    plot.plot(population[:, 0], [f(t, linear_model) for t in population[:, 0]])
    plot.xlabel("T")
    plot.ylabel("N")
    plot.title("Population: Linear model")

    # Экспоненциальная модель
    exp_model = regression_coefficients(plan_matrix_ss, y_ln)
    plot.subplot(212)
    plot.plot(population_ln[:, 0], population_ln[:, 1], linestyle='-', color='r')
    plot.plot(population_ln[:, 0], [f(t, exp_model) for t in population_ln[:, 0]])
    plot.xlabel("T")
    plot.ylabel("Ln(N)")
    plot.title("Population: Exponential model")

    plot.show()


def show_plots_for_different_sources():
    print "Коэффициенты линейной модели: %s" % regression_coefficients(plan_matrix_ds, y_ds)
    print "Коэффициенты линейной модели: %s" % regression_coefficients(plan_matrix_ds, y_ds_ln)

    plot.figure(1, figsize=(19, 10), dpi=80)

    # Линейная модель
    data = ddsp.get_data_from_different_sources()
    linear_model = regression_coefficients(plan_matrix_ds, y_ds)
    plot.subplot(211)
    plot.plot(
        population_ds[:, 0], population_ds[:, 1],
        data[1][:, 0], data[1][:, 1],
        data[2][:, 0], data[2][:, 1],
        linestyle='-', color='r'
    )
    plot.plot(population_ds[:, 0], [f(t, linear_model) for t in population_ds[:, 0]])
    plot.fill_between(data[1][:, 0], data[1][:, 1], data[2][:, 1], color='red')
    plot.xlabel("T")
    plot.ylabel("N")
    plot.title("Population: Linear Model")

    # Экспоненциальная модель
    data = ddsp.get_data_from_different_sources(use_population_ln=True)
    exp_model = regression_coefficients(plan_matrix_ds, y_ds_ln)
    plot.subplot(212)
    plot.plot(
        population_ds_ln[:, 0], population_ds_ln[:, 1],
        data[1][:, 0], data[1][:, 1],
        data[2][:, 0], data[2][:, 1],
        linestyle='-', color='r'
    )
    plot.plot(population_ds_ln[:, 0], [f(t, exp_model) for t in population_ds_ln[:, 0]])
    plot.fill_between(data[1][:, 0], data[1][:, 1], data[2][:, 1], color='red')
    plot.xlabel("T")
    plot.ylabel("Ln(N)")
    plot.title("Population: Exponential model")

    plot.show()


def hyp_f(t, c):
    return np.exp(c[0])/(c[1] - t)


def show_plots_for_single_source_hyp():
    # population = dpp.get_population_data(use_population_ln=True)
    hyp_model = regression_coefficients_hyper(population)
    plot.plot(population[:, 0], population[:, 1], linestyle='-', color='r')
    plot.plot(population[:, 0], [f(t, hyp_model) for t in population[:, 0]])
    plot.xlabel("T")
    plot.ylabel("N")
    plot.title("Population: Hyper model")
    plot.show()


show_plots_for_single_source()
show_plots_for_different_sources()
show_plots_for_single_source_hyp()