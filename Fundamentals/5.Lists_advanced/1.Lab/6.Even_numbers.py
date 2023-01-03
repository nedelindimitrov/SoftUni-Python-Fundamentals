numbers_input = input().split(", ")
indices_list = list()

for i in range(len(numbers_input)):
    current_number = int(numbers_input[i])
    current_index = int(i)
    if current_number % 2 == 0:
        indices_list.append(current_index)

print(indices_list)
