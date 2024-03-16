def reverse_text(string: str):
    for element in string[::-1]:
        yield element

#
# for char in reverse_text("step"):
#     print(char, end='')
