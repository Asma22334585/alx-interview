#!/usr/bin/python3
import sys


def place(pos, occupied_pos):
    for i in range(len(occupied_pos)):
        if (
            occupied_pos[i] == pos
            or occupied_pos[i] - i == pos - len(occupied_pos)
            or occupied_pos[i] + i == pos + len(occupied_pos)
        ):
            return False
    return True


def queens(n, index, occupied_pos, all_taken_pos):
    if index == n:
        all_taken_pos.append(occupied_pos[:])
        return

    for i in range(n):
        if place(i, occupied_pos):
            occupied_pos.append(i)
            queens(n, index + 1, occupied_pos, all_taken_pos)
            occupied_pos.pop()


def solveQueens(n):
    all_taken_pos = []
    queens(n, 0, [], all_taken_pos)
    return all_taken_pos


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solveQueens(n)
    for solution in solutions:
        r = [[i, pos] for i, pos in enumerate(solution)]
        print(r)


if __name__ == "__main__":
    main()
