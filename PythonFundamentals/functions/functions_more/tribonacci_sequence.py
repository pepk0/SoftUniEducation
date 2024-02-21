def tribonacci(num: int) -> list:
    tribonacci_sequence = [1, 1, 2]
    prev_three = 0
    if num <= 3:
        return tribonacci_sequence[:num]
    while len(tribonacci_sequence) < num:
        sum_prev_three = sum(tribonacci_sequence[prev_three:])
        tribonacci_sequence.append(sum_prev_three)
        prev_three += 1
    return tribonacci_sequence


nth_tribonacci = int(input())
print(*tribonacci(nth_tribonacci))
