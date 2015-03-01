# coding=utf-8
import openpyxl as xl
import matplotlib.pyplot as plot
import numpy as np

__author__ = 'ikatlinsky'


def get_different_sources_wb():
    wb = xl.load_workbook(filename="ASCP01.xlsx", read_only=True, use_iterators=True)
    return wb.get_sheet_by_name("Different sources")


def get_ln_value(value, use_ln_value):
    """
    Возвращает исходное значение если :param use_ln_value=False, иначе верен натуральный логарифм от значения
    :param value: значение для вычисления логарифма
    :param use_ln_value: True - если надо получить логарфм от значения
    :return: результат
    """
    return np.log(value) if use_ln_value else value


def get_data_from_different_sources(use_time_ln=False, use_population_ln=False):
    """

    :param use_time_ln:
    :param use_population_ln:
    :return:
    """
    data_pairs = []
    max_pairs = []
    min_pairs = []

    for row in get_different_sources_wb().iter_rows('A3:L83'):
        #
        year = get_ln_value(row[0].value, use_time_ln)
        #
        values_row = []

        for num in range(1, len(row)):
            #
            if row[num].value is not None:
                #
                if "--" not in str(row[num].value):
                    val = get_ln_value(row[num].value, use_population_ln)
                    data_pairs.append([year, val])
                    values_row.append(val)
                #
                else:
                    values = [x.strip() for x in row[num].value.split('--')]
                    data_pairs.append([year, get_ln_value(values[0], use_population_ln)])
                    data_pairs.append([year, get_ln_value(values[1], use_population_ln)])
                    values_row.append(get_ln_value(values[0], use_population_ln))
                    values_row.append(get_ln_value(values[1], use_population_ln))

        #
        if len(values_row) > 0:
            #
            max_pop = np.amax(values_row)
            min_pop = np.amin(values_row)
            #
            max_pairs.append([year, max_pop])
            min_pairs.append([year, min_pop])

    return [np.asanyarray(data_pairs), np.asanyarray(max_pairs), np.asanyarray(min_pairs)]


def draw_population_data():
    data = get_data_from_different_sources()
    data_population_ln = get_data_from_different_sources(use_population_ln=True)
    data_all_ln = get_data_from_different_sources(use_time_ln=True, use_population_ln=True)

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


# draw_population_data()