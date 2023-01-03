number_of_orders = int(input())

total_money = 0


for _ in range(number_of_orders):
    skip = False

    price_per_capsule = float(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        skip = True

    days = int(input())
    if days < 1 or days > 31:
        skip = True

    capsules_per_day = int(input())
    if capsules_per_day < 1 or capsules_per_day > 2000:
        skip = True

    current_total = days * capsules_per_day * price_per_capsule

    if skip:
        continue
    else:
        print(f"The price for the coffee is: ${current_total:.2f}")
        total_money += current_total
        continue

print(f"Total: ${total_money:.2f}")
