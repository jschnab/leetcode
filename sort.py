from random import randint


def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        while i > 0 and array[i-1] > current:
            array[i] = array[i-1]
            i -= 1
        array[i] = current


def selection_sort(array):
    for i in range(len(array)):
        mini = i
        for j in range(i + 1, len(array)):
            if array[j] < array[mini]:
                mini = j
        array[i], array[mini] = array[mini], array[i]


def merge_sort(array):
    if len(array) > 1:

        q = len(array) // 2  # median index
        low = array[:q]
        high = array[q:]

        merge_sort(low)
        merge_sort(high)

        i = 0  # index of the low sub-array
        j = 0  # index of the high sub-array
        k = 0  # index of the merged array

        # iterate over sub-arrays elements in parallel
        # and fill the main array
        while i < len(low) and j < len(high):
            if low[i] < high[j]:
                array[k] = low[i]
                i += 1
            else:
                array[k] = high[j]
                j += 1
            k += 1

        if i < len(low):
            array[k:] = low[i:]
        elif j < len(high):
            array[k:] = high[j:]


def _partition(array, p, r):
    q = p
    for j in range(p, r):
        if array[j] <= array[r]:
            array[j], array[q] = array[q], array[j]
            q += 1
    array[r], array[q] = array[q], array[r]
    return q


def _quick_sort(array, p, r):
    if p < r:
        q = _partition(array, p, r)
        _quick_sort(array, p, q-1)
        _quick_sort(array, q+1, r)


def quick_sort(array):
    _quick_sort(array, 0, len(array)-1)


if __name__ == "__main__":
    array = [randint(0, 100) for _ in range(10)]
    print(array)
    merge_sort(array)
    print("Merge sort :", array)
