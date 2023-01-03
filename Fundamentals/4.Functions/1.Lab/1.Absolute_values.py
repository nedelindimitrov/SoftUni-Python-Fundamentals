def upper_nums():
    input_list = input().split(" ")
    input_len = len(input_list)
    new_list = list()

    for i in range(input_len):
        current_num = abs(float(input_list[i]))
        new_list.append(current_num)

    print(new_list)

upper_nums()
