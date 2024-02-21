def sorting_cheeses(**kwargs) -> str:
    result = []

    for cheese, pieces in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(cheese)
        [result.append(str(el)) for el in sorted(pieces, reverse=True)]


    return "\n".join(result)


# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )