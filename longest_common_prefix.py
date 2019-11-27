# script which returns the longest common prefix among a list of strings

class Solution(object):
    def common_prefix(strings):
        output = ''
        for i in range(len(strings[0])):
            letter = strings[0][i]
            for s in strings[1:]:
                if i + 1 > len(s) or s[i] != letter:
                    return output
            output += letter
        return output

if __name__ == '__main__':
    # strings = ['flower', 'flight', 'flow']
    # answer -> 'fl'

    n = int(input('Please enter the number of strings: '))
    strings = [''] * n
    for i in range(n):
        strings[i] = input('String {0}: '.format(i))
    print(Solution.common_prefix(strings))
