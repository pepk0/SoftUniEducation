def sum_of_devisors(num: int) -> int:
    devisors = []
    for i in range(1, num):
        if num % i == 0:
            devisors.append(i)
    return sum(devisors)


def is_perfect_number(num: int) -> str:
    if num == sum_of_devisors(num):
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect_number(number))
