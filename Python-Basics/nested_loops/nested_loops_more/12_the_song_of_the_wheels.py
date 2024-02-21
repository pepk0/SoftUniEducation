control_number = int(input())
password_counter = 0
valid_password = ""

for digit_a in range(1, 10):
    for digit_b in range(1, 10):
        for digit_c in range(1, 10):
            for digit_d in range(1, 10):

                condition_one = (control_number == (digit_a * digit_b) 
                                 + (digit_c * digit_d))
                condition_two = digit_a < digit_b
                condition_three = digit_c > digit_d

                if condition_one and condition_two and condition_three:
                    password_counter += 1
                    generated_password = f"{digit_a}{digit_b}{digit_c}{digit_d}"
                    print(generated_password, end=" ")

                    if password_counter == 4:
                        valid_password = generated_password

print()
if valid_password:
    print(f"Password: {valid_password}")
else:
    print("No!")