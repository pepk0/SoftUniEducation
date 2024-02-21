def rectangle(length: int, width: int) -> str:
    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    def area() -> int:
        return width * length

    def perimeter() -> int:
        return 2 * (width + length)

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

# print(rectangle(2, 10))

# print(rectangle('2', 10))
