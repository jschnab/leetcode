def binary_search(array, x):
    """
    Find element x in an array.
    """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high - 1) // 2
        if x == array[mid]:
            return True
        if x > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False
