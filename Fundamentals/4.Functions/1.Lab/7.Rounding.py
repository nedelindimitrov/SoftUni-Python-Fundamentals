def rounding_list(current_list):
    rounded_list = list()
    new_int_list = map(int, current_list)

    for integer in range(len(current_list)):
        new_integer = current_list[integer]
        new_integer = round(float(new_integer))
        rounded_list.append(new_integer)
    print(rounded_list)

current_list_input = input().split(" ")

rounding_list(current_list_input)
