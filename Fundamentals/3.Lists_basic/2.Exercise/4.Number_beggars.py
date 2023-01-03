numbers = input().split(", ")
count_of_beggars = int(input())

final_list = list()

for b in range(count_of_beggars):
    sum = 0

    for nums in range(b, len(numbers), count_of_beggars):
        sum += int(numbers[nums])
    final_list.append(sum)

print(final_list)
