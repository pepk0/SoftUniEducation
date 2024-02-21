first_pair_start = int(input())
second_pair_start = int(input())
first_pair_difference = int(input())
second_pair_difference = int(input())

first_pair_end = first_pair_start + first_pair_difference
second_pair_end = second_pair_start + second_pair_difference

for first_pair in range(first_pair_start, first_pair_end + 1):
        is_first_pair_prime = True
        
        for deviser in range(2, int(first_pair//2)):
            if first_pair % deviser == 0:
                is_first_pair_prime = False
                break
        
        if not is_first_pair_prime:
            continue
        
        for second_pair in range(second_pair_start, second_pair_end + 1):
            is_second_pair_prime = True
            
            for deviser in range(2, int(second_pair//2)):
                if second_pair % deviser == 0:
                    is_second_pair_prime = False
                    break

            if not is_second_pair_prime:
                continue        
                
            print(f"{first_pair}{second_pair}")

