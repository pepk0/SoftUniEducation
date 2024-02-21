numbers = int(input())
even_sum = 0
max_even = -float("inf")
min_even = float("inf")
odd_sum = 0
max_odd = -float("inf")
min_odd = float("inf")

for number in range(1, numbers + 1):

    current_number = float(input())

    if number % 2 != 0:
        odd_sum += current_number
        if current_number > max_odd:
            max_odd = current_number
        if current_number < min_odd:
            min_odd = current_number
    
    else:
        even_sum += current_number
        if current_number > max_even:
            max_even = current_number
        if current_number < min_even:
            min_even = current_number
    
print(f"OddSum={odd_sum:.2f},")
if min_odd == float("inf"):
    print("OddMin=No,")
else:
    print(f"OddMin={min_odd:.2f},")
if max_odd == -float("inf"):
    print("OddMax=No,")
else:
    print(f"OddMax={max_odd:.2f},")    
print(f"EvenSum={even_sum:.2f},")
if min_even == float("inf"):
    print("EvenMin=No,")
else:
    print(f"EvenMin={min_even:.2f},")
if max_even == -float("inf"):
    print("EvenMax=No")
else:
    print(f"EvenMax={max_even:.2f}")    
