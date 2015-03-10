# coding=utf-8
"""
Класс для выполнения операций нормализации множеств, создания тестовых множеств, манипулирования ими,
извлечения данных из множеств и так далее.
"""
import random as rnd
import numpy as np

__author__ = 'ikatlinsky'


def create_set(size):
    """
    Создает двумерное множество заданной размерности.
    :param size: размерность множества
    :return: множество вида [[x1, y1], ...]
    """
    return [[rnd.random(), rnd.random()] for _ in range(size)]


def create_numbered_set(size):
    """
    Создает двумерное множество заданной размерности, каждый элемент которого принадлежит к некторому классу.
    :param size:  размерность множества
    :return: множество вида [[[x1, y1], c1], ...], где c1 - класс точки
    """
    return [[[rnd.random(), rnd.random()], rnd.randint(0, 1)] for _ in range(size)]


def get_points(data):
    """
    Возвращает список значений для множества нумерованных двумерных точек ([[[x1, y1], c1], ...]).
    :param data: множество вида [[[x1, y1], c1], ...]
    :return: множество вида [[x1, y1], ...]
    """
    return [data[i][0] for i in range(len(data))]


def get_classes(data):
    """
    Возвращает список классов для множества нумерованных двумерных точек ([[[x1, y1], c1], ...]).
    :param data: множество вида [[[x1, y1], c1], ...]
    :return: множество вида [c1, c2, ...]
    """
    return [data[i][1] for i in range(len(data))]


def get_x(data):
    """
    Возвращает координаты x для множества нумерованных двумерных точек ([[[x1, y1], c1], ...]).
    :param data: множество вида [[[x1, y1], c1], ...]
    :return: множество вида [x1, x2, ...]
    """
    data = get_points(data)
    return [data[i][0] for i in range(len(data))]


def get_y(data):
    """
    Возвращает координаты y для множества нумерованных двумерных точек ([[[x1, y1], c1], ...]).
    :param data: множество вида [[[x1, y1], c1], ...]
    :return: множество вида [y1, y2, ...]
    """
    data = get_points(data)
    return [data[i][1] for i in range(len(data))]


def mean_to_zero(data):
    """
    Нормализует множество таким образрм, чтобы средние значения координат множества равнялись 0.
    :param data: входное множество вида [[x1, y1], ...]
    :return: нормализованное множество
    """
    new_set = []

    mean_x = np.mean([data[i][0] for i in range(len(data))])
    mean_y = np.mean([data[i][1] for i in range(len(data))])

    for i in range(len(data)):
        new_set.append([data[i][0] - mean_x, data[i][1] - mean_y])

    return new_set


def std_to_one(set_with_zero_mean):
    """
    Нормализует множество таким образов, чтобы среднее отколнение координат равнялось 1.
    :param set_with_zero_mean: входное множество вида [[x1, y1], ...]
    :return: нормализованное множество
    """
    data = set_with_zero_mean
    new_set = []

    std_x = np.std([data[i][0] for i in range(len(data))])
    std_y = np.std([data[i][1] for i in range(len(data))])

    for i in range(len(data)):
        new_set.append([data[i][0] / std_x, data[i][1] / std_y])

    return new_set


def norm_svm(numbered_set):
    """
    Полный цикл нормализации: приведение среднего к 0 и отколнения к 1
    :param numbered_set: множество вида [[[x1, y1], c1], ...]
    :return: нрмализованное множество
    """
    data = [numbered_set[i][0] for i in range(len(numbered_set))]

    data = mean_to_zero(data)
    data = std_to_one(data)

    return [[data[i], numbered_set[0][1]] for i in range(len(data))]


def test():
    """
    Проверка функций нормализации множества.
    """
    # Нормализация множества
    normalized = norm_svm(create_numbered_set(10))

    # Выводим нормализованные точки
    print "Выводим нормализованные точки:"
    print get_points(normalized)

    # Выводим средние значения по координатам после нормализации
    print "Выводим средние значения по координатам после нормализации:"
    print np.mean(get_x(normalized))
    print np.mean(get_y(normalized))

    # Выводим среднеее отклонение по координатам после нормализации
    print "Выводим среднеее отклонение по координатам после нормализации:"
    print np.std(get_x(normalized))
    print np.std(get_y(normalized))


test()

