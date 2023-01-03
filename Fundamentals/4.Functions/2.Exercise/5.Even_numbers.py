def filter_func(integers):
    even_list = list()
    for i in integers:
        i = int(i)
        if i % 2 == 0:
            even_list.append(i)

    return even_list

input_numbers = input().split(" ")

print(filter_func(input_numbers))
