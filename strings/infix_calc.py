#!/usr/bin/env python3

import re
import sys


def evaluate(tokens):
    operand = 0
    operator = None
    sub_tokens = []
    for tok in tokens:
        if tok.isnumeric():
            tok = int(tok)
            if operator is None:
                operand = tok
            else:
                if operator == "+":
                    operand += tok
                elif operator == "-":
                    operand -= tok
                operator = None
        elif tok in "+-":
            operator = tok
        elif tok == "(":
            pcnt = 1
            while tok != ")" and pcnt > 0:
                tok = next(tokens)
                sub_tokens.append(tok)
                if tok == "(":
                    pcnt += 1
                elif tok == ")":
                    pcnt -= 1
            sub_tokens.pop()
            sub_eval = evaluate(sub_tokens)
            if operator is None:
                operand = sub_eval
            else:
                if operator == "+":
                    operand += sub_eval
                elif operator == "-":
                    operand -= sub_eval
                operator = None
    return operand


def tokenize(expr):
    return iter(re.findall(r"\d+|[()+-]", expr))


def main(expr):
    print(evaluate(tokenize(expr)))


def test():
    main("3 + 4")
    main("3 + 4 + 5")
    main("3 - 4")
    main("3 - 4 - 5")
    main("3 + (4 + 5)")
    main("3 + (4 + 5) - 6")
    main("(3 + 4)")
    main("-3")
    main("-(3 + 4)")


if __name__ == "__main__":
    #main(sys.argv[1])
    test()
