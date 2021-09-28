import numpy as np


def find_longest_array(array):
    longest = (0, )
    for element in array:
        if element.shape > longest:
            longest = element.shape
    return longest


def pad_array(array):
    max_size = find_longest_array(array)
    new_arr = []
    for element in array:
        padded_array = np.zeros((max_size))
        padded_array[:len(element)] = element
        new_arr.append(padded_array)
    return np.array(new_arr)
