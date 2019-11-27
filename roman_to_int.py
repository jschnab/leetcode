# script which converts roman numerals to integers

def roman_to_int(roman):
    """Convert roman numeral to integer."""
    dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    answer = 0
    i = 0
    while i < (len(roman) - 1):
        if dic[roman[i]] < dic[roman[i + 1]]:
            answer -= dic[roman[i]]
        else:
            answer += dic[roman[i]]
        i += 1
    answer += dic[roman[-1]]
    return answer

if __name__ == '__main__':

    # the following should return 1994
    print(roman_to_int('MCMXCIV'))
