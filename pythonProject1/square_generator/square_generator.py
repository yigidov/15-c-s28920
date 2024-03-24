
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range cannot be less than start")

        return [x ** 2 for x in range(start, end + 1)]


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):

        if end < start:
            raise ValueError("End of range cannot be less than start")

        return [x ** 3 for x in range(start, end + 1)]

    def generate_squares(self, start, end):

        if start > end:
            raise ValueError("Start of range cannot be greater than end")

        return [x ** 2 for x in range(start, end + 1)]