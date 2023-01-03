two_strings = input().split(" ")

# We use ord() for ascii char to num

first_string = two_strings[0]
second_string = two_strings[1]

total_sum = 0

if len(first_string) == len(second_string):

    for i in range(len(first_string)):
        current_num_one = ord(first_string[i])
        current_num_two = ord(second_string[i])

        result = current_num_one * current_num_two
        total_sum += result


elif len(first_string) < len(second_string):

    for i in range(len(first_string)):
        current_num_one = ord(first_string[i])
        current_num_two = ord(second_string[i])

        result = current_num_one * current_num_two
        total_sum += result

    for i in range(len(first_string), len(second_string)):
        current_num = ord(second_string[i])
        result = current_num
        total_sum += result

elif len(first_string) > len(second_string):

    for i in range(len(second_string)):
        current_num_one = ord(first_string[i])
        current_num_two = ord(second_string[i])

        result = current_num_one * current_num_two
        total_sum += result

    for i in range(len(second_string), len(first_string)):
        current_num = ord(first_string[i])
        result = current_num
        total_sum += result

print(total_sum)
