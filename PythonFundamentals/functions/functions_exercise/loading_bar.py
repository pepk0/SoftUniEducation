def percent_bar(percent: int) -> str:
    bar = percent // 10
    loading_bar = "%" * bar + "." * (10 - bar)
    return f"[{loading_bar}]"


def get_output(percent: int) -> str:
    string_percent = f"{percent}%"
    bar = percent_bar(percent)
    if percent != 100:
        return f"{string_percent} {bar}\nStill loading..."
    return f"{string_percent} Complete!\n{bar}"


percent_as_int = int(input())
print(get_output(percent_as_int))
