def vowel_filter(function):
    def wrapper():
        results = function()
        return [letter for letter in results if letter.lower() in "ayeiou"]

    return wrapper
