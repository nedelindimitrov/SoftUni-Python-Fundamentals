def bakery_func():

    bakery_dict = {}
    command = input()

    while command != "statistics":
        token = command.split(": ")
        current_product = token[0]
        current_quantity = int(token[1])

        if current_product not in bakery_dict:
            bakery_dict[current_product] = 0
        bakery_dict[current_product] += current_quantity

        command = input()

    print("Products in stock:")
    for (product, quantity) in bakery_dict.items():
        print(f"- {product}: {quantity}")
    print(f"Total Products: {len(bakery_dict.keys())}")
    print(f"Total Quantity: {sum(bakery_dict.values())}")


bakery_func()
