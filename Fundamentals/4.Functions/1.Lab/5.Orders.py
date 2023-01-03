def item_price_calculator(item_type, quantity):
    single_price = 0

    if item_type == "coffee":
        single_price = 1.50
    elif item_type == "water":
        single_price = 1
    elif item_type == "coke":
        single_price = 1.40
    elif item_type == "snacks":
        single_price = 2

    return single_price * quantity

order_type = input()
order_quantity = int(input())
final_price = item_price_calculator(order_type, order_quantity)

print(f"{final_price:.2f}")
