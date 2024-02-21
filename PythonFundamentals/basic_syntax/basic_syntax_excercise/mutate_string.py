first_string = input()
second_string = input()
index = 0
previous_word = first_string

while index < len(first_string):

    first_string = (first_string[:index] + second_string[index] 
                    + first_string[index + 1:])
    index += 1

    if previous_word != first_string :
        print(first_string)

    previous_word = first_string