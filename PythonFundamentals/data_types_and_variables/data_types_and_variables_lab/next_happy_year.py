input_year = int(input())

while True:

    input_year += 1  # counter here because it must be the next year!

    str_year = str(input_year)
    if len(str_year) == len([el for el in str_year if str_year.count(el) == 1]):
        print(str_year)
        break
