first_symbol = input()
second_symbol = input()

first_ord = ord(first_symbol)
second_ord = ord(second_symbol)

for ch in range(first_ord + 1, second_ord):
    print(chr(ch), end=" ")
