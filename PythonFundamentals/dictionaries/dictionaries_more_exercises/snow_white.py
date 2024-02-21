def add_dwarf(dwarf_name: str, dwarf_hat_color: str,
              dwarf_physique: int, dwarfs: dict) -> None:
    if (dwarf_hat_color, dwarf_name) not in dwarfs:
        dwarfs[(dwarf_hat_color, dwarf_name)] = dwarf_physique
    else:
        if dwarfs[(dwarf_hat_color, dwarf_name)] <= dwarf_physique:
            dwarfs[(dwarf_hat_color, dwarf_name)] = dwarf_physique


def count_hat_color(dwarfs: dict) -> dict:
    result = {}
    for hat_color, _ in dwarfs:
        if hat_color not in result:
            result[hat_color] = 0
        result[hat_color] += 1
    return result


all_dwarfs = {}
while True:
    dwarf = input().split(" <:> ")
    if len(dwarf) <= 1:
        break
    dwarf_name, dwarf_hat_color, dwarf_physique = dwarf
    add_dwarf(dwarf_name, dwarf_hat_color, int(dwarf_physique), all_dwarfs)

colored_hats = count_hat_color(all_dwarfs)
for (hat_color, name), physique in sorted(
        all_dwarfs.items(), key=lambda x: (-x[1], -colored_hats[x[0][0]])):
    print(f"({hat_color}) {name} <-> {physique}")
