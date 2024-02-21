def palindrome(word: str, index: int) -> str:
    def is_palindrome(word_: str) -> bool:
        if len(word_) == 1:
            return True

        if word_[0] != word_[-1]:
            return False

        return is_palindrome(word_[1:-1])

    return f"{word} is a palindrome" if is_palindrome(
        word) else f"{word} is not a palindrome"

# print(palindrome("cabac", 0))
