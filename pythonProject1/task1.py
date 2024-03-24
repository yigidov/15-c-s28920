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
