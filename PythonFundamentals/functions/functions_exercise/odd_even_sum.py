def even_odd_sum(num: str) -> tuple:
    even_result = 0
    odd_result = 0
    for i in range(len(num)):
        num_as_int = int(num[i])
        if num_as_int % 2 == 0:
            even_result += num_as_int
        else:
            odd_result += num_as_int
    return even_result, odd_result


number = input()
even_sum, odd_sum = even_odd_sum(number)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
