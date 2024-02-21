def get_result(grade: float) -> str:
    result = "Fail"
    if 3 <= grade <= 3.49:
        result = "Poor"
    elif 3.5 <= grade <= 4.49:
        result = "Good"
    elif 4.5 <= grade <= 5.49:
        result = "Very Good"
    elif 5.5 <= grade <= 6:
        result = "Excellent"
    return result


grade_as_float = float(input())
print(get_result(grade_as_float))
