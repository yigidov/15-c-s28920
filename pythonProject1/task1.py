squares = [x ** 2 for x in range(1, 11)]

print("List of squares from 1 to 10:")
print(squares)


def e_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


if __name__ == "__main__":
    start = 1
    end = 10

    squares = e_squares(start, end)

    print("List of squares of numbers from", start, "to", end, ":")
    print(squares)


class SquareGenerator:
    def generate_squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]


if __name__ == "__main__":
    square_gen = SquareGenerator()

    start = 1
    end = 10

    squares = square_gen.generate_squares(start, end)

    print("List of squares of numbers from", start, "to", end, ":")
    print(squares)

import math


class SquareGenerator:
    def generate_squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]


if __name__ == "__main__":
    square_gen = SquareGenerator()
    start = 1
    end = 10

    squares = square_gen.generate_squares(start, end)
    square_roots = [math.sqrt(x) for x in squares]

    print("Square roots of numbers from", start, "to", end, ":")
    print(square_roots)

# class SquareGenerator:
#     def generate_squares(self, start, end):
#         if end < start:
#             raise ValueError("End of range cannot be less than start")
#
#         return [x ** 2 for x in range(start, end + 1)]
#
# from square_generator import SquareGenerator
from square_generator.square_generator import SquareGenerator

if __name__ == "__main__":
    square_gen = SquareGenerator()

    start = 1
    end = 10

    try:
        squares = square_gen.generate_squares(start, end)

        print("List of squares of numbers from", start, "to", end, ":")
        print(squares)
    except ValueError as e:
        print("Error:", e)

from square_generator.square_generator import CubicGenerator

if __name__ == "__main__":
    cubic_gen = CubicGenerator()

    start = 1
    end = 10

    try:
        cubes = cubic_gen.generate_cubes(start, end)

        print("List of cubes of numbers from", start, "to", end, ":")
        print(cubes)
    except ValueError as e:
        print("Error:", e)
