largest_num = int(input())

for _ in range(2):
    current = int(input())
    if current > largest_num:
        largest_num = current

print(largest_num)
