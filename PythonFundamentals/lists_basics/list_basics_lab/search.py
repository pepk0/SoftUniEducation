number = int(input())
word = input()

filtered_word = []
unfiltered_word = []

for _ in range(number):

    phrase = input()

    if word in phrase:
        filtered_word.append(phrase)
    
    unfiltered_word.append(phrase)

print(unfiltered_word, filtered_word, sep="\n")
