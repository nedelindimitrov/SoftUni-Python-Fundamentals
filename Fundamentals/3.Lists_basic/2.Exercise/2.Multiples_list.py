number1 = int(input())
number2 = int(input())
list_nums = list()

for num in range(1, number2 + 1):
    current_num = number1 * num
    list_nums.append(current_num)

print(list_nums)
