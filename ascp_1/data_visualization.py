# coding=utf-8
"""
Класс содержит методы отображения графиков численности популяции в ращличных шкалах для случая одного или нескольких
источников.
"""

import matplotlib.pyplot as plot
import data_parsing as dp

__author__ = 'ikatlinsky'

# Отрисовка данных по одному источнику


def draw_single_source_data():
    """
    Отображает данные из одного истоника в трех координатах: (T, N), (T, ln(N)), (ln(T), ln(N)).
    :return:
    """
    data = dp.get_single_source_data()
    data_population_log = dp.get_single_source_data(use_population_ln=True)
    data_log = dp.get_single_source_data(use_time_ln=True, use_population_ln=True)

    plot.figure(1, figsize=(19, 10), dpi=80)

    # Данные в стандартной шкале
    plot.subplot(221)
    plot.plot(data[:, 0], data[:, 1], linestyle='-', color='r')
    plot.xlabel("T")
    plot.ylabel("N")
    plot.title("Population: standard scale")

    # Численность населения - ln
    plot.subplot(222)
    plot.plot(data_population_log[:, 0], data_population_log[:, 1], linestyle='-', color='g')
    plot.xlabel("T")
    plot.ylabel("Ln(N)")
    plot.title("Population: Ln from population")

    # Года и численность населения - ln
    plot.subplot(212)
    plot.plot(data_log[:, 0], data_log[:, 1], linestyle='-', color='b')
    plot.xlabel("Ln(T)")
    plot.ylabel("Ln(N)")
    plot.title("Population: Ln from population and time")

    plot.tight_layout()
    plot.show()

# Отрисовка данных из разных источников


def draw_multiple_sources_data():
    """
    Отображает данные из многих истоников в трех координатах: (T, N), (T, ln(N)), (ln(T), ln(N)).
    :return:
    """
    data = dp.get_multiple_sources_data()
    data_population_ln = dp.get_multiple_sources_data(use_population_ln=True)
    data_all_ln = dp.get_multiple_sources_data(use_time_ln=True, use_population_ln=True)

    plot.figure(1, figsize=(19, 10), dpi=80)

    # Данные в стандартной шкале
    plot.subplot(221)
    plot.plot(
        data[0][:, 0], data[0][:, 1],
        data[1][:, 0], data[1][:, 1],
        data[2][:, 0], data[2][:, 1],
        linestyle='-', color='r'
    )
    plot.fill_between(data[1][:, 0], data[1][:, 1], data[2][:, 1], color='red')
    plot.xlabel("T")
    plot.ylabel("N")
    plot.title("Population: standard scale")

    # Численность населения - ln
    plot.subplot(222)
    plot.plot(
        data_population_ln[0][:, 0], data_population_ln[0][:, 1],
        data_population_ln[1][:, 0], data_population_ln[1][:, 1],
        data_population_ln[2][:, 0], data_population_ln[2][:, 1],
        linestyle='-', color='g'
    )
    plot.fill_between(data_population_ln[1][:, 0], data_population_ln[1][:, 1], data_population_ln[2][:, 1], color='green')
    plot.xlabel("T")
    plot.ylabel("Ln(N)")
    plot.title("Population: Ln from population")

    # Года и численность населения - ln
    plot.subplot(212)
    plot.plot(
        data_all_ln[0][:, 0], data_all_ln[0][:, 1],
        data_all_ln[1][:, 0], data_all_ln[1][:, 1],
        data_all_ln[2][:, 0], data_all_ln[2][:, 1],
        linestyle='-', color='b'
    )
    plot.fill_between(data_all_ln[1][:, 0], data_all_ln[1][:, 1], data_all_ln[2][:, 1], color='blue')
    plot.xlabel("Ln(T)")
    plot.ylabel("Ln(N)")
    plot.title("Population: Ln from population and year")

    plot.tight_layout()
    plot.show()


# Вызов методов отрисовки

draw_single_source_data()
draw_multiple_sources_data()