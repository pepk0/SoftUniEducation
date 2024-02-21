target_book = input()
current_book = ""
books_looked_trough = 0 

while target_book != current_book:

    current_book = input()
    if current_book == target_book:
        continue
    
    if current_book == "No More Books":
        print("The book you search is not here!", 
              f"You checked {books_looked_trough} books.", sep="\n")
        break
    books_looked_trough += 1

else:
    print(f"You checked {books_looked_trough} books and found it.")

