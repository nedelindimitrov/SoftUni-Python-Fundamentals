first_list = input().split(" ")
copy_list = list(map(int, first_list))
rounds = int(input())

for _ in range(rounds):
    current_min_num = min(copy_list)
    first_list.remove(str(current_min_num))
    copy_list.remove(current_min_num)

print(', '.join(first_list))
