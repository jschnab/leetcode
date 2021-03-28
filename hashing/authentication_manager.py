# design an authentication manager: leetcode challenge 1797
# the system works with authentication tokens
# for each session the user will receive a new authentication token that will
# expire 'ttl' seconds after the 'timestamp'
# if the token is renewed, the expiry time will be extended to expire 'ttl'
# seconds after the given 'timestamp'
# class 'AuthenticationManager' sets 'ttl'
# method 'generate(str tokenId, int timestamp)'
# method 'renew(str tokenId, int timestamp)' renews unexpired token
# method 'countUnexpired(int timestamp)' returns number of unexpired tokens


from collections import OrderedDict


class AuthenticationManager:
    def __init__(self, ttl):
        self.tokens = OrderedDict()
        self.ttl = ttl

    def generate(self, tokenId, timestamp):
        self.evictExpired(timestamp)
        self.tokens[tokenId] = timestamp + self.ttl

    def renew(self, tokenId, timestamp):
        self.evictExpired(timestamp)
        if tokenId in self.tokens:
            self.tokens[tokenId] = timestamp + self.ttl
            self.tokens.move_to_end(tokenId)

    def countUnexpired(self, timestamp):
        self.evictExpired(timestamp)
        return len(self.tokens)

    def evictExpired(self, timestamp):
        while self.tokens and next(iter(self.tokens.values())) <= timestamp:
            self.tokens.popitem(last=False)


def test1():
    auth = AuthenticationManager(5)
    auth.renew("aaa", 1)
    assert auth.countUnexpired(2) == 0
    auth.generate("aaa", 2)
    assert auth.countUnexpired(6) == 1
    auth.generate("bbb", 7)
    assert auth.countUnexpired(7) == 1
    auth.renew("aaa", 8)
    assert auth.countUnexpired(9) == 1
    auth.renew("bbb", 10)
    assert auth.countUnexpired(15) == 0


def main():
    test1()


if __name__ == "__main__":
    main()
