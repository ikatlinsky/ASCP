# coding=utf-8
"""
Класс для тестирования функционала применения метода svm к множествам.
"""

from sklearn import svm
import svm_normalization as su

__author__ = 'ikatlinsky'


def apply_svm(data):
    """
    Применение метода svm к множеству data
    :param data: множество вида [[[x1, y1], c1], ...], где c1 - класс
    :return: обученный объект, способный определять принадлежность точки к классу
    """
    # множество точек
    x = su.get_points(data)
    # множество классов
    y = su.get_classes(data)
    # обучение
    clf = svm.SVC()
    clf.fit(x, y)

    return clf


def test():
    """
    Тестирование обученной сети методом svm.
    """
    points = su.create_numbered_set(10)
    print points
    predictor = apply_svm(points)

    print predictor.predict([[1., 1.]])


test()

