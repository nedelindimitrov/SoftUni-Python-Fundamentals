def even_odd_func(string):
    current_string = string
    even_sum = 0
    odd_sum = 0

    for i in range(len(current_string)):
        current_num = int(current_string[i])
        if current_num % 2 == 0:
            even_sum += current_num
        elif current_num % 2 != 0:
            odd_sum += current_num

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

input_string = input()

even_odd_func(input_string)
