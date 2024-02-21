def add_employ(company: str, id_: str, companies: dict) -> None:
    if company not in companies:
        companies[company] = []
    if id_ not in companies[company]:
        companies[company].append(id_)


companies_register = {}
while 1:
    employ_information = input().split(" -> ")
    if employ_information[0] == "End":
        break
    employ_company, employ_id = employ_information
    add_employ(employ_company, employ_id, companies_register)

for company_name, company_employs in companies_register.items():
    print(f"{company_name}")
    print(*[f"-- {employ}" for employ in company_employs], sep="\n")
