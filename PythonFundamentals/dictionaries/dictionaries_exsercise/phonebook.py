def find_user(user_name: str, phonebook: dict) -> str:
    result = f"Contact {user_name} does not exist."
    if user_name in phonebook:
        result = f"{user_name} -> {phonebook[user_name]}"
    return result


contact_phonebook = {}
number_searches = 0
while 1:
    user_information = input().split("-")
    if len(user_information) <= 1:
        number_searches = int(user_information[0])
        break
    user_name, user_phone_number = user_information
    contact_phonebook[user_name] = user_phone_number

for _ in range(number_searches):
    user_query = input()
    print(find_user(user_query, contact_phonebook))
