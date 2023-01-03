interval = int(input())
total_sum = 0

for digit in range(interval):
    current_symbol = input()
    symbol_meaning = ord(current_symbol)
    total_sum += symbol_meaning

print(f"The sum equals: {total_sum}")
