import regex as re
import sys
import cProfile


def main():
    with open('4_input') as f:
        data=f.readlines()

    board = [l.strip() for l in data]
    c =len(board[0])
    board  = ''.join(board)

    print(len(list(filter(lambda m: (m.span()[0] % c) < c-2, re.finditer(rf'(?:(M)|(S)).(?:(M)|(S)).{{{c-2}}}A.{{{c-2}}}(?(3)S|(?(4)M|\n)).(?(1)S|(?(2)M|\n))', board, overlapped=True)))))

cProfile.run('main()')