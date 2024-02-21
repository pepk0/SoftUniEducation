def draw(n: int) -> None:

    if n == 1:
        print("*", "#", sep="\n")
        return

    print("*" * n)

    draw(n - 1)

    print("#" * n)


draw(int(input()))
