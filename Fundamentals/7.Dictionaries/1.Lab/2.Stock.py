def bakery_func():
    input_list = input().split(" ")
    bakery_dict = {}

    for i in range(0, len(input_list), 2):
        key = input_list[i]
        value = int(input_list[i + 1])

        bakery_dict[key] = value

    customer_needs = input().split(" ")

    for i in range(len(customer_needs)):
        current_item = customer_needs[i]

        if current_item in input_list:
            print(f"We have {bakery_dict[current_item]} of {current_item} left")
        else:
            print(f"Sorry, we don't have {current_item}")


bakery_func()
