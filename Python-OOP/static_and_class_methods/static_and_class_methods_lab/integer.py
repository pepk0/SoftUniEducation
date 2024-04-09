class Integer:
    def __init__(self, value: int or float or str) -> None:
        self.value = value

    @classmethod
    def from_float(cls, value: float):
        if isinstance(value, float):
            return cls(int(value))
        return "value is not a float"

    @classmethod
    def from_string(cls, value: str):
        if isinstance(value, str):
            return cls(int(value))
        return "wrong type"

    @classmethod
    def from_roman(cls, value: str):
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                   'M': 1000}

        total_sum = 0

        for i in range(len(value)):
            if i != 0 and mapping[value[i]] > mapping[value[i - 1]]:
                total_sum += mapping[value[i]] - 2 * mapping[value[i - 1]]
            else:

                total_sum += mapping[value[i]]

        return cls(total_sum)

# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
