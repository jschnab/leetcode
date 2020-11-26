from itertools import combinations


def helper(array, data, start, end, index, size, result):
     if index == size:
         result.append(data.copy())
         return
     for i in range(start, end):
         data[index] = array[i]
         helper(array, data, i+1, end, index+1, size, result)


def mycombinations(array, size):
    result = []
    helper(array, [0]*size, 0, len(array), 0, size, result)
    return result


def mycombinationsiter(array, size):
    pool = tuple(array)
    length = len(pool)
    if size > length:
        return
    indices = list(range(size))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(size)):
            if indices[i] != i + length - size:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, size):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def test1():
    array = [2, 5, 3, 4]
    size = 2
    print(list(mycombinationsiter(array, size)))
    print()
    print(list(combinations(array, size)))


def main():
    test1()


if __name__ == "__main__":
    main()
