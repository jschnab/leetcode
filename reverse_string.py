# reverse string in python

def rev_str1(s):
    return ''.join(list(s)[::-1])

def rev_str2(s):
    l = list(s)
    size = len(s)
    for i in range(0, size // 2):
        l[i], l[size - i - 1] = l[size - i - 1], l[i]
    return ''.join(l)
