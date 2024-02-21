key = int(input())
number_of_symbols = int(input())
result = ""

for _ in range(number_of_symbols):

    symbol = input()
    result += chr(ord(symbol) + key)

print(result)
