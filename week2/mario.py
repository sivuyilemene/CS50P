
from operator import le
from traceback import print_tb


def main():
    print_column(3)
    print_row(4)
    print_square(3)


def print_column(height):
    for _ in range(height):
        print("#")


def print_row(width):
    print("?" * width)


def print_square(size):
    for _ in range(size):
        print("#" * size)
#   # For each row in square
#     for i in range(size):
#         # For each brick in row
#         for j in range(size):
#             # print brick
#             print("#", end="")
#         print()


main()
