user_name = input()
password = input()
entered_password = ""

while entered_password != password:
    entered_password = input()

else:
    print(f"Welcome {user_name}!")