reservations = {input() for _ in range(int(input()))}
guests_attended = set()
command = input()

while command != "END":
    guests_attended.add(command)
    command = input()

not_attended = reservations.difference(guests_attended)
print(len(not_attended), *sorted(not_attended), sep="\n")
