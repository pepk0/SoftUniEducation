list_of_elements = [int(i) for i in input().split(", ")]
max_element = max(list_of_elements)

for group in range(10, max_element + 10, 10):
    print(f"Group of {group}'s: "
          f"{[i for i in list_of_elements if group - 10 < i <= group]}")
