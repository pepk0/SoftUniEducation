from math import ceil

number_people = int(input())
capacity = int(input())

courses = ceil(number_people / capacity)
print(courses)
