material_dict = {}

while True:
    command = input()

    if command == "stop":
        break

    quantity = int(input())

    if command not in material_dict:
        material_dict[command] = quantity
    else:
        material_dict[command] += quantity

for key, value in material_dict.items():
    print(f"{key} -> {value}")
