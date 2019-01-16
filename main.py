from lab_2.lab_python_oop.shapes import Rectangle, Circle, Square
from lab_2.lab_python_oop.color import Color


def main():
    rectangle = Rectangle(3, 2, Color('синий'))
    circle = Circle(5, Color('зеленый'))
    square = Square(5, Color('красный'))

    shapes = [rectangle, circle, square]
    result = ', '.join(str(shape) for shape in shapes)

    print("У меня есть:", result)


if __name__ == '__main__':
    # execute only if run as a script
    main()