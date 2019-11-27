from random import randint
from time import time

import matplotlib.pyplot as plt

from sort import merge_sort, quick_sort, selection_sort, insertion_sort


def time_func(fun, length, n_runs=3):
    """
    Return the average time of running a function sorting an array.

    :param fun: function to be called, takes a single argument which is
                a list
    :param int length: length of the array to sort
    :param int n_runs: number of runs to perform
    """
    arrays = []
    for _ in range(n_runs):
        arrays.append([randint(0, 1000000) for _ in range(length)])
    runtimes = []
    for a in arrays:
        start = time()
        fun(a)
        stop = time()
        runtimes.append(stop - start)
    return sum(runtimes) / n_runs


if __name__ == "__main__":
    lengths = [10, 100, 500, 1000, 1250, 1500, 1750, 2000]
    time_builtin = [time_func(sorted, l) for l in lengths]
    time_selection = [time_func(selection_sort, l) for l in lengths]
    time_insertion = [time_func(insertion_sort, l) for l in lengths]
    time_merge = [time_func(merge_sort, l) for l in lengths]
    time_quick = [time_func(quick_sort, l) for l in lengths]

    fig, ax = plt.subplots()
    ax.plot(lengths, time_builtin, label="builtin sort")
    ax.plot(lengths, time_selection, label="selection sort")
    ax.plot(lengths, time_insertion, label="insertion sort")
    ax.plot(lengths, time_merge, label="merge sort")
    ax.plot(lengths, time_quick, label="quick sort")
    ax.legend()
    plt.show()
