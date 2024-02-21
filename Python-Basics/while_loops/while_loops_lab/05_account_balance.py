total_bank_account = 0

while total_bank_account >= 0:

    deposit_amount = input()
    if deposit_amount == "NoMoreMoney":
        break
    
    deposit_amount = float(deposit_amount)
    if deposit_amount < 0:
        print("Invalid operation!")
        break
    
    total_bank_account += deposit_amount
    print(f"Increase: {deposit_amount:.2f}")

print(f"Total: {total_bank_account:.2f}")
