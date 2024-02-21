# nested list comprehension, to calculate the sum of each element
indexes = [sum([int(i) for i in j]) for j in input().split()]
string = input()

phrase = ""
for index in indexes:
    while index >= len(string):
        index = index % len(string)
    phrase += string[index]
    string = string[:index] + string[index + 1:]

print(phrase)
