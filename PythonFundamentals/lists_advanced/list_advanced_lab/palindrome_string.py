words_list = [word for word in input().split()]
palindrome = input()
def condition(x): return x == x[::-1]

list_of_palindromes = [word for word in words_list if condition(word)]
palindrome_occurrences = list_of_palindromes.count(palindrome)
print(list_of_palindromes,
      f"Found palindrome {palindrome_occurrences} times", sep="\n")
