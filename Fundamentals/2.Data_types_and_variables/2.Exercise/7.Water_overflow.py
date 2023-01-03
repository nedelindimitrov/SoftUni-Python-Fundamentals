num_of_lines = int(input())
liters = 255

for n in range(num_of_lines):
    current_liters = int(input())
    if current_liters <= liters:
        liters -= current_liters
    else:
        print("Insufficient capacity!")
        continue
print(255 - liters)
