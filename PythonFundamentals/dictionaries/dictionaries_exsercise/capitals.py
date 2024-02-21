def combine(countries_list: list, capitals_list: list) -> dict:
    return {countries_list[i]: capitals_list[i]
            for i in range(len(capitals_list))}


countries = input().split(", ")
capitals = input().split(", ")
print(*[f"{k} -> {v}" for k, v in combine(countries, capitals).items()],
       sep="\n")
