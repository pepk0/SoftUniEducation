condition = lambda x: len(x) % 2 == 0 
words = [el for el in input().split()]
print(*[word for word in words if condition(word)], sep="\n")
