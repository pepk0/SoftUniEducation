len_set_one, len_set_two = [int(i) for i in input().split()]

set_one = {int(input()) for _ in range(len_set_one)}
set_two = {int(input()) for _ in range(len_set_two)}

print(*set_one.intersection(set_two), sep="\n")
