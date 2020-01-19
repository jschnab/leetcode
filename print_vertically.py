# leetcode contest 172 problem 1324

from itertools import zip_longest


def print_vertically(sentence):
    """
    Print vertically a sentence.
    "how are you" becomes "hay" "oro" "weu"

    Complete with spaces when necessary but trailing spaces are not allowed.
    "to be or not to be" becomes "tbontb" "oerooe" "   t"

    :param str sentence: sentence to print vertically
    :return list[str]:
    """
    columns = sentence.split()
    rows = zip_longest(*columns, fillvalue=" ")
    return ["".join(r).rstrip() for r in rows]


def print_vertically2(sentence):
    """
    Print vertically a sentence.

    This is another version or print_vertically which does not use Python
    builtin functions.

    :param str sentence: sentence to print vertically
    :return list[str]:
    """
    splitted = sentence.split()

    # output length is length of the longest word
    max_length = 0
    for sp in splitted:
        max_length = max(max_length, len(sp))
    output = [""] * max_length

    # left-pad short words with spaces
    for i, sp in enumerate(splitted):
        if len(sp) < max_length:
            splitted[i] += " " * (max_length - len(sp))

    # list of pointers to characters in `splitted`
    pointers = [0] * len(splitted)

    # we will iterate over characters with pointers until we reach
    # each splitted word's end
    lengths = [max_length] * len(splitted)

    # iterate over characters and fill output
    while pointers != lengths:
        for i, p in enumerate(pointers):
            output[p] += splitted[i][p]
            pointers[i] += 1

    # trailing spaces not allowed
    return [o.rstrip() for o in output]



if __name__ == "__main__":
    print(print_vertically2("how are you"))
