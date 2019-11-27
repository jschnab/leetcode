# leetcode 953
# verify that words in a list according to a weird dictionary

def alien_dict(words, order):
    """Returns True if words are sorted according to order else False."""

    # compares word to the next one in the list
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]

        # iterates through word letters to see if they are sorted
        for j in range(min(len(w1), len(w2))):
            
            # it we find a different letter, we return False if
            # words are not sorted, else we break the for loop
            # since it means word are sorted
            if w1[j] != w2[j]:
                if order.index(w1[j]) > order.index(w2[j]):
                    return False
                break

        # if words are sorted based on letter we check the shorter word
        # if first in the list
        if len(w1) > len(w2):
            return False

    # if we did not find any problem so far it means words are sorted
    return True

if __name__ == '__main__':
    words = ['hello', 'leetcode', 'absolute']
    order = 'hlabcdefgijkmnopqrstuvwxyz'
    print(words)
    print(order)
    print(alien_dict(words, order))
    print('True should be printed')
    print()
    words = ['apple', 'app']
    print(words)
    print(order)
    print(alien_dict(words, order))
    print('False should be printed')

