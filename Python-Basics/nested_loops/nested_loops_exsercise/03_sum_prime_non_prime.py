prime_sum = 0
non_prime_sum = 0
number = input()

while number != "stop":

    number = int(number)

    if number < 0:
        print("Number is negative.")
    
    elif number == 1:
        non_prime_sum += number
    
    elif number > 1:
        for deviser in range(2, int(number/2) + 1):
            if number % deviser == 0:
                non_prime_sum += number
                break
        else:
            prime_sum += number

    number = input()

print(f"Sum of all prime numbers is: {prime_sum}",
      f"Sum of all non prime numbers is: {non_prime_sum}", sep="\n")
