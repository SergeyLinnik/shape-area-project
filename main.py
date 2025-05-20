from shape import Rectangle, Circle


def main():
    shapes = [
        Rectangle(5, 10),
        Circle(7)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} площадью: {shape.area()}")


if __name__ == "__main__":
    main()
