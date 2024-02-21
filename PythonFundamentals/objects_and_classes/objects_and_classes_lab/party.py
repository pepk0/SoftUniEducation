class Party:
    def __init__(self) -> None:
        self.people = []


party = Party()
while 1:
    person_name = input()
    if person_name == "End":
        break
    else:
        party.people.append(person_name)

print(f"Going: {', '.join(party.people)}",
      f"Total: {len(party.people)}", sep="\n")
