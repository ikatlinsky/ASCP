# coding=utf-8
import openpyxl as xl
import matplotlib.pyplot as plot
import numpy as np

__author__ = 'ikatlinsky'

year = 'A3:A102'
population = 'B3:B102'


def get_population_wb():
    wb = xl.load_workbook(filename="ASCP01.xlsx", read_only=True, use_iterators=True)
    return wb.get_sheet_by_name("Population")


def get_ln_value(value, use_ln_value):
    """

    :param value:
    :param use_ln_value:
    :return:
    """
    return np.log(value) if use_ln_value else value

# form pairs of simple population data


def get_population_data(use_time_ln=False, use_population_ln=False):
    data_pairs = []

    for row in get_population_wb().iter_rows('A3:B102'):
        data_pairs.append([get_ln_value(row[0].value, use_time_ln), get_ln_value(row[1].value, use_population_ln)])

    return np.asanyarray(data_pairs)


# Отрисовка графиков для популяции

def draw_simple_population_data():
    data = get_population_data()
    data_population_log = get_population_data(use_population_ln=True)
    data_log = get_population_data(use_time_ln=True, use_population_ln=True)

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


draw_simple_population_data()