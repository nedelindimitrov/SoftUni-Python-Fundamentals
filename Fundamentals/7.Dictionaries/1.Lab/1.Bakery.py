def bakery_func():
    input_list = input().split(" ")
    bakery_dict = {}

    for i in range(0, len(input_list), 2):
        key = input_list[i]
        value = int(input_list[i + 1])

        bakery_dict[key] = value

    print(bakery_dict)


bakery_func()
