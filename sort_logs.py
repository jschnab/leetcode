# script to sort list of logs with the following format:
# ['aw2 act car zoo', 'di9 1 8 4', 'po9 act car zoo', 'me7 9 4 6', 'ml4 cat dog bob']
# first element of log is index, all other elements are body
# sort letter-containing logs alphanumerically based on body then break ties with index
# do not sort digit-containing logs
# return list of sorted letter logs then digits logs

def sort_logs(logs):
    """Sort logs."""

    # sorting key function
    def fun(log):
        id_, body = log.split(' ', 1)
        return (0, body, id_) if body[0].isalpha() else (1,)

    return sorted(logs, key=fun)

if __name__ == '__main__':
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print(sort_logs(logs))
