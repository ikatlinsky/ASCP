# coding=utf-8
import matplotlib.pyplot as plot
import numpy as np
import numpy.linalg as la
import data_parsing as dp

__author__ = 'ikatlinsky'

# Линейная и экспоненциальная модели #
# Вычисление коэффициентов для линейной и эуспоненциальной моделей


def regression_coefficients(data):
    """
    Вычисление коэффициентов для линейной и экспоненциальной моделей
    :param data: numpy массив вида [[year1, population1], ...]
    :return: массив коэффициентов модели вида [c1, c2]
    """
    plan = [[1, val[0]] for val in data]
    y = [val for val in data[:, 1]]

    u, s, v = la.svd(np.dot(np.transpose(plan), plan))
    inv_s = np.diag([1 / d for d in s])
    # (V.invS.Transpose[U])
    c = np.dot(np.dot(v, inv_s), np.transpose(u))
    # (V.invS.Transpose[U]).Transpose[plan]
    c = np.dot(c, np.transpose(plan))
    # (V.invS.Transpose[U]).Transpose[plan].Transpose[{y}]
    c = np.dot(c, np.transpose([y]))

    return [c[0, 0], c[1, 0]]


def f(t, c):
    """
    Функция задающая график модели по коэффициетам
    :param t: параметр - годы
    :param c: коэффициенты
    :return: начения линейной модели в заданной точке t
    """
    return c[0] + c[1] * t

# Функция отрисовки графиков для линейной и экспоненциальной моделей

# Данные из одного источника
population = dp.get_single_source_data()
# Данные из нескольких источников
population_ds = dp.get_multiple_sources_data()[0]
population_ds_ln = dp.get_multiple_sources_data(use_population_ln=True)[0]


def show_plots_for_different_sources():
    print "Коэффициенты линейной модели (различные источники): %s" % regression_coefficients(population_ds)
    print "Коэффициенты экспоненциальной модели (различные источники): %s" % regression_coefficients(population_ds_ln)

    plot.figure(1, figsize=(19, 10), dpi=80)

    # Линейная модель
    data = dp.get_multiple_sources_data()
    linear_model = regression_coefficients(population_ds)
    plot.subplot(211)
    plot.plot(
        population_ds[:, 0], population_ds[:, 1],
        data[1][:, 0], data[1][:, 1],
        data[2][:, 0], data[2][:, 1],
        linestyle='-', color='r', label="Population data", linewidth=5
    )
    plot.plot(population_ds[:, 0], [f(t, linear_model) for t in population_ds[:, 0]], label="Linear model", linewidth=5)
    plot.fill_between(data[1][:, 0], data[1][:, 1], data[2][:, 1], color='red')
    plot.xlabel("T")
    plot.ylabel("N")
    plot.title("Population: Linear Model")
    plot.legend(loc='upper left')

    # Экспоненциальная модель
    data = dp.get_multiple_sources_data(use_population_ln=True)
    exp_model = regression_coefficients(population_ds_ln)
    plot.subplot(212)
    plot.plot(
        population_ds_ln[:, 0], population_ds_ln[:, 1],
        data[1][:, 0], data[1][:, 1],
        data[2][:, 0], data[2][:, 1],
        linestyle='-', color='r', label="Population data", linewidth=5
    )
    plot.plot(population_ds_ln[:, 0], [f(t, exp_model) for t in population_ds_ln[:, 0]], label="Exponential model", linewidth=5)
    plot.fill_between(data[1][:, 0], data[1][:, 1], data[2][:, 1], color='red')
    plot.xlabel("T")
    plot.ylabel("Ln(N)")
    plot.title("Population: Exponential model")
    plot.legend(loc='upper left')

    plot.show()


# Гиперболическая модель #
# Вычисление коэффицентов для гиперболической модели

def regression_coefficients_hyper(data):
    """
    Вычисление коэффициентов для гиперболической модели
    :param data: numpy массив вида [[year1, population1], ...]
    :return: массив коэффициентов модели вида [c1, c2]
    """
    data = np.asanyarray(data)
    t0 = 2016
    y = [np.log(val) for val in data[:, 1]]
    x = [np.log(t0 - val) for val in data[:, 0]]

    r = 10
    c2 = 0
    while r > 5 and (-1 - c2) < 0.1:
        t0 += 1
        pl_m = [[1, np.log(t0 - val[0])] for val in data]
        u, s, v = la.svd(np.dot(np.transpose(pl_m), pl_m))
        inv_s = np.diag([1 / d for d in s])
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


def hyp_f(t, c):
    """
    Функция задающая график гиперболической модели
    :param t: параметр
    :param c: коэффиценты
    :return: значение для модели в точке t
    """
    return np.exp(c[0]) / (c[1] - t)

# Функция отрисовки графиков для гиперболической модели


def show_plots_for_single_source_hyp():
    print "Коэффициенты гиперболической модели (различные источники): %s" % regression_coefficients_hyper(population_ds)
    hyp_model = regression_coefficients_hyper(population_ds)

    plot.figure(1, figsize=(19, 10), dpi=80)
    plot.subplot(111)
    plot.plot(population_ds[:, 0], population_ds[:, 1], linestyle='-', color='r', label="Population data", linewidth=5)
    plot.plot(population_ds[:, 0], [hyp_f(t, hyp_model) for t in population_ds[:, 0]], label="Hyper model", linewidth=5)
    plot.xlabel("T")
    plot.ylabel("N")
    plot.title("Population: Hyper model")
    plot.legend(loc='upper left')
    plot.show()


# Вызов функций

show_plots_for_different_sources()
show_plots_for_single_source_hyp()