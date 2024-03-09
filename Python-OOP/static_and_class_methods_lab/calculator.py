from collections import deque


class Calculator:

    @staticmethod
    def operation(operator: str, nums: tuple) -> int or float:
        operators = {
            "divide": lambda x, y: x / y,
            "multiply": lambda x, y: x * y,
            "subtract": lambda x, y: x - y,
        }

        line = deque(nums)

        while len(line) > 1:
            first_el, second_el = line.popleft(), line.popleft()
            line.appendleft(operators[operator](first_el, second_el))

        return line.pop()

    @staticmethod
    def add(*nums) -> int:
        return sum(nums)

    @staticmethod
    def multiply(*nums) -> int or float:
        return Calculator.operation("multiply", nums)

    @staticmethod
    def divide(*nums) -> int or float:
        return Calculator.operation("divide", nums)

    @staticmethod
    def subtract(*nums) -> int or float:
        return Calculator.operation("subtract", nums)
