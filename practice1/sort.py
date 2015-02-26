__author__ = 'ikatlinsky'

a = [5, 4, 3, 2, 8]

print a


def sort_double(array):
    """
    :param array:
    :return:
    """
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array


print sort_double(a)

m = [[1, 3, 1], [2, 5, 3]]


def my_max(matrix):
    temp_max = matrix[0]

    for x in matrix[1:]:
        for i in range(len(x)):
            if x[i] > temp_max[i]:
                temp_max[i] = x[i]

    return temp_max


print my_max(m)

maxList = my_max(m)


m = [[1, 3, 1], [2, 5, 3]]
print m
# print encode(maxList, m)


def encode_2(matrix, maxes):
    result = []

    for x in matrix:
        template = [[0] * i for i in maxes]

        for i in range(len(x)):
            template[i][x[i] - 1] = 1

        result.append(template)

    return result


print encode_2(m, maxList)